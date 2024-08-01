from typing import Dict

import torch
from torch import nn

from labml_nn.optimizers import WeightDecay
from labml_nn.optimizers.adam import Adam


class AMSGrad(Adam):
    def __init__(self, params, lr=1e-3, betas=(0.9, 0.999), eps=1e-16,
                 weight_decay: WeightDecay=WeightDecay(),
                 optimized_update: bool=True,
                 amsgrad=True, defaults=None):

        defaults = {} if defaults is None else defaults
        defaults.update(dict(amsgrad=amsgrad))