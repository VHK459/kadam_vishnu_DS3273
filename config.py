import torch.nn as nn


batchsize = 32
epochs = 20
resize_x, resize_y = 64, 64
input_channels = 3
num_classes = 58
learning_rate = 0.001

loss_fn = nn.CrossEntropyLoss()