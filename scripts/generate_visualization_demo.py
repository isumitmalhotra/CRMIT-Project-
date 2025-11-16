"""
Visualization Demo Script - Deliverable Demonstration
====================================================

Purpose: Demonstrate all three visualization deliverables:
1. FCS file parser + basic scatter plot generation
2. NTA text file parser + size distribution analysis  
3. Anomaly detection for scatter plot shifts

This script showcases the complete visualization pipeline using real project data.

Author: CRMIT Team
Date: November 15, 2025
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from loguru import logger

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.visualization.fcs_plots import FCSPlotter
from src.visualization.nta_plots import NTAPlotter
from src.visualization.anomaly_detection import AnomalyDetector
from src.parsers.fcs_parser import FCSParser
from src.parsers.nta_parser import NTAParser


def demo_fcs_visualization():
    """
    Deliverable 1: FCS file parser + basic scatter plot generation
    """
    logger.info("=" * 80)
    logger.info("DELIVERABLE 1: FCS File Parser + Basic Scatter Plot Generation")
    logger.info("=" * 80)
    
    # Initialize
    fcs_parser = FCSParser()
    fcs_plotter = FCSPlotter(output_dir=Path("figures/demo/fcs"))
    
    # Find FCS files
    fcs_dir = Path("nanoFACS/10000 exo and cd81")
    if not fcs_dir.exists():
        logger.warning(f"FCS directory not found: {fcs_dir}")
        return None
    
    fcs_files = list(fcs_dir.glob("*.fcs"))[:3]  # Use first 3 files for demo
    
    if not fcs_files:
        logger.warning("No FCS files found")
        return None
    
    logger.info(f"Found {len(fcs_files)} FCS files for visualization")
    
    results = []
    
    for fcs_file in fcs_files:
        try:
            logger.info(f"\n📁 Processing: {fcs_file.name}")
            
            # Parse FCS file
            fcs_data, metadata = fcs_parser.parse_fcs_file(fcs_file)
            
            if fcs_data is None or len(fcs_data) == 0:
                logger.warning(f"  No data from {fcs_file.name}")
                continue
            
            logger.info(f"  ✓ Parsed: {len(fcs_data):,} events, {len(fcs_data.columns)} channels")
            
            # Generate scatter plot (FSC-A vs SSC-A)
            scatter_path = fcs_plotter.plot_scatter(
                fcs_data=fcs_data,
                x_channel='FSC-A',
                y_channel='SSC-A',
                sample_id=metadata.get('sample_id', fcs_file.stem),
                log_scale=True,
                density=True,
                save=True
            )
            
            if scatter_path:
                logger.info(f"  ✓ Scatter plot saved: {scatter_path.name}")
            
            # Generate histograms
            for channel in ['FSC-A', 'SSC-A']:
                if channel in fcs_data.columns:
                    hist_path = fcs_plotter.plot_histogram(
                        fcs_data=fcs_data,
                        channel=channel,
                        sample_id=metadata.get('sample_id', fcs_file.stem),
                        save=True
                    )
                    if hist_path:
                        logger.info(f"  ✓ Histogram saved: {hist_path.name}")
            
            results.append({
                'file': fcs_file.name,
                'events': len(fcs_data),
                'channels': list(fcs_data.columns),
                'scatter_plot': scatter_path
            })
            
        except Exception as e:
            logger.error(f"  ✗ Error processing {fcs_file.name}: {e}")
    
    logger.info(f"\n✅ FCS Visualization Demo Complete: {len(results)} samples processed")
    return results


def demo_nta_visualization():
    """
    Deliverable 2: NTA text file parser + size distribution analysis
    """
    logger.info("\n" + "=" * 80)
    logger.info("DELIVERABLE 2: NTA Text File Parser + Size Distribution Analysis")
    logger.info("=" * 80)
    
    # Initialize
    nta_parser = NTAParser()
    nta_plotter = NTAPlotter(output_dir=Path("figures/demo/nta"))
    
    # Find NTA directories
    nta_base = Path("NTA")
    if not nta_base.exists():
        logger.warning(f"NTA directory not found: {nta_base}")
        return None
    
    nta_dirs = [d for d in nta_base.iterdir() if d.is_dir()][:2]  # Use first 2 for demo
    
    if not nta_dirs:
        logger.warning("No NTA directories found")
        return None
    
    logger.info(f"Found {len(nta_dirs)} NTA sample directories")
    
    results = []
    stats_list = []
    
    for nta_dir in nta_dirs:
        try:
            logger.info(f"\n📁 Processing: {nta_dir.name}")
            
            # Parse NTA directory
            nta_stats = nta_parser.parse_nta_directory(nta_dir)
            
            if nta_stats is None or len(nta_stats) == 0:
                logger.warning(f"  No data from {nta_dir.name}")
                continue
            
            logger.info(f"  ✓ Parsed: {len(nta_stats)} measurements")
            
            # Display key statistics
            if 'mean_size' in nta_stats.columns:
                mean_size = nta_stats['mean_size'].mean()
                logger.info(f"  ✓ Mean size: {mean_size:.1f} nm")
            
            if 'concentration' in nta_stats.columns:
                mean_conc = nta_stats['concentration'].mean()
                logger.info(f"  ✓ Mean concentration: {mean_conc:.2e} particles/mL")
            
            # Generate size distribution plot
            dist_path = nta_plotter.plot_size_distribution(
                nta_data=nta_stats,
                sample_id=nta_dir.name,
                show_percentiles=True,
                save=True
            )
            
            if dist_path:
                logger.info(f"  ✓ Size distribution saved: {dist_path.name}")
            
            stats_list.append((nta_stats, nta_dir.name))
            
            results.append({
                'directory': nta_dir.name,
                'measurements': len(nta_stats),
                'size_dist_plot': dist_path
            })
            
        except Exception as e:
            logger.error(f"  ✗ Error processing {nta_dir.name}: {e}")
    
    # Generate comparison plots if we have multiple samples
    if len(stats_list) >= 2:
        logger.info("\n📊 Generating comparison plots...")
        
        # Combine all stats for comparison
        all_stats = pd.concat([stats for stats, _ in stats_list], ignore_index=True)
        
        # Concentration comparison
        conc_path = nta_plotter.plot_concentration_comparison(
            nta_stats=all_stats,
            save=True
        )
        if conc_path:
            logger.info(f"  ✓ Concentration comparison: {conc_path.name}")
        
        # D-values comparison
        d_path = nta_plotter.plot_d_values_comparison(
            nta_stats=all_stats,
            save=True
        )
        if d_path:
            logger.info(f"  ✓ D-values comparison: {d_path.name}")
        
        # Overlay plot
        overlay_path = nta_plotter.plot_overlay_size_distributions(
            nta_stats_list=stats_list,
            save=True
        )
        if overlay_path:
            logger.info(f"  ✓ Overlay plot: {overlay_path.name}")
    
    logger.info(f"\n✅ NTA Visualization Demo Complete: {len(results)} samples processed")
    return results


def demo_anomaly_detection():
    """
    Deliverable 3: Anomaly detection for scatter plot shifts
    """
    logger.info("\n" + "=" * 80)
    logger.info("DELIVERABLE 3: Anomaly Detection for Scatter Plot Shifts")
    logger.info("=" * 80)
    
    # Initialize
    fcs_parser = FCSParser()
    detector = AnomalyDetector(output_dir=Path("figures/demo/anomalies"))
    
    # Find FCS files
    fcs_dir = Path("nanoFACS/10000 exo and cd81")
    if not fcs_dir.exists():
        logger.warning(f"FCS directory not found: {fcs_dir}")
        return None
    
    fcs_files = list(fcs_dir.glob("*.fcs"))
    
    if len(fcs_files) < 2:
        logger.warning("Need at least 2 FCS files for anomaly detection demo")
        return None
    
    logger.info(f"Found {len(fcs_files)} FCS files")
    
    try:
        # Use first file as baseline
        baseline_file = fcs_files[0]
        logger.info(f"\n📊 Setting baseline: {baseline_file.name}")
        
        baseline_data, baseline_meta = fcs_parser.parse_fcs_file(baseline_file)
        
        if baseline_data is None or len(baseline_data) == 0:
            logger.error("Failed to parse baseline file")
            return None
        
        logger.info(f"  ✓ Baseline: {len(baseline_data):,} events")
        
        # Set baseline for detector
        baseline_stats = detector.set_baseline(
            baseline_data=baseline_data,
            x_channel='FSC-A',
            y_channel='SSC-A'
        )
        
        logger.info(f"  ✓ Baseline statistics calculated")
        
        # Test remaining files for shifts
        results = []
        
        for test_file in fcs_files[1:4]:  # Test first 3 files
            logger.info(f"\n🔍 Testing: {test_file.name}")
            
            test_data, test_meta = fcs_parser.parse_fcs_file(test_file)
            
            if test_data is None or len(test_data) == 0:
                logger.warning(f"  Skipping {test_file.name}")
                continue
            
            logger.info(f"  ✓ Test data: {len(test_data):,} events")
            
            # Detect scatter plot shift
            shift_results = detector.detect_scatter_shift(
                test_data=test_data,
                threshold=2.0,
                save_plot=True
            )
            
            if shift_results:
                status = "🚨 ANOMALY" if shift_results['is_anomaly'] else "✅ Normal"
                logger.info(f"  {status}")
                logger.info(f"    Shift magnitude: {shift_results['shift_magnitude']:.2f}σ")
                logger.info(f"    X-shift: {shift_results['x_shift_mean']:.2f}σ")
                logger.info(f"    Y-shift: {shift_results['y_shift_mean']:.2f}σ")
                
                results.append({
                    'file': test_file.name,
                    'is_anomaly': shift_results['is_anomaly'],
                    'shift_magnitude': shift_results['shift_magnitude'],
                    'details': shift_results
                })
        
        # Detect outliers (Z-score method)
        logger.info(f"\n📊 Detecting outliers in baseline data...")
        
        outliers_df = detector.detect_outliers_zscore(
            data=baseline_data,
            channels=['FSC-A', 'SSC-A'],
            threshold=3.0
        )
        
        n_outliers = outliers_df['is_outlier'].sum()
        logger.info(f"  ✓ Found {n_outliers:,} outliers using Z-score method")
        
        # Detect outliers (IQR method)
        outliers_iqr_df = detector.detect_outliers_iqr(
            data=baseline_data,
            channels=['FSC-A', 'SSC-A'],
            factor=1.5
        )
        
        n_outliers_iqr = outliers_iqr_df['is_outlier_iqr'].sum()
        logger.info(f"  ✓ Found {n_outliers_iqr:,} outliers using IQR method")
        
        logger.info(f"\n✅ Anomaly Detection Demo Complete: {len(results)} samples analyzed")
        
        # Summary
        anomalies_detected = sum(1 for r in results if r['is_anomaly'])
        logger.info(f"\n📊 Summary:")
        logger.info(f"  - Baseline: {baseline_file.name}")
        logger.info(f"  - Samples tested: {len(results)}")
        logger.info(f"  - Anomalies detected: {anomalies_detected}")
        logger.info(f"  - Normal samples: {len(results) - anomalies_detected}")
        
        return results
        
    except Exception as e:
        logger.error(f"Error in anomaly detection demo: {e}")
        import traceback
        traceback.print_exc()
        return None


def main():
    """
    Run all three deliverable demonstrations.
    """
    logger.info("🚀 Starting Visualization Deliverables Demonstration")
    logger.info("=" * 80)
    logger.info("This demo will showcase:")
    logger.info("  1. FCS file parser + basic scatter plot generation")
    logger.info("  2. NTA text file parser + size distribution analysis")
    logger.info("  3. Anomaly detection for scatter plot shifts")
    logger.info("=" * 80)
    
    # Create output directories
    Path("figures/demo/fcs").mkdir(parents=True, exist_ok=True)
    Path("figures/demo/nta").mkdir(parents=True, exist_ok=True)
    Path("figures/demo/anomalies").mkdir(parents=True, exist_ok=True)
    
    # Run demonstrations
    fcs_results = demo_fcs_visualization()
    nta_results = demo_nta_visualization()
    anomaly_results = demo_anomaly_detection()
    
    # Final summary
    logger.info("\n" + "=" * 80)
    logger.info("🎉 ALL DELIVERABLES DEMONSTRATION COMPLETE")
    logger.info("=" * 80)
    
    if fcs_results:
        logger.info(f"✅ Deliverable 1: {len(fcs_results)} FCS samples visualized")
    else:
        logger.warning("⚠️ Deliverable 1: No FCS results")
    
    if nta_results:
        logger.info(f"✅ Deliverable 2: {len(nta_results)} NTA samples analyzed")
    else:
        logger.warning("⚠️ Deliverable 2: No NTA results")
    
    if anomaly_results:
        anomalies = sum(1 for r in anomaly_results if r['is_anomaly'])
        logger.info(f"✅ Deliverable 3: {len(anomaly_results)} samples tested, {anomalies} anomalies detected")
    else:
        logger.warning("⚠️ Deliverable 3: No anomaly results")
    
    logger.info("\n📁 All plots saved to: figures/demo/")
    logger.info("=" * 80)


if __name__ == '__main__':
    main()
