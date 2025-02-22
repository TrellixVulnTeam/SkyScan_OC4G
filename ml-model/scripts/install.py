"""Functions for installing external components."""

import os
import subprocess

# pylint: disable=W1510


def clone_tensorflow_repo():
    """Git clone tensorflow."""
    # deterministically download tensorflow v2.5.0
    # only download this large repo if it isn't already downloaded.
    if not os.path.isdir("/tf/models"):
        command = "git clone --depth 1 https://github.com/tensorflow/models/tree/v2.5.0 /tf/models"
        subprocess.run(command.split())


def setup_and_install_tensorflow_utilities():
    """Do file setup and installation to enable tensorflow.

    Compile tensorflow protocol buffer description files and install
    packages from tensorflow object detection module via a bash
    script.
    """
    # removed Shell=True to avoid security problems
    # https://stackoverflow.com/questions/3172470/actual-meaning-of-shell-true-in-subprocess/3172488#3172488
    subprocess.run("./install_tf_utils.sh")

clone_tensorflow_repo()
setup_and_install_tensorflow_utilities()