"""
B2g4
RepVGG(num_blocks=[4, 6, 16, 1], 
    width_multiplier=[2.5, 2.5, 2.5, 5], override_groups_map=g4_map)

"""
g4_map = {l: 4 for l in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26]}

model = dict(
    type='ImageClassifier',
    backbone=dict(type='RepVGG',num_blocks=[4, 6, 16, 1], width_multiplier=[2.5, 2.5, 2.5, 5],override_groups_map=g4_map),
    neck=None,
    head=dict(type='LinearClsHead',num_classes=10,in_channels=2560,loss=dict(type='CrossEntropyLoss', loss_weight=1.0),topk=(1, 5)
            ))


#cifar_bs_16
dataset_type = 'CIFAR10'
img_norm_cfg = dict(
    mean=[125.307, 122.961, 113.8575],
    std=[51.5865, 50.847, 51.255],
    to_rgb=False)
train_pipeline = [
    dict(type='RandomCrop', size=32, padding=4),
    dict(type='RandomFlip', flip_prob=0.5, direction='horizontal'),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='ToTensor', keys=['gt_label']),
    dict(type='Collect', keys=['img', 'gt_label'])
]
test_pipeline = [
    dict(type='Normalize', **img_norm_cfg),
    dict(type='ImageToTensor', keys=['img']),
    dict(type='Collect', keys=['img'])
]
data = dict(
    samples_per_gpu=16,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type, data_prefix='data/cifar10',
        pipeline=train_pipeline),
    val=dict(
        type=dataset_type,
        data_prefix='data/cifar10',
        pipeline=test_pipeline,
        test_mode=True),
    test=dict(
        type=dataset_type,
        data_prefix='data/cifar10',
        pipeline=test_pipeline,
        test_mode=True))

# optimizer
optimizer = dict(type='SGD', lr=0.1, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='step', step=[100, 150])
runner = dict(type='EpochBasedRunner', max_epochs=200)

# checkpoint saving
checkpoint_config = dict(interval=1)
# yapf:disable
log_config = dict(
    interval=100,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])
# yapf:enable

dist_params = dict(backend='nccl')
log_level = 'INFO'
load_from = None
resume_from = None
workflow = [('train', 1)]
