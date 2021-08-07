# RepVGG-openMMLab

>**This repository is the code that needs to be submitted for [OpenMMLab Algorithm Ecological Challenge](https://openmmlab.com/competitions/algorithm-2021)，the paper is [RepVGG: Making VGG-style ConvNets Great Again](http://openaccess.thecvf.com//content/CVPR2021/papers/Ding_RepVGG_Making_VGG-Style_ConvNets_Great_Again_CVPR_2021_paper.pdf)**


## **Result**

- *RepVGG-b2g4 top1 is **79.78***
- *RepVGG-b3g4 top1 is **80.31***
- *RepVGG-B3   top1 is **80.31***


## **How TO Use?**

### **What is MMCV？**
MMCV is a foundational library for computer vision research and supports many research projects as below:
* [MMClassification](https://github.com/open-mmlab/mmclassification):OpenMMLab image classification toolbox and benchmark.
* [MMDetection](https://github.com/open-mmlab/mmdetection):OpenMMLab detection toolbox and benchmark.
* [MMDetection3D](https://github.com/open-mmlab/mmdetection3d):OpenMMLab’s next-generation platform for general 3D object detection.
* [MMSegmentation](https://github.com/open-mmlab/mmsegmentation):OpenMMLab semantic segmentation toolbox and benchmark.
* [MMAction2](https://github.com/open-mmlab/mmaction2):OpenMMLab’s next-generation action understanding toolbox and benchmark.
* [MMTracking](https://github.com/open-mmlab/mmtracking):OpenMMLab video perception toolbox and benchmark.
* ...



### **Using MMCV for the first time?**
If pytorch is not installed, can try conda :)
``` shell
# Create a conda virtual environment and activate it

conda create -n open-mmlab python=3.7 -y
conda activate open-mmlab

# If you have CUDA 10.1 installed under /usr/local/cuda and would like to install PyTorch 1.5, you need to install the prebuilt PyTorch with CUDA 10.1

conda install pytorch cudatoolkit=10.1 torchvision -c pytorch

```
**and install MMClassification repository now:** 

1. **Install MMCV using MIM**
``` shell
pip install git+https://github.com/open-mmlab/mim.git
mim install mmcv-full
```


2. **clone MMClassification and install**
``` shell 
git clone https://github.com/open-mmlab/mmclassification.git
cd mmclassification
pip install -e .
```



3. **Register RepVGG in MMclassification**

``` shell
cp RepVGG-openMMLab/backbones/RepVGG.py \
mmclassification/mmcls/models/backbones/
```
*in mmclassification/mmcls/models/backbones/__init__.py*
``` python
...
from .RepVGG import RepVGG

__all__ = [
    ..., 'RepVGG'
]
```
4. **copy config file to mmclassification/config**
``` shell
cp RepVGG-openMMLab/config/repvggb2g4_b32x8.py \
mmclassification/config/
```
5. **Train Model(If you downloaded Imagenet)**

``` shell
cd mmclassification

python tools/train.py config/repvggb2g4_b32x8.py
```
### **Download && Unzip ImageNet**
*It is recommended to symlink the dataset root to $MMCLASSIFICATION/data. If your folder structure is different, you may need to change the corresponding paths in config files*
``` shell
#data/download_imagenet.sh ，this script can automatically build the file structure that Imagenet needs for mmcls

mkdir -p mmclassification/data
cp RepVGG-openMMLab/data/download_imagenet.sh mmclassification/data
cd mmclassification/data
bash download_imagenet.sh

```


### **Pre-trained Model**
*pre-trained model in [Google Drive](https://drive.google.com/drive/folders/1g6s_EM6NX2q7Nn3qZWW7MFj6nEDJpExT?usp=sharing)*

* ***RepVGGB2g4.pth***

* ***RepVGGB3g4.pth***

* ***RepVGGB3.pth***


### **Test Model**

``` shell
in mmclassification

python tools/test.py config/repvggb2g4_b32x8.py ${CHECKPOINT} --metrics ${METRICS} --out ${RESULT}

something like this..
```



## **reference**
- [RepVGG：极简架构，SOTA性能，让VGG式模型再次伟大（CVPR-2021)](https://zhuanlan.zhihu.com/p/344324470)
- [RepVGG: Making VGG-style ConvNets Great Again (CVPR-2021) (PyTorch)](https://github.com/DingXiaoH/RepVGG#readme)
- [MMClassification Docs](https://mmclassification.readthedocs.io/zh_CN/latest/install.html)
- [MMCV Docs](https://mmcv.readthedocs.io/en/latest/get_started/introduction.html)
- [ImageNet](https://image-net.org/)



