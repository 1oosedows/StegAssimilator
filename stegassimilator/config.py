"""Configuration settings for StegAssimilator."""

from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class AnalyzerConfig:
    """Configuration for the steganography analyzer."""
    
    # Detection thresholds
    thresholds: Dict[str, float] = None
    
    # Analysis parameters
    dct_block_size: int = 8
    edge_detection_threshold: float = 100
    lsb_analysis_depth: int = 1
    texture_analysis_window: int = 3
    frequency_analysis_bands: int = 4
    
    # Performance settings
    max_image_size: int = 4096
    batch_size: int = 10
    num_workers: int = 4
    
    # Output settings
    output_dir: str = "analysis_results"
    verbose: bool = False
    save_visualizations: bool = True
    save_reports: bool = True
    
    def __post_init__(self):
        """Initialize default thresholds if not provided."""
        if self.thresholds is None:
            self.thresholds = {
                "general": 0.8,
                "color_anomaly": 0.7,
                "dct_anomaly": 0.75,
                "edge_anomaly": 0.65,
                "lsb_anomaly": 0.7,
                "palette_anomaly": 0.6,
                "texture_anomaly": 0.7,
                "frequency_anomaly": 0.75
            }

@dataclass
class VisualizerConfig:
    """Configuration for visualization components."""
    
    # Output settings
    output_dir: str = "visualization_output"
    dpi: int = 300
    figure_size: tuple = (12, 8)
    
    # Visualization parameters
    histogram_bins: int = 256
    edge_detection_threshold: float = 100
    frequency_analysis_scale: str = "log"
    texture_analysis_cmap: str = "viridis"
    
    # Style settings
    style: str = "seaborn"
    color_palette: str = "deep"
    font_size: int = 10

@dataclass
class DeobfuscatorConfig:
    """Configuration for deobfuscation techniques."""
    
    # Adaptive thresholding
    adaptive_block_size: int = 11
    adaptive_c: float = 2
    
    # High-pass filtering
    high_pass_kernel_size: int = 3
    high_pass_sigma: float = 1.5
    
    # Denoising
    denoise_strength: float = 10
    denoise_patch_size: int = 7
    
    # Unsharp masking
    unsharp_amount: float = 1.5
    unsharp_radius: float = 1.0
    unsharp_threshold: float = 0
    
    # Histogram equalization
    hist_clip_limit: float = 2.0
    hist_tile_grid_size: tuple = (8, 8)
    
    # Laplacian pyramid
    pyramid_levels: int = 3
    pyramid_sigma: float = 2.0
    
    # Frequency domain
    freq_scale: str = "log"
    freq_bands: int = 4

@dataclass
class LoggingConfig:
    """Configuration for logging."""
    
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    file: Optional[str] = "steg_analysis.log"
    max_size: int = 10485760  # 10MB
    backup_count: int = 5

@dataclass
class Config:
    """Main configuration class."""
    
    analyzer: AnalyzerConfig = AnalyzerConfig()
    visualizer: VisualizerConfig = VisualizerConfig()
    deobfuscator: DeobfuscatorConfig = DeobfuscatorConfig()
    logging: LoggingConfig = LoggingConfig()
    
    # Global settings
    supported_formats: List[str] = None
    temp_dir: str = "temp"
    cache_dir: str = "cache"
    
    def __post_init__(self):
        """Initialize default supported formats if not provided."""
        if self.supported_formats is None:
            self.supported_formats = [
                ".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"
            ]

# Default configuration
DEFAULT_CONFIG = Config() 