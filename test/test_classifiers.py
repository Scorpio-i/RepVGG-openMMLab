import torch
from mmcls.models.classifiers import ImageClassifier
from mmcls.models.backbones.RepVGG import RepVGG
g4_map = {l: 4 for l in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]}

def test_image_classifier_RepVGG():
        model = dict(
        type='ImageClassifier',
        backbone=dict(type='RepVGG',num_blocks=[4, 6, 16, 1], width_multiplier=[2.5, 2.5, 2.5, 5],override_groups_map=g4_map),
        neck=None,
        head=dict(type='LinearClsHead',num_classes=1000,in_channels=2560,loss=dict(
                type='LabelSmoothLoss', label_smooth_val=0.1, loss_weight=1.0),
                topk=(1, 5)),
        train_cfg=dict(
                augments=dict(type='BatchMixup', alpha=0.2, num_classes=1000,
                        prob=1.))
                )
        img_classifier = ImageClassifier(**model_cfg)
        img_classifier.init_weights()
        imgs = torch.randn(16, 3, 32, 32)
        label = torch.randint(0, 10, (16, ))
        losses = img_classifier.forward_train(imgs, label)
        assert losses['loss'].item()>0, "..."

        model_cfg['train_cfg'] = dict(mixup=dict(alpha=1.0, num_classes=10))
        img_classifier = ImageClassifier(**model_cfg)
        img_classifier.init_weights()
        imgs = torch.randn(16, 3, 32, 32)
        label = torch.randint(0, 10, (16, ))
        losses = img_classifier.forward_train(imgs, label)
        assert losses['loss'].item()>0,"..."