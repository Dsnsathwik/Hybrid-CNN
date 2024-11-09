import numpy as np

class Conv2d:
    def __init__(self, in_channels, out_channels, kernel_size, stride=1, padding=0):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride
        self.padding = padding

    def __call__(self, input):
        if self.padding != 0:
            input = np.pad(input, pad_width=((0, 0), (self.stride, self.stride), (self.stride, self.stride)), mode='constant', constant_values=0)

            
        







