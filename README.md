# RepVGG-openMMLab

#### 使用指南

##### Download && Unzip ImageNet

```
data/download_imagenet.sh 可以做到自动构建Imagenet数据集为
mmclas需要的结构

mkdir -p mmclassification/data
cp RepVGG-openMMLab/data/download_imagenet.sh mmclassification/data
cd mmclassification/data
bash download_imagenet.sh

```


##### 第一次使用mmcv？
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

##### **参考**
1. [RepVGG：极简架构，SOTA性能，让VGG式模型再次伟大（CVPR-2021)](https://zhuanlan.zhihu.com/p/344324470)
2. [RepVGG: Making VGG-style ConvNets Great Again (CVPR-2021) (PyTorch)](https://github.com/DingXiaoH/RepVGG#readme)
3. [MMClassification Docs](https://mmclassification.readthedocs.io/zh_CN/latest/install.html)
4. [ImageNet](https://image-net.org/)
