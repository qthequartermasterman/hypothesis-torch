"""Test that loading the package does not initialize cuda.

This is required for test suites that involve lots of forking processes. CUDA can not be initialized in a parent
process and then forked.

In particular, this is necessary so that the vLLM Unit tests introduced in
https://github.com/vllm-project/vllm/pull/22962 break the rest of the test suite by prematurely initializing CUDA in a
parent process that is later forked.
"""
import multiprocessing as mp


def check_import() -> None:
    """Import torch, and make sure that torch.cuda is uninitialized after hypothesis_torch is imported."""
    import torch

    # Test is invalid if cuda is already initialized.
    assert not torch.cuda.is_initialized()
    import hypothesis_torch

    assert not torch.cuda.is_initialized()


def test_loading_package_does_not_initialize_cuda() -> None:
    """Test that loading the package does not initialize cuda.

    This is required for test suites that involve lots of forking processes. CUDA can not be initialized in a parent
    process and then forked.
    """
    ctx = mp.get_context("spawn")
    p = ctx.Process(target=check_import)
    p.start()
    p.join()
    assert p.exitcode == 0
