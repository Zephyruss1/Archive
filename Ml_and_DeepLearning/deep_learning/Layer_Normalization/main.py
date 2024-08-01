from typing import Union, List
import torch
from torch import nn, Size

from labml_helpers.module import Module


class LayerNorm(Module):
    def __init__(self, normalized_shape: Union[int, list[int], Size], *,
                 eps: float = 1e-5, elementwise_affine: bool = True):
        super().__init__()

        if isinstance(normalized_shape, int):
            normalized_shape = torch.Size([normalized_shape])

        elif isinstance(normalized_shape, list):
            normalized_shape = torch.Size(normalized_shape)

        assert isinstance(normalized_shape, torch.Size)

        self.normalized_shape = normalized_shape
        self.eps = eps
        self.elementwise_affine = elementwise_affine

        if self.elementwise_affine:
            self.gain = nn.Parameter(torch.ones(normalized_shape))
            self.bias = nn.Parameter(torch.zeros(normalized_shape))

    def forward(self, x: torch.Tensor):
        assert self.normalized_shape == x.shape[-len(self.normalized_shape):]
        dims = [-(i + 1) for i in range(len(self.normalized_shape))]
        mean = x.mean(dim=dims, keepdim=True)
        mean_x2 = (x ** 2).mean(dim=dims, keepdim=True)
        var = mean_x2 - mean ** 2

        x_norm = (x - mean) / torch.sqrt(var + self.eps)

        if self.elementwise_affine:
            x_norm = self.gain * x_norm + self.bias

        return x_norm


def _test():
    from labml.logger import inspect

    x = torch.zeros([14, 32, 21, 48])
    inspect(x.shape)
    ln = LayerNorm(x.shape[2:])

    x = ln(x)
    inspect(x.shape)
    inspect(ln.gain.shape)


if __name__ == '__main__':
    _test()
