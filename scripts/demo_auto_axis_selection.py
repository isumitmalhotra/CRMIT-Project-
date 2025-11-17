"""
Demo Script: Auto-Axis Selection for FCS Data

Demonstrates the auto-axis selection feature that intelligently recommends
the best channel combinations for scatter plot visualization.

Author: GitHub Copilot
Date: November 16, 2025
Task: Phase 2 - Auto-Axis Selection Implementation
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from parsers.fcs_parser import FCSParser
from visualization.auto_axis_selector import AutoAxisSelector
from visualization.fcs_plots import FCSPlotter
import pandas as pd
from loguru import logger

# Configure logger
logger.remove()
logger.add(sys.stdout, format="<green>{time:HH:mm:ss}</green> | <level>{level: <8}</level> | <level>{message}</level>")


def demo_auto_axis_selection():
    """Demonstrate auto-axis selection with real FCS data."""
    
    print("\n" + "="*70)
    print(" "*15 + "AUTO-AXIS SELECTION DEMO")
    print("="*70 + "\n")
    
    # Find FCS files
    fcs_dir = Path("nanoFACS/10000 exo and cd81")
    fcs_files = list(fcs_dir.glob("*.fcs"))
    
    if not fcs_files:
        print("❌ No FCS files found in:", fcs_dir)
        return
    
    # Use first file
    fcs_file = fcs_files[0]
    print(f"📁 Analyzing: {fcs_file.name}\n")
    
    # Parse FCS file
    logger.info("Parsing FCS file...")
    parser = FCSParser(file_path=fcs_file)
    data = parser.parse()
    
    print(f"✓ Loaded {len(data):,} events with {len(data.columns)} channels\n")
    
    # Initialize auto-axis selector
    selector = AutoAxisSelector(
        min_variance_threshold=0.1,
        max_correlation_threshold=0.95,
        sample_size=10000
    )
    
    # Generate recommendations
    print("🔍 Analyzing channel combinations...")
    recommendations = selector.generate_recommendations(data, n_recommendations=7)
    
    # Display recommendations
    print("\n" + "─"*70)
    print("📊 RECOMMENDED CHANNEL PAIRS (Ranked by Quality Score)")
    print("─"*70 + "\n")
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', None)
    pd.set_option('display.max_colwidth', 50)
    
    # Format recommendations
    print(recommendations.to_string(index=False))
    
    # Highlight top 3
    print("\n" + "─"*70)
    print("⭐ TOP 3 RECOMMENDATIONS:")
    print("─"*70)
    
    for idx in range(min(3, len(recommendations))):
        rec = recommendations.iloc[idx]
        print(f"\n{idx+1}. {rec['x_channel']} vs {rec['y_channel']}")
        print(f"   Score: {rec['score']:.3f}")
        print(f"   Reason: {rec['reason']}")
    
    # Generate plots for top recommendations
    print("\n" + "─"*70)
    print("📈 GENERATING PLOTS FOR TOP RECOMMENDATIONS")
    print("─"*70 + "\n")
    
    output_dir = Path("figures/auto_axis_demo")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    plotter = FCSPlotter(output_dir=output_dir)
    
    # Generate plots for top 3 recommendations
    for idx in range(min(3, len(recommendations))):
        rec = recommendations.iloc[idx]
        x_ch = rec['x_channel']
        y_ch = rec['y_channel']
        
        print(f"  Generating plot {idx+1}: {x_ch} vs {y_ch}...")
        
        try:
            plotter.plot_scatter(
                data=data,
                x_channel=x_ch,
                y_channel=y_ch,
                title=f"Auto-Selected: {x_ch} vs {y_ch}\nScore: {rec['score']:.3f} - {rec['reason']}",
                output_file=f"rank_{idx+1}_{x_ch}_vs_{y_ch}.png",
                plot_type="density",
                sample_size=50000
            )
            print(f"    ✓ Saved: rank_{idx+1}_{x_ch}_vs_{y_ch}.png")
        except Exception as e:
            print(f"    ❌ Error: {e}")
    
    print(f"\n✅ All plots saved to: {output_dir}")
    
    # Summary statistics
    print("\n" + "="*70)
    print("📊 CHANNEL ANALYSIS SUMMARY")
    print("="*70 + "\n")
    
    # Get numeric channels
    numeric_channels = data.select_dtypes(include=['number']).columns.tolist()
    exclude_cols = ['sample_id', 'event_id', 'Time', 'time', 'index']
    numeric_channels = [col for col in numeric_channels if col not in exclude_cols]
    
    scatter_channels = selector._identify_scatter_channels(numeric_channels)
    fluorescence_channels = selector._identify_fluorescence_channels(numeric_channels)
    
    print(f"Total Channels: {len(numeric_channels)}")
    print(f"  • Scatter Channels: {len(scatter_channels)} {scatter_channels}")
    print(f"  • Fluorescence Channels: {len(fluorescence_channels)} {fluorescence_channels[:5]}{'...' if len(fluorescence_channels) > 5 else ''}")
    print(f"\nTotal Possible Pairs: {len(numeric_channels) * (len(numeric_channels) - 1) // 2}")
    print(f"Recommended Pairs: {len(recommendations)}")
    print(f"Reduction: {100 * (1 - len(recommendations) / (len(numeric_channels) * (len(numeric_channels) - 1) // 2)):.1f}%")
    
    print("\n" + "="*70)
    print("✅ AUTO-AXIS SELECTION DEMO COMPLETE")
    print("="*70 + "\n")


if __name__ == "__main__":
    demo_auto_axis_selection()
