NiChart_DLMUSE
==============

.. image:: https://codecov.io/gh/CBICA/NiChart_DLMUSE/graph/badge.svg?token=i5Vyjayoct
   :target: https://codecov.io/gh/CBICA/NiChart_DLMUSE
   :alt: Code Coverage

.. image:: https://github.com/CBICA/NiChart_DLMUSE/actions/workflows/macos_build.yml/badge.svg
   :target: https://github.com/CBICA/NiChart_DLMUSE/actions/workflows/macos_build.yml
   :alt: macOS Build

.. image:: https://github.com/CBICA/NiChart_DLMUSE/actions/workflows/ubuntu_build.yml/badge.svg
   :target: https://github.com/CBICA/NiChart_DLMUSE/actions/workflows/ubuntu_build.yml
   :alt: Ubuntu Build

.. image:: https://img.shields.io/pypi/v/NiChart_DLMUSE
   :target: https://pypi.org/project/NiChart_DLMUSE/
   :alt: PyPI Stable

Overview
--------

**NiChart_DLMUSE** is a package that allows the users to process their brain imaging (sMRI) data easily and efficiently.

NiChart_DLMUSE offers easy ICV (Intra-Cranial Volume) mask extraction, and brain segmentation into ROIs. This is achieved through the `DLICV <https://github.com/CBICA/DLICV>`_ and `DLMUSE <https://github.com/CBICA/DLMUSE>`_ methods. Intermediate step results are saved for easy access to the user.

Given an input (sMRI) scan, NiChart_DLMUSE extracts the following:

  1. ICV mask
  2. Brain MUSE ROI segmentation
  3. ROI volumes in a .csv format
  4. Individual ROI mask (optionally).

This package uses `nnU-Net v2 <https://github.com/MIC-DKFZ/nnUNet>`_ as a basis model architecture for the deep learning parts, and various other `libraries <requirements.txt>`_.

Installation
------------

******************************
As a locally installed package
******************************

You can install NiChart DLMUSE from source: ::

    $ git clone https://github.com/CBICA/NiChart_DLMUSE.git
      cd NiChart_DLMUSE
      python3 -m pip install -e .

Or from out latest stable PyPI wheel: ::

    $ pip install NiChart_DLMUSE

(If needed for your system) Install PyTorch with compatible CUDA.
You only need to run this step if you experience errors with CUDA while running NiChart_DLMUSE.
Run "pip uninstall torch torchaudio torchvision".
Then follow the `PyTorch installation instructions <https://pytorch.org/get-started/locally/>`_ for your CUDA version. 
Specific versions are needed for full compatibility. On Linux, download Torch 2.3.1, on Windows install 2.5.1. For example, after installing NiChart_DLMUSE: ::

   $ pip uninstall torch torchvision torchaudio
     pip install torch==2.3.1 --index-url https://download.pytorch.org/whl/cu121

******************
Run NiChart_DLMUSE
******************

Example usage below: ::

    $ NiChart_DLMUSE   -i                    /path/to/input     \
                       -o                    /path/to/output    \
                       -d                    cpu/cuda/mps

Docker/Singularity/Apptainer-based build and installation
---------------------------------------------------------

************
Docker build
************

The package comes already pre-built as a `docker container <https://hub.docker.com/repository/docker/cbica/nichart_dlmuse/general>`_, for convenience. Please see `Usage <#usage>`_ for more information on how to use it. Alternatively, you can build the docker image
locally from the source repo, like so: ::

  $ docker build -t cbica/nichart_dlmuse .

**************************************
(OUTDATED) Singularity/Apptainer build
**************************************

Singularity and Apptainer images can be built for NiChart_DLMUSE, allowing for frozen versions of the pipeline and easier installation for end-users.
Note that the Singularity project recently underwent a rename to "Apptainer", with a commercial fork still existing under the name "Singularity" (confusing!).
Please note that while for now these two versions are largely identical, future versions may diverge. It is recommended to use the AppTainer distribution. For now, these instructions apply to either.

First install `the container engine <https://apptainer.org/admin-docs/3.8/installation.html>`_.
Then, from the cloned project repository, run: ::

  $ singularity build nichart_dlmuse.sif singularity.def

This will take some time, but will build a containerized version of your current repo. Be aware that this includes any local changes!
The nichart_dlmuse.sif file can be distributed via direct download, or pushed to a container registry that accepts SIF images.

*****
Usage
*****

Pre-trained nnUNet models for the skull-stripping can be found in `HuggingFace nichart/DLICV <https://huggingface.co/nichart/DLICV/tree/main>`_ and segmentation tasks
can be found in `HuggingFace nichart/DLMUSE <https://huggingface.co/nichart/DLMUSE/tree/main>`_. Feel free to use it under the package's `license <LICENSE>`_.

******************************
As a locally installed package
******************************

A complete command would be (run from the directory of the package): ::

  $ NiChart_DLMUSE -i                    /path/to/input     \
                   -o                    /path/to/output    \
                   -d                    cpu/cuda/mps

For further explanation please refer to the complete documentation: ::

    $ NiChart_DLMUSE -h

Troubleshooting model download failures
---------------------------------------

Our model download process creates several deep directory structures. If you are running on Windows and your model download process fails, it may be due to Windows file path limitations.

To enable long path support in Windows 10, version 1607, and later, the registry key `HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\FileSystem LongPathsEnabled (Type: REG_DWORD)` must exist and be set to 1.

If this affects you, we recommend re-running NiChart_DLMUSE with the `--clear_cache` flag set on the first run.

Using the docker container
--------------------------

Using the file structure explained above, an example command using the `docker container <https://hub.docker.com/repository/docker/cbica/nichart_dlmuse/general>`_ is the following: ::

  # Pull the image for your CUDA version (as needed)
  $ CUDA_VERSION=11.8 docker pull cbica/nichart_dlmuse:1.0.1-cuda${CUDA_VERSION}
  # or, for CPU:
  $ docker pull cbica/nichart_dlmuse:1.0.1

  # Run the container with proper mounts, GPU enabled
  # Place input in /path/to/input/on/host.
  # Replace "-d cuda" with "-d mps" or "-d cpu" as needed...
  # or don't pass at all to automatically use CPU.
  # Each "/path/to/.../on/host" is a placeholder, use your actual paths!
  $ docker run -it --name DLMUSE_inference --rm
      --mount type=bind,source=/path/to/input/on/host,target=/input,readonly
      --mount type=bind,source=/path/to/output/on/host,target=/output
      --gpus all cbica/nichart_dlmuse -d cuda


(OUTDATED) singularity container
------------------------------------------

To use the singularity container, you can just do: ::

    $ singularity run --nv --containall --bind /path/to/.\:/workspace/ nichart_dlmuse.simg NiChart_DLMUSE -i /workspace/temp/nnUNet_raw_data_base/nnUNet_raw_data/ -o /workspace/temp/nnUNet_out -p structural --derived_ROI_mappings_file /NiChart_DLMUSE/shared/dicts/MUSE_mapping_derived_rois.csv --MUSE_ROI_mappings_file /NiChart_DLMUSE/shared/dicts/MUSE_mapping_consecutive_indices.csv --nnUNet_raw_data_base /workspace/temp/nnUNet_raw_data_base/ --nnUNet_preprocessed /workspace/temp/nnUNet_preprocessed/ --model_folder /workspace/temp/nnUNet_model/ --all_in_gpu True --mode fastest --disable_tta
