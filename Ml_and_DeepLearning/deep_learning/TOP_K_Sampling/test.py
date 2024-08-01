import torch
from labml_nn.sampling import Sampler
from main import TopKSampler


class DummySampler(Sampler):
    def __call__(self, logits: torch.Tensor):
        return torch.argmax(logits, dim=-1)


def test_topk_sampler():
    dummy_sampler = DummySampler()
    k = 3
    topk_sampler = TopKSampler(k, dummy_sampler)

    logits = torch.tensor([[12.0, 33.0, 42.0, 47.0, 20.5],
                           [0.2, 2.5, 1.5, 0.1, 3.0]])

    samples = topk_sampler(logits)

    print("Logits:\n", logits)
    print("Samples:\n", samples)


test_topk_sampler()
