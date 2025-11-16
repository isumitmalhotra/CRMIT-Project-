"""
Batch FCS Visualization Script - Integrated Pipeline
===================================================

Purpose: Generate visualizations for all FCS files in batch processing pipeline

Integration: Extends batch_process_fcs.py with visualization capabilities

Author: CRMIT Team
Date: November 15, 2025
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from loguru import logger
from tqdm import tqdm
import warnings
warnings.filterwarnings('ignore')

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.parsers.fcs_parser import FCSParser
from src.visualization.fcs_plots import FCSPlotter


def batch_visualize_fcs(
    input_dir: Path,
    output_dir: Path,
    stats_file: Path,
    plot_types: list = ['scatter', 'histogram'],
    max_files: int | None = None
):
    """
    Generate visualizations for all processed FCS files.
    
    Args:
        input_dir: Directory with FCS files
        output_dir: Directory for plots
        stats_file: Path to FCS statistics parquet file
        plot_types: List of plot types to generate
        max_files: Maximum files to process (None = all)
    """
    logger.info("=" * 80)
    logger.info("🎨 FCS BATCH VISUALIZATION PIPELINE")
    logger.info("=" * 80)
    
    # Initialize
    plotter = FCSPlotter(output_dir=output_dir)
    
    # Load statistics if available
    stats_df = None
    if stats_file.exists():
        stats_df = pd.read_parquet(stats_file)
        logger.info(f"📊 Loaded statistics: {len(stats_df)} samples")
    
    # Find FCS files
    fcs_files = list(input_dir.rglob("*.fcs"))
    
    if max_files:
        fcs_files = fcs_files[:max_files]
    
    logger.info(f"📁 Found {len(fcs_files)} FCS files")
    logger.info(f"📊 Plot types: {', '.join(plot_types)}")
    logger.info(f"💾 Output: {output_dir}")
    
    # Process each file
    success_count = 0
    error_count = 0
    plot_count = 0
    
    for fcs_file in tqdm(fcs_files, desc="Generating plots"):
        try:
            # Parse FCS file
            parser = FCSParser(file_path=fcs_file)
            data = parser.parse()
            
            if data is None or len(data) == 0:
                logger.warning(f"⚠️  No data: {fcs_file.name}")
                error_count += 1
                continue
            
            # Get metadata from stats if available
            sample_id = fcs_file.stem
            if stats_df is not None:
                sample_row = stats_df[stats_df['file_name'] == fcs_file.name]
                if len(sample_row) > 0:
                    sample_id = sample_row.iloc[0].get('sample_id', fcs_file.stem)
            
            # Generate scatter plots
            if 'scatter' in plot_types:
                # FSC-A vs SSC-A
                if 'FSC-A' in data.columns and 'SSC-A' in data.columns:
                    scatter_path = plotter.plot_scatter(
                        data=data,
                        x_channel='FSC-A',
                        y_channel='SSC-A',
                        title=f'Scatter Plot - {sample_id}',
                        sample_name=sample_id,
                        log_scale=True,
                        save_path=output_dir / f"{sample_id}_scatter_FSC_SSC.png"
                    )
                    if scatter_path:
                        plot_count += 1
                
                # FSC-H vs SSC-H if available
                if 'FSC-H' in data.columns and 'SSC-H' in data.columns:
                    plotter.plot_scatter(
                        data=data,
                        x_channel='FSC-H',
                        y_channel='SSC-H',
                        title=f'Scatter Plot (Height) - {sample_id}',
                        sample_name=sample_id,
                        log_scale=True,
                        save_path=output_dir / f"{sample_id}_scatter_FSC_SSC_height.png"
                    )
                    plot_count += 1
            
            # Generate histograms
            if 'histogram' in plot_types:
                for channel in ['FSC-A', 'SSC-A', 'FL1-A', 'FL2-A', 'FL3-A']:
                    if channel in data.columns:
                        plotter.plot_histogram(
                            data=data,
                            channel=channel,
                            title=f'{channel} Distribution - {sample_id}',
                            sample_name=sample_id,
                            bins=100,
                            log_scale=True,
                            save_path=output_dir / f"{sample_id}_hist_{channel}.png"
                        )
                        plot_count += 1
            
            success_count += 1
            
        except Exception as e:
            logger.error(f"❌ Error processing {fcs_file.name}: {e}")
            error_count += 1
    
    # Summary
    logger.info("\n" + "=" * 80)
    logger.info("📊 BATCH VISUALIZATION COMPLETE")
    logger.info("=" * 80)
    logger.info(f"✅ Successful: {success_count} files")
    logger.info(f"❌ Errors: {error_count} files")
    logger.info(f"📈 Total plots generated: {plot_count}")
    logger.info(f"💾 Plots saved to: {output_dir}")
    
    return success_count, error_count, plot_count


def main():
    """Main execution."""
    # Configuration
    INPUT_DIR = Path("nanoFACS/10000 exo and cd81")
    OUTPUT_DIR = Path("figures/fcs_batch")
    STATS_FILE = Path("data/processed/fcs_statistics.parquet")
    
    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    
    # Run batch visualization
    batch_visualize_fcs(
        input_dir=INPUT_DIR,
        output_dir=OUTPUT_DIR,
        stats_file=STATS_FILE,
        plot_types=['scatter'],  # Just scatter plots for speed
        max_files=None  # Process all files
    )


if __name__ == '__main__':
    main()
