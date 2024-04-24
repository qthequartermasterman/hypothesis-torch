"""Register a random.Random-compatible shim for `torch.random` with Hypothesis."""

import hypothesis
import torch


class TorchRandomWrapper:
    """Shim for `torch.random` to match the random.Random interface.

    Hypothesis's random state manager requires a random.Random-compatible object.
    """

    def __init__(self) -> None:
        """Initialize the TorchRandomWrapper."""
        self.seed = torch.random.manual_seed
        self.getstate = torch.random.get_rng_state
        self.setstate = torch.random.set_rng_state


TORCH_RANDOM_WRAPPER = TorchRandomWrapper()

hypothesis.register_random(TORCH_RANDOM_WRAPPER)
