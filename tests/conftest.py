"""Global test configuration."""

import hypothesis
import os

hypothesis.settings.register_profile("ci", max_examples=100)
hypothesis.settings.register_profile("slow", max_examples=1000)
hypothesis.settings.register_profile("dev", max_examples=10)
hypothesis.settings.register_profile("fast", max_examples=3)
hypothesis.settings.register_profile("debug", max_examples=10, verbosity=hypothesis.Verbosity.verbose)
hypothesis.settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "default"))
