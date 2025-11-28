#!/usr/bin/env python
# Copyright (c) Megvii, Inc. and its affiliates. All Rights Reserved

import sys

from setuptools import setup
from torch.utils import cpp_extension


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
