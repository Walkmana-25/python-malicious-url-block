#!/bin/bash
python setup.py bdist_wheel -p manylinux_2_28_x86_64

python setup.py bdist_wheel -p manylinux_2_28_aarch64
python setup.py bdist_wheel -p manylinux_2_28_ppc64le
python setup.py bdist_wheel -p manylinux_2_28_s390x