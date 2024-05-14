"""Global test configuration."""

import datetime
import os

import hypothesis
from hypothesis import database

local = database.DirectoryBasedExampleDatabase(".hypothesis/examples")
shared = database.ReadOnlyDatabase(
    database.GitHubArtifactDatabase(
        "qthequartermaserman",
        "hypothesis-torch",
        cache_timeout=datetime.timedelta(days=7),
    )
)

hypothesis.settings.register_profile("ci", max_examples=100, database=local)
hypothesis.settings.register_profile("default", max_examples=100, database=database.MultiplexedDatabase(local, shared))
hypothesis.settings.register_profile("slow", max_examples=1000, database=database.MultiplexedDatabase(local, shared))
hypothesis.settings.register_profile("dev", max_examples=10, database=database.MultiplexedDatabase(local, shared))
hypothesis.settings.register_profile("fast", max_examples=3, database=database.MultiplexedDatabase(local, shared))
hypothesis.settings.register_profile(
    "debug",
    max_examples=10,
    verbosity=hypothesis.Verbosity.verbose,
    database=database.MultiplexedDatabase(local, shared),
)
hypothesis.settings.load_profile(os.getenv("HYPOTHESIS_PROFILE", "default"))
