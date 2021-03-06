# MIT License

# Copyright (c) 2020 Constantin Pape

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages

setup(
    name="ai4ia",
    packages=['stardist_impl'],
    version="0.0.1",
    author="Constantin Pape, Christian Tischer",
    url="https://git.embl.de/grp-bio-it/ai4ia.git",
    license='MIT',
    entry_points={
        "console_scripts": [
            "train_stardist_2d = stardist_impl.train_stardist_2d:main",
            "predict_stardist_2d = stardist_impl.predict_stardist_2d:main",
            "train_stardist_3d = stardist_impl.train_stardist_3d:main",
            "predict_stardist_3d = stardist_impl.predict_stardist_3d:main",
            "stardist_model_to_fiji = stardist_impl.stardist_model_to_fiji:main"
        ]
    },
)
