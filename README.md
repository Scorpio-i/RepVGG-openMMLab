# RepVGG-openMMLab

#### 使用指南
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
cp backbones/RepVGG.py \
mmclassification/mmcls/models/backbones/

在mmclassification/mmcls/models/backbones/__init__.py中添加新模块来注册RepVGG

...
from .RepVGG import RepVGG

__all__ = [
    ..., 'RepVGG'
]
```


#### **参考**
[RepVGG：极简架构，SOTA性能，让VGG式模型再次伟大（CVPR-2021)](https://zhuanlan.zhihu.com/p/344324470)
[RepVGG: Making VGG-style ConvNets Great Again (CVPR-2021) (PyTorch)](https://github.com/DingXiaoH/RepVGG#readme)
