#!/usr/bin/env python
# Copyright (c) Megvii, Inc. and its affiliates. All Rights Reserved

import sys

from setuptools import setup

try:
    from torch.utils import cpp_extension
except ImportError:
    print(
        "\n" + "="*70 + "\n"
        "ERROR: PyTorch is not installed!\n\n"
        "YOLOX requires PyTorch to be installed before building.\n"
        "Please install PyTorch first based on your system configuration:\n\n"
        "  For CUDA 11.8:   pip install torch>=2.2.1 torchvision>=0.17.1\n"
        "  For CUDA 12.1:   pip install torch>=2.2.1 torchvision>=0.17.1\n"
        "  For CPU only:    pip install torch>=2.2.1 torchvision>=0.17.1 --index-url https://download.pytorch.org/whl/cpu\n\n"
        "Visit https://pytorch.org/get-started/locally/ for more options.\n"
        "="*70 + "\n"
    )
    sys.exit(1)


def get_ext_modules():
    ext_module = []
    if sys.platform != "win32":  # pre-compile ops on linux
        # if any other op is added, please also add it here
        try:
            from yolox.layers import FastCOCOEvalOp
            ext_module.append(FastCOCOEvalOp().build_op())
        except ImportError:
            # Package not yet installed, skip extension modules for now
            # print warning message
            print("[Warning] Failed to import yolox.layers.FastCOCOEvalOp. Skipping extension module build.")
            pass
    return ext_module


def get_cmd_class():
    return {"build_ext": cpp_extension.BuildExtension}


if __name__ == "__main__":
    # Alle Metadaten, Dependencies, Packages etc. kommen aus pyproject.toml.
    setup(
        ext_modules=get_ext_modules(),
        cmdclass=get_cmd_class(),
    )
