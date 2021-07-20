import torch
from mmcls.models.classifiers import ImageClassifier


def test_repvgg():
    g4_map = {l: 4 for l in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]}
    model_cfg = dict(backbone=dict(
        type='RepVGG',
        num_classes=1000,
        num_blocks=[4, 6, 16, 1],
        width_multiplier=[2.5, 2.5, 2.5, 5],
        override_groups_map=g4_map,
    ),
                     neck=None,
                     head=dict(type='ClsHead',
                               loss=dict(type='CrossEntropyLoss')))
    img_classifier = ImageClassifier(**model_cfg)
    img_classifier.init_weights()
    imgs = torch.randn(16, 3, 32, 32)
    label = torch.randint(0, 10, (16, ))

    losses = img_classifier.forward_train(imgs, label)
    assert losses['loss'].item() > 0, "====> loss error "


if __name__ == '__main__':
    test_repvgg()
