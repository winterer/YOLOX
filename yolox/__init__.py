#!/usr/bin/env python3
# -*- coding:utf-8 -*-

__version__ = "0.3.0"

# Check if PyTorch is available
try:
    import torch
    import torchvision
except ImportError as e:
    missing_package = str(e).split("'")[1] if "'" in str(e) else "torch or torchvision"
    raise ImportError(
        f"\n{'='*70}\n"
        f"ERROR: {missing_package} is not installed!\n\n"
        f"YOLOX requires PyTorch and torchvision to be installed.\n"
        f"Please install them based on your system configuration:\n\n"
        f"  For CUDA 11.8:   pip install torch>=2.2.1 torchvision>=0.17.1\n"
        f"  For CUDA 12.1:   pip install torch>=2.2.1 torchvision>=0.17.1\n"
        f"  For CPU only:    pip install torch>=2.2.1 torchvision>=0.17.1 --index-url https://download.pytorch.org/whl/cpu\n\n"
        f"Visit https://pytorch.org/get-started/locally/ for more options.\n"
        f"{'='*70}\n"
    ) from e
