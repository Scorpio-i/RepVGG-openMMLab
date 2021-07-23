# RepVGG-openMMLab

>**This repository is the code that needs to be submitted for [OpenMMLab Algorithm Ecological Challenge](https://openmmlab.com/competitions/algorithm-2021)，the paper is [RepVGG: Making VGG-style ConvNets Great Again](http://openaccess.thecvf.com//content/CVPR2021/papers/Ding_RepVGG_Making_VGG-Style_ConvNets_Great_Again_CVPR_2021_paper.pdf)**


#### **Result :)**
1. *RepVGG-b2g4 top1 is 79.78*
2. *RepVGG-b3g4 top1 is 80.31*
3. *RepVGG-B3   top1 is 80.59*


#### **How TO Use?**

##### **What is MMCV?**
MMCV is a foundational library for computer vision research and supports many research projects as below:
* [MMClassification](https://github.com/open-mmlab/mmclassification):OpenMMLab image classification toolbox and benchmark.
* [MMDetection](https://github.com/open-mmlab/mmdetection):OpenMMLab detection toolbox and benchmark.
* [MMDetection3D](https://github.com/open-mmlab/mmdetection3d):OpenMMLab’s next-generation platform for general 3D object detection.
* [MMSegmentation](https://github.com/open-mmlab/mmsegmentation):OpenMMLab semantic segmentation toolbox and benchmark.
* [MMAction2](https://github.com/open-mmlab/mmaction2):OpenMMLab’s next-generation action understanding toolbox and benchmark.
* [MMTracking](https://github.com/open-mmlab/mmtracking):OpenMMLab video perception toolbox and benchmark.
* ...



##### **Using MMCV for the first time??**
1. **Install MMCV using MIM**
```
pip install git+https://github.com/open-mmlab/mim.git

mim install mmcv-full

```


2. **clone MMClassification and install**
```
git clone https://github.com/open-mmlab/mmclassification.git

cd mmclassification

pip install -e .
```



3. **Register RepVGG in MMclassification**

```
cp RepVGG-openMMLab/backbones/RepVGG.py \
mmclassification/mmcls/models/backbones/

in mmclassification/mmcls/models/backbones/__init__.py

...
from .RepVGG import RepVGG

__all__ = [
    ..., 'RepVGG'
]
```
4. **copy config file to mmclassification/config**
```

cp RepVGG-openMMLab/config/repvggb2g4_b32x8.py \
mmclassification/config/


```
5. **Train Model(If you downloaded Imagenet)**

```
cd mmclassification
python tools/train.py config/repvggb2g4_b32x8.py 

```
##### **Download && Unzip ImageNet**

```
data/download_imagenet.sh ，This script can automatically build the file structure that Imagenet needs for mmcls

mkdir -p mmclassification/data
cp RepVGG-openMMLab/data/download_imagenet.sh mmclassification/data
cd mmclassification/data
bash download_imagenet.sh

```


##### **Use the pre-trained model on Google Drive**
[pre-trained model](https://drive.google.com/drive/folders/1g6s_EM6NX2q7Nn3qZWW7MFj6nEDJpExT?usp=sharing)

* ***RepVGGB2g4.pth***

* ***RepVGGB3g4.pth***

* ***RepVGGB3.pth***


##### **Test Model**

```
in mmclassification

python tools/test.py config/repvggb2g4_b32x8.py ${repvggb2g4 model file} --meterics accuracy

someting like this..
```



##### **reference**
1. [RepVGG：极简架构，SOTA性能，让VGG式模型再次伟大（CVPR-2021)](https://zhuanlan.zhihu.com/p/344324470)
2. [RepVGG: Making VGG-style ConvNets Great Again (CVPR-2021) (PyTorch)](https://github.com/DingXiaoH/RepVGG#readme)
3. [MMClassification Docs](https://mmclassification.readthedocs.io/zh_CN/latest/install.html)
4. [ImageNet](https://image-net.org/)
5. [MMCV DOCs](https://mmcv.readthedocs.io/en/latest/get_started/introduction.html)

