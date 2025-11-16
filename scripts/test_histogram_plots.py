"""
Test Histogram Plotting for Fluorescence Marker Analysis

Demonstrates:
1. Single channel histograms (CD81, CD63, CD9)
2. Multi-marker comparison histograms
3. Gating and % positive calculation
4. Statistical overlays
"""

import sys
from pathlib import Path
import pandas as pd
from loguru import logger

# Add src to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.parsers.fcs_parser import FCSParser
from src.visualization.fcs_plots import FCSPlotter


def test_histogram_plots():
    """Test histogram plotting with real FCS data."""
    
    logger.info("=" * 80)
    logger.info("🧪 TESTING HISTOGRAM PLOTS FOR MARKER ANALYSIS")
    logger.info("=" * 80)
    
    # Find FCS files
    fcs_dir = project_root / "nanoFACS" / "10000 exo and cd81"
    fcs_files = list(fcs_dir.glob("*.fcs"))
    
    if not fcs_files:
        logger.error("No FCS files found")
        return
    
    # Use CD81 file for testing
    test_files = [f for f in fcs_files if 'CD81' in f.name or 'cd81' in f.name]
    if not test_files:
        test_files = fcs_files[:1]
    
    test_file = test_files[0]
    logger.info(f"Using test file: {test_file.name}")
    
    # Parse FCS file
    logger.info("Parsing FCS file...")
    parser = FCSParser(file_path=test_file)
    data = parser.parse()
    
    logger.info(f"Loaded {len(data)} events")
    logger.info(f"Channels: {list(data.columns)}")
    
    # Initialize plotter
    output_dir = project_root / "figures" / "histogram_demo"
    plotter = FCSPlotter(output_dir=output_dir)
    
    # Find fluorescence channels
    fl_channels = [col for col in data.columns 
                   if (col.startswith(('V4', 'B5', 'Y5', 'R6', 'R7')) 
                       and col.endswith('-A'))]
    
    logger.info(f"Found {len(fl_channels)} fluorescence channels: {fl_channels}")
    
    # Test 1: Single channel histogram
    if fl_channels:
        logger.info("\n--- Test 1: Single Channel Histogram ---")
        channel = fl_channels[0]
        logger.info(f"Plotting histogram for {channel}")
        
        plotter.plot_histogram(
            data=data,
            channel=channel,
            output_file=f"single_histogram_{channel}.png",
            bins=256,
            log_scale=True,
            gate_threshold=1000,  # Example threshold
            show_stats=True
        )
        logger.success(f"✅ Created single histogram for {channel}")
    
    # Test 2: Multi-marker comparison
    if len(fl_channels) >= 2:
        logger.info("\n--- Test 2: Multi-Marker Comparison ---")
        logger.info(f"Creating comparison plot for {len(fl_channels[:4])} markers")
        
        # Example gate thresholds
        gate_thresholds = {channel: 1000 for channel in fl_channels[:4]}
        
        plotter.plot_marker_histograms(
            data=data,
            marker_channels=fl_channels[:4],
            output_file="marker_comparison_histograms.png",
            bins=256,
            log_scale=True,
            gate_thresholds=gate_thresholds
        )
        logger.success(f"✅ Created multi-marker comparison plot")
    
    # Test 3: Create individual histograms for each marker
    logger.info("\n--- Test 3: Individual Histograms for Each Marker ---")
    for channel in fl_channels:
        logger.info(f"Creating histogram for {channel}")
        
        plotter.plot_histogram(
            data=data,
            channel=channel,
            output_file=f"histogram_{channel}.png",
            bins=256,
            log_scale=True,
            show_stats=True
        )
    
    logger.success(f"✅ Created {len(fl_channels)} individual histograms")
    
    # Summary
    logger.info("\n" + "=" * 80)
    logger.info("📊 SUMMARY")
    logger.info("=" * 80)
    logger.info(f"📁 Output directory: {output_dir}")
    
    output_files = list(output_dir.glob("*.png"))
    total_size = sum(f.stat().st_size for f in output_files) / (1024 * 1024)
    
    logger.info(f"📈 Histograms created: {len(output_files)}")
    logger.info(f"💾 Total size: {total_size:.2f} MB")
    logger.info("\n✨ Histogram plotting test complete!")


if __name__ == "__main__":
    test_histogram_plots()
