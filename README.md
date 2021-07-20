# RepVGG-openMMLab

#### 使用指南
##### 第一次使用mmcv？
1. **使用mim来安装mmcls**
```
pip install git+https://github.com/open-mmlab/mim.git

mim install mmcls

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


TODO
一些参考
一些使用方法