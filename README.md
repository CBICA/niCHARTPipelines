# NiChart_DLMUSE

## Overview

NiChart_DLMUSE is a package that allows the users to process their brain imaging (sMRI) data easily and efficiently.

NiChart_DLMUSE offers easy ICV (Intra-Cranial Volume) mask extraction, and brain segmentation into ROIs. This is achieved through the [DLICV](https://github.com/CBICA/DLICV) and [DLMUSE](https://github.com/CBICA/DLMUSE) methods. Intermediate step results are saved for easy access to the user.

Given an input (sMRI) scan, NiChart_DLMUSE extracts the following:

1. ICV mask
2. Brain MUSE ROI segmentation
3. ROI volumes in a .csv format
4. Individual ROI mask (optionally).

This package uses [nnU-Net v2](https://github.com/MIC-DKFZ/nnUNet) as a basis model architecture for the deep learning parts, and various other [libraries](requirements.txt).


## Installation

### As a locally installed package

1. Create a new conda env

    ```bash
    conda create --name NCP python=3.12
    conda activate NCP
    ```

2. Clone and install NiChart_DLMUSE

    ```bash
    git clone  https://github.com/CBICA/NiChart_DLMUSE.git
    cd NiChart_DLMUSE
    pip install -e .
    ```

3. Run NiChart_DLMUSE. Example usage below

    ```bash
    NiChart_DLMUSE   -i                    /path/to/input     \
                     -o                    /path/to/output    \
                     -d                    cpu/cuda/mps
    ```

### (OUTDATED) Docker/Singularity/Apptainer-based build and installation 

The package comes already pre-built as a [docker container](https://hub.docker.com/repository/docker/aidinisg/nichart_dlmuse/general), for convenience. Please see [Usage](#usage) for more information on how to use it. Alternatively, you can build the docker image locally, like so:

```bash
docker -t NiChart_DLMUSE .
```

Singularity and Apptainer images can be built for NiChart_DLMUSE, allowing for frozen versions of the pipeline and easier installation for end-users.
Note that the Singularity project recently underwent a rename to "Apptainer", with a commercial fork still existing under the name "Singularity" (confusing!).
Please note that while for now these two versions are largely identical, future versions may diverge. It is recommended to use the AppTainer distribution. For now, these instructions apply to either.

First install [the container engine](https://apptainer.org/admin-docs/3.8/installation.html).
Then, from the cloned project repository, run:

```bash
singularity build nichart_dlmuse.sif singularity.def
```

This will take some time, but will build a containerized version of your current repo. Be aware that this includes any local changes!
The nichart_dlmuse.sif file can be distributed via direct download, or pushed to a container registry that accepts SIF images.

## Usage
Pre-trained nnUNet models for the skull-stripping can be found in [HuggingFace nichart/DLICV](https://huggingface.co/nichart/DLICV/tree/main) and segmentation tasks can be found in [HuggingFace nichart/DLMUSE](https://huggingface.co/nichart/DLMUSE/tree/main). Feel free to use it under the package's [license](LICENSE).

### As a locally installed package

A complete command would be (run from the directory of the package):

```bash

NiChart_DLMUSE -i                    /path/to/input     \
               -o                    /path/to/output    \
               -d                    cpu/cuda/mps
```

For further explanation please refer to the complete documentation:

```bash
NiChart_DLMUSE -h
```

### (OUTDATED) Using the docker container

Using the file structure explained above, an example command using the [docker container](https://hub.docker.com/repository/docker/aidinisg/nichart_dlmuse/general) is the following:

```bash
docker run -it --rm --gpus all -v ./:/workspace/ aidinisg/nichart_dlmuse:0.1.7 NiChart_DLMUSE -i temp/nnUNet_raw_database/nnUNet_raw_data/ -o temp/nnUNet_out/ -p structural --derived_ROI_mappings_file /NiChart_DLMUSE/shared/dicts/MUSE_mapping_derived_rois.csv --MUSE_ROI_mappings_file /NiChart_DLMUSE/shared/dicts/MUSE_mapping_consecutive_indices.csv --model_folder temp/nnUNet_model/ --nnUNet_raw_data_base temp/nnUNet_raw_database/ --nnUNet_preprocessed  temp/nnUNet_preprocessed/ --all_in_gpu True --mode fastest --disable_tta
```

### (OUTDATED) Using the singularity container

```bash
singularity run --nv --containall --bind /path/to/.\:/workspace/ nichart_dlmuse.simg NiChart_DLMUSE -i /workspace/temp/nnUNet_raw_data_base/nnUNet_raw_data/ -o /workspace/temp/nnUNet_out -p structural --derived_ROI_mappings_file /NiChart_DLMUSE/shared/dicts/MUSE_mapping_derived_rois.csv --MUSE_ROI_mappings_file /NiChart_DLMUSE/shared/dicts/MUSE_mapping_consecutive_indices.csv --nnUNet_raw_data_base /workspace/temp/nnUNet_raw_data_base/ --nnUNet_preprocessed /workspace/temp/nnUNet_preprocessed/ --model_folder /workspace/temp/nnUNet_model/ --all_in_gpu True --mode fastest --disable_tta
```
