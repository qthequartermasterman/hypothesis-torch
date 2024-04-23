"""Global test configuration."""

import hypothesis
import os

hypothesis.settings.register_profile("ci", max_examples=1000, deadline=None)
hypothesis.settings.register_profile("dev", max_examples=10)
hypothesis.settings.register_profile("debug", max_examples=10, verbosity=hypothesis.Verbosity.verbose)
hypothesis.settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "default"))
