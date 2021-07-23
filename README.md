# RepVGG-openMMLab

>**这个Repo是[OpenMMLab算法生态挑战赛](https://openmmlab.com/competitions/algorithm-2021)所需提交的代码库,本次复现的文献是[RepVGG: Making VGG-style ConvNets Great Again](https://zhuanlan.zhihu.com/p/344324470)**

#### 使用指南

##### **MMCV是什么？**
MMCV is a foundational library for computer vision research and supports many research projects as below:
* [MMClassification](https://github.com/open-mmlab/mmclassification):OpenMMLab image classification toolbox and benchmark.
* [MMDetection](https://github.com/open-mmlab/mmdetection):OpenMMLab detection toolbox and benchmark.
* [MMDetection3D](https://github.com/open-mmlab/mmdetection3d):OpenMMLab’s next-generation platform for general 3D object detection.
* [MMSegmentation](https://github.com/open-mmlab/mmsegmentation):OpenMMLab semantic segmentation toolbox and benchmark.
* [MMAction2](https://github.com/open-mmlab/mmaction2):OpenMMLab’s next-generation action understanding toolbox and benchmark.
* [MMTracking](https://github.com/open-mmlab/mmtracking):OpenMMLab video perception toolbox and benchmark.
* ...



##### **第一次使用mmcv?**
1. **使用mim来安装mmcv-full**
```
pip install git+https://github.com/open-mmlab/mim.git

mim install mmcv-full

```


2. **clone MMClassification 并以dev安装**
```
git clone https://github.com/open-mmlab/mmclassification.git

cd mmclassification

pip install -e .
```



3. **到MMclassification注册RepVGG**

```
cp RepVGG-openMMLab/backbones/RepVGG.py \
mmclassification/mmcls/models/backbones/

在mmclassification/mmcls/models/backbones/__init__.py中添加新模块来注册RepVGG

...
from .RepVGG import RepVGG

__all__ = [
    ..., 'RepVGG'
]
```
4. **copy config files to mmclassification/config**
```

cp RepVGG-openMMLab/config/repvggb2g4_b32x8.py \
mmclassification/config/


```
5. **Train Model(如果下载了ImageNet)**

```
cd mmclassification
python tools/train.py config/repvggb2g4_b32x8.py 

```
##### **Download && Unzip ImageNet**

```
data/download_imagenet.sh 可以做到自动构建Imagenet数据集为
mmclas需要的结构

mkdir -p mmclassification/data
cp RepVGG-openMMLab/data/download_imagenet.sh mmclassification/data
cd mmclassification/data
bash download_imagenet.sh

```


##### **使用Google云端硬盘上的预训练模型**
[预训练模型](https://drive.google.com/drive/folders/1g6s_EM6NX2q7Nn3qZWW7MFj6nEDJpExT?usp=sharing)

* ***RepVGGB2g4.pth***

* ***RepVGGB3g4.pth***

* ***RepVGGB3.pth***


##### **测试模型**

```
in mmclassification

python tools/test.py config/repvggb2g4_b32x8.py ${repvggb2g4 model file} --meterics accuracy

someting like this..
```



##### **参考**
1. [RepVGG：极简架构，SOTA性能，让VGG式模型再次伟大（CVPR-2021)](https://zhuanlan.zhihu.com/p/344324470)
2. [RepVGG: Making VGG-style ConvNets Great Again (CVPR-2021) (PyTorch)](https://github.com/DingXiaoH/RepVGG#readme)
3. [MMClassification Docs](https://mmclassification.readthedocs.io/zh_CN/latest/install.html)
4. [ImageNet](https://image-net.org/)
5. [MMCV DOCs](https://mmcv.readthedocs.io/en/latest/get_started/introduction.html)


