"""Register a random.Random-compatible shim for `torch.random` with Hypothesis."""

from typing import Any, Callable

import hypothesis
import hypothesis.internal.entropy
import torch


class TorchRandomWrapper:
    """Shim for `torch.random` to match the random.Random interface.

    Hypothesis's random state manager requires a random.Random-compatible object.
    """

    seed: Callable[..., Any]
    getstate: Callable[[], Any]
    setstate: Callable[..., Any]

    def __init__(self) -> None:
        """Initialize the TorchRandomWrapper."""
        self.seed = torch.random.manual_seed
        self.getstate = torch.random.get_rng_state
        self.setstate = torch.random.set_rng_state


TORCH_RANDOM_WRAPPER = TorchRandomWrapper()


def _register_random_torch_state() -> None:
    """Register the random torch state with Hypothesis."""
    # Pyright is unhappy with the typing of WeakValueDictionary.values()
    # error: Operator "not in" not supported for types "TorchRandomWrapper" and "Iterator[RandomLike]"
    # (reportOperatorIssue)
    if TORCH_RANDOM_WRAPPER not in hypothesis.internal.entropy.RANDOMS_TO_MANAGE.values():  # type: ignore
        # For some reason pyright complains about this Protocol:
        # error: Argument of type "TorchRandomWrapper" cannot be assigned to parameter "r" of type "RandomLike" in
        # function "register_random"
        #     "TorchRandomWrapper" is incompatible with protocol "RandomLike"
        #       Could not bind method "<anonymous>" because it is missing a "self" or "cls" parameter
        #       (reportArgumentType)
        hypothesis.register_random(TORCH_RANDOM_WRAPPER)  # type: ignore
