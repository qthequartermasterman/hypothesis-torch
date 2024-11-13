# CHANGELOG


## v0.8.4 (2024-11-13)

### Build System

- **deps**: Bump the lint-and-dev group with 4 updates
  ([`0200d68`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0200d68acd96ac548d8fd6bf3e90d3982e610897))

Bumps the lint-and-dev group with 4 updates: [ruff](https://github.com/astral-sh/ruff),
  [pyright](https://github.com/RobertCraigie/pyright-python),
  [mkdocstrings[python]](https://github.com/mkdocstrings/mkdocstrings) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Updates `ruff` from 0.7.2 to 0.7.3 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.7.2...0.7.3)

Updates `pyright` from 1.1.387 to 1.1.388 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.387...v1.1.388)

Updates `mkdocstrings[python]` from 0.26.2 to 0.27.0 - [Release
  notes](https://github.com/mkdocstrings/mkdocstrings/releases) -
  [Changelog](https://github.com/mkdocstrings/mkdocstrings/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/mkdocstrings/mkdocstrings/compare/0.26.2...0.27.0)

Updates `mkdocs-material` from 9.5.43 to 9.5.44 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.43...9.5.44)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pyright
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev - dependency-name: mkdocstrings[python] dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: lint-and-dev - dependency-name:
  mkdocs-material dependency-type: direct:production update-type: version-update:semver-patch
  dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump torch in the direct-dependencies group
  ([`35e700c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/35e700cd0572f33759ce1d7d09079f34bec58e12))

Bumps the direct-dependencies group with 1 update: [torch](https://github.com/pytorch/pytorch).

Updates `torch` from 2.1.2+cpu to 2.5.1 - [Release
  notes](https://github.com/pytorch/pytorch/releases) -
  [Changelog](https://github.com/pytorch/pytorch/blob/main/RELEASE.md) -
  [Commits](https://github.com/pytorch/pytorch/commits/v2.5.1)

--- updated-dependencies: - dependency-name: torch dependency-type: direct:production update-type:
  version-update:semver-minor dependency-group: direct-dependencies ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Update transformers requirement
  ([`0588258`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0588258d778e9a6f334d917d3dad229231bbb509))

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit
  the latest version.

Updates `transformers` to 4.46.2 - [Release
  notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.42.3...v4.46.2)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production
  dependency-group: optional-dependencies ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.8.3 (2024-11-04)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 2 updates
  ([`f8a27a6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f8a27a6c03247558f9108b37cf4b96d42eb20dfe))

Bumps the lint-and-dev group with 2 updates in the / directory:
  [ruff](https://github.com/astral-sh/ruff) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Updates `ruff` from 0.7.1 to 0.7.2 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.7.1...0.7.2)

Updates `mkdocs-material` from 9.5.42 to 9.5.43 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.42...9.5.43)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: mkdocs-material
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.8.2 (2024-10-31)

### Build System

- **deps**: Update transformers requirement
  ([`eb5499f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/eb5499f923abca8056e37814e754acc85cef4d7d))

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit
  the latest version.

Updates `transformers` to 4.46.1 - [Release
  notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.42.3...v4.46.1)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production
  dependency-group: optional-dependencies ...

Signed-off-by: dependabot[bot] <support@github.com>

### Continuous Integration

- Allow using any available pypi index in ci
  ([`4629597`](https://github.com/qthequartermasterman/hypothesis-torch/commit/46295972e35f2ceb419d29b7ea6d98e332a0e2df))

- Pin numpy versions for old torch versions
  ([`61e6db6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/61e6db6a0f21268370f2cc3a9763fc27ae65850f))

- Install torch after the rest of the dependencies in CI to force correct version of numpy
  ([`fbc2ef0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fbc2ef0695e9acad7c0fa98d4fe5222d13800167))


## v0.8.1 (2024-10-31)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 5 updates
  ([`c9c0f57`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c9c0f57cc66e33de2eaf70926473c2b8cf2b2259))

Bumps the lint-and-dev group with 5 updates in the / directory:

| Package | From | To | | --- | --- | --- | | [mypy](https://github.com/python/mypy) | `1.12.0` |
  `1.13.0` | | [ruff](https://github.com/astral-sh/ruff) | `0.6.9` | `0.7.1` | |
  [pyright](https://github.com/RobertCraigie/pyright-python) | `1.1.384` | `1.1.387` | |
  [pytest-cov](https://github.com/pytest-dev/pytest-cov) | `5.0.0` | `6.0.0` | |
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material) | `9.5.40` | `9.5.42` |

Updates `mypy` from 1.12.0 to 1.13.0 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.12.0...v1.13.0)

Updates `ruff` from 0.6.9 to 0.7.1 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.9...0.7.1)

Updates `pyright` from 1.1.384 to 1.1.387 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.384...v1.1.387)

Updates `pytest-cov` from 5.0.0 to 6.0.0 -
  [Changelog](https://github.com/pytest-dev/pytest-cov/blob/master/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest-cov/compare/v5.0.0...v6.0.0)

Updates `mkdocs-material` from 9.5.40 to 9.5.42 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.40...9.5.42)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:production update-type:
  version-update:semver-minor dependency-group: lint-and-dev - dependency-name: ruff
  dependency-type: direct:production update-type: version-update:semver-minor dependency-group:
  lint-and-dev - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pytest-cov
  dependency-type: direct:production update-type: version-update:semver-major dependency-group:
  lint-and-dev - dependency-name: mkdocs-material dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.8.0 (2024-10-31)

### Bug Fixes

- Add support for 'd'
  ([`339456b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/339456bb113cfd22e3a1f27911582d334e499549))

- Add support for 'd' and 'eps' for Adafactor
  ([`d5c3d9a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d5c3d9a2cf6e99d07bef9343cac0696707051c5d))

### Features

- Support pytorch 2.5
  ([`7ce1d64`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7ce1d6420dabd81c30da00fce0e344dac04e6984))


## v0.7.19 (2024-10-14)

### Build System

- **deps**: Bump the lint-and-dev group with 4 updates
  ([`1600e62`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1600e6260d8e963f131a02c5a0de6c76b3c797d6))

Bumps the lint-and-dev group with 4 updates: [mypy](https://github.com/python/mypy),
  [pyright](https://github.com/RobertCraigie/pyright-python),
  [mkdocstrings[python]](https://github.com/mkdocstrings/mkdocstrings) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Updates `mypy` from 1.11.2 to 1.12.0 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.11.2...v1.12.0)

Updates `pyright` from 1.1.383 to 1.1.384 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.383...v1.1.384)

Updates `mkdocstrings[python]` from 0.26.1 to 0.26.2 - [Release
  notes](https://github.com/mkdocstrings/mkdocstrings/releases) -
  [Changelog](https://github.com/mkdocstrings/mkdocstrings/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/mkdocstrings/mkdocstrings/compare/0.26.1...0.26.2)

Updates `mkdocs-material` from 9.5.39 to 9.5.40 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.39...9.5.40)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:production update-type:
  version-update:semver-minor dependency-group: lint-and-dev - dependency-name: pyright
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev - dependency-name: mkdocstrings[python] dependency-type: direct:production
  update-type: version-update:semver-patch dependency-group: lint-and-dev - dependency-name:
  mkdocs-material dependency-type: direct:production update-type: version-update:semver-patch
  dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.18 (2024-10-07)

### Build System

- **deps**: Bump the lint-and-dev group with 2 updates
  ([`47d2f5f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/47d2f5f90fa14ea6b15b1952ec18d210015e0bc6))

Bumps the lint-and-dev group with 2 updates: [ruff](https://github.com/astral-sh/ruff) and
  [pyright](https://github.com/RobertCraigie/pyright-python).

Updates `ruff` from 0.6.8 to 0.6.9 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.8...0.6.9)

Updates `pyright` from 1.1.382.post1 to 1.1.383 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.382.post1...v1.1.383)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pyright
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.17 (2024-09-30)

### Build System

- **deps**: Bump the lint-and-dev group with 3 updates
  ([`af776ac`](https://github.com/qthequartermasterman/hypothesis-torch/commit/af776ac38f0e2749faeeae4e7c96936d27752a80))

Bumps the lint-and-dev group with 3 updates: [ruff](https://github.com/astral-sh/ruff),
  [pyright](https://github.com/RobertCraigie/pyright-python) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Updates `ruff` from 0.6.7 to 0.6.8 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.7...0.6.8)

Updates `pyright` from 1.1.381 to 1.1.382.post1 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.381...v1.1.382.post1)

Updates `mkdocs-material` from 9.5.36 to 9.5.39 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.36...9.5.39)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pyright
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev - dependency-name: mkdocs-material dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.16 (2024-09-23)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 4 updates
  ([`38241ed`](https://github.com/qthequartermasterman/hypothesis-torch/commit/38241edb76dd566f46282371fc5067911ad76dc0))

Bumps the lint-and-dev group with 4 updates in the / directory:
  [ruff](https://github.com/astral-sh/ruff),
  [pyright](https://github.com/RobertCraigie/pyright-python),
  [pytest](https://github.com/pytest-dev/pytest) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Updates `ruff` from 0.6.4 to 0.6.7 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.4...0.6.7)

Updates `pyright` from 1.1.379 to 1.1.381 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.379...v1.1.381)

Updates `pytest` from 8.3.2 to 8.3.3 - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.3.2...8.3.3)

Updates `mkdocs-material` from 9.5.34 to 9.5.36 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.34...9.5.36)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pyright
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev - dependency-name: pytest dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: mkdocs-material
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.15 (2024-09-06)

### Bug Fixes

- Only support memory formats for strided tensors
  ([`6add69f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6add69f419adacf0090079a3f7cb7b3bea23e02e))

### Continuous Integration

- Add pre-commit pyright/mypy full library
  ([`98c1985`](https://github.com/qthequartermasterman/hypothesis-torch/commit/98c198565454a8fa68d0735940e69238b3f0e139))

### Refactoring

- :recycle: extract internal function to more easily test available memory formats when inferring a
  strategy
  ([`b95feea`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b95feea541d397e6ccbac47e6fa2d04b57e7e91d))

### Testing

- Use zeros for sparse tensors
  ([`6519c27`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6519c278adaf7089dc752feb85e63d073f89aa1f))

- Fix missing arg
  ([`b14d1b9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b14d1b9a00254c38f43dadbda29b37436b517d91))

- Limit size of tensors for permitted memory format tests
  ([`c76bac8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c76bac89d68e55da895542c42bd7349136588ef7))

- Do correct assertion using dim order instead of contiguous for memory format
  ([`56f0997`](https://github.com/qthequartermasterman/hypothesis-torch/commit/56f0997d701eafa17fdb23e5080c2cb0650565f9))

- Assert tensor is contiguous
  ([`c358946`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c35894600e8cb970c3d3a04976b65e16a5af905c))

- Mark pragma no cover
  ([`b7b87d9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b7b87d911867a7b2559cac6164ad3b6fbd23e66e))

- :white_check_mark: add additional tests for `tensor_strategy` checking that passing in strategies
  as arguments is correct.
  ([`39795ce`](https://github.com/qthequartermasterman/hypothesis-torch/commit/39795ceccd3d596c4ab2c5ad667ffa79dd6c0d4d))


## v0.7.14 (2024-09-06)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 7 updates
  ([`c444527`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c4445275df35bf4f520d7e6024c0d3644b51b05f))

Bumps the lint-and-dev group with 7 updates in the / directory:

| Package | From | To | | --- | --- | --- | | [mypy](https://github.com/python/mypy) | `1.11.0` |
  `1.11.2` | | [ruff](https://github.com/astral-sh/ruff) | `0.5.4` | `0.6.4` | |
  [pyright](https://github.com/RobertCraigie/pyright-python) | `1.1.372` | `1.1.379` | |
  [pytest](https://github.com/pytest-dev/pytest) | `8.3.1` | `8.3.2` | |
  [mkdocs](https://github.com/mkdocs/mkdocs) | `1.6.0` | `1.6.1` | |
  [mkdocstrings[python]](https://github.com/mkdocstrings/mkdocstrings) | `0.25.1` | `0.26.1` | |
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material) | `9.5.29` | `9.5.34` |

Updates `mypy` from 1.11.0 to 1.11.2 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.11...v1.11.2)

Updates `ruff` from 0.5.4 to 0.6.4 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.4...0.6.4)

Updates `pyright` from 1.1.372 to 1.1.379 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.372...v1.1.379)

Updates `pytest` from 8.3.1 to 8.3.2 - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.3.1...8.3.2)

Updates `mkdocs` from 1.6.0 to 1.6.1 - [Release notes](https://github.com/mkdocs/mkdocs/releases) -
  [Commits](https://github.com/mkdocs/mkdocs/compare/1.6.0...1.6.1)

Updates `mkdocstrings[python]` from 0.25.1 to 0.26.1 - [Release
  notes](https://github.com/mkdocstrings/mkdocstrings/releases) -
  [Changelog](https://github.com/mkdocstrings/mkdocstrings/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/mkdocstrings/mkdocstrings/compare/0.25.1...0.26.1)

Updates `mkdocs-material` from 9.5.29 to 9.5.34 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.29...9.5.34)

--- updated-dependencies: - dependency-name: mypy dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: ruff
  dependency-type: direct:production update-type: version-update:semver-minor dependency-group:
  lint-and-dev - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pytest
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev - dependency-name: mkdocs dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: mkdocstrings[python]
  dependency-type: direct:production update-type: version-update:semver-minor dependency-group:
  lint-and-dev - dependency-name: mkdocs-material dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>

### Continuous Integration

- Move transformers to its own dependabot group
  ([`8f9e21c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8f9e21c66989b4aa69578a229bcf5d6508430c19))

- Move transformers to its own dependabot group
  ([`81eefab`](https://github.com/qthequartermasterman/hypothesis-torch/commit/81eefab044247b359062d01390eb0daa4fec1f3f))


## v0.7.13 (2024-09-05)

### Build System

- Drop support for pytorch 1.13
  ([`ab0beb1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ab0beb18dc099c6aec7e601f4751d807ebda530a))

### Code Style

- :label: Add type ignore in casting to memory format
  ([`1c8107b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1c8107b762e9ca746d7dda60f44d2a0f0276239f))

- :label: Add type ignore in casting to memory format
  ([`63b0646`](https://github.com/qthequartermasterman/hypothesis-torch/commit/63b0646f14cc3fc911ae4dc6896026933b756ac6))

### Continuous Integration

- Exclude impossible torch/python versions py3.12torch2.1.2
  ([`6129f33`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6129f3364a90bae7708fa9781028daf285195e86))

- Decrease dependabot frequency
  ([`d05f966`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d05f96656a4e7d15ebf98107a7a566e8641066ec))

- Fail fast false
  ([`34b761b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/34b761bee6353f89b4991b9f6c8d194b179de79f))

- Use cpu wheels
  ([`9b03cc7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/9b03cc74854853ea6de16ee83f21c3fae0fdda3d))

- Use cpu wheels
  ([`0610956`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0610956c304c0eb89d72401f14b8e051448bec61))

- Use cpu wheels
  ([`664acca`](https://github.com/qthequartermasterman/hypothesis-torch/commit/664accaea7be81a5ac6cd004c98a0482060f694b))

- Support testing against latest
  ([`81781e0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/81781e0e8fde386e962fd80ac2924a80c1fc5344))

- Support testing against latest
  ([`f65ea91`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f65ea91cc12d39113c500f3ca441fe28c5ffed1f))

- Support testing against latest
  ([`1d8980c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1d8980c1c22deb47615fddc8199e1590f1ab61aa))

- Fix torch version for github actions
  ([`f6a19ed`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f6a19ed1822649bb2dd5f3287bf15e1ec0063d2b))

- Fix torch version for github actions
  ([`3f6d3e1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3f6d3e1df8a6411c204bec29eca92c309009bbc1))

### Refactoring

- :recycle: :label: Use a type alias to avoid type checking issues in 2.4.0 related to Optimizer not
  being publicly exported for the type checker
  ([`dfcd394`](https://github.com/qthequartermasterman/hypothesis-torch/commit/dfcd394b888819a0d9ee59dc535a1ca91c83e25f))


## v0.7.12 (2024-07-22)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 6 updates
  ([`695301b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/695301b4171f4a31a6014560a1b471d7d133868f))

Updates the requirements on [transformers](https://github.com/huggingface/transformers),
  [mypy](https://github.com/python/mypy), [ruff](https://github.com/astral-sh/ruff),
  [pyright](https://github.com/RobertCraigie/pyright-python),
  [pytest](https://github.com/pytest-dev/pytest) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material) to permit the latest version.

Updates `transformers` to 4.42.4 - [Release
  notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.42.3...v4.42.4)

Updates `mypy` from 1.10.1 to 1.11.0 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.10.1...v1.11)

Updates `ruff` from 0.5.1 to 0.5.4 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.1...0.5.4)

Updates `pyright` from 1.1.370 to 1.1.372 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.370...v1.1.372)

Updates `pytest` from 8.2.2 to 8.3.1 - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.2.2...8.3.1)

Updates `mkdocs-material` from 9.5.28 to 9.5.29 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.28...9.5.29)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production
  dependency-group: lint-and-dev - dependency-name: mypy dependency-type: direct:production
  update-type: version-update:semver-minor dependency-group: lint-and-dev - dependency-name: ruff
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: pytest
  dependency-type: direct:production update-type: version-update:semver-minor dependency-group:
  lint-and-dev - dependency-name: mkdocs-material dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.11 (2024-07-06)

### Build System

- **deps**: Bump ruff from 0.5.0 to 0.5.1 in the lint-and-dev group
  ([`88cd5e8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/88cd5e80189b511ad659a49067da5889b9f2ea60))

Bumps the lint-and-dev group with 1 update: [ruff](https://github.com/astral-sh/ruff).

Updates `ruff` from 0.5.0 to 0.5.1 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.0...0.5.1)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.10 (2024-07-05)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 5 updates
  ([`6e39b50`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6e39b50a117d25a1b88f25248f939b7f8ce966ab))

Updates the requirements on [transformers](https://github.com/huggingface/transformers),
  [mypy](https://github.com/python/mypy), [ruff](https://github.com/astral-sh/ruff),
  [pyright](https://github.com/RobertCraigie/pyright-python) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material) to permit the latest version.

Updates `transformers` to 4.42.3 - [Release
  notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.0.0...v4.42.3)

Updates `mypy` from 1.10.0 to 1.10.1 -
  [Changelog](https://github.com/python/mypy/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/python/mypy/compare/v1.10.0...v1.10.1)

Updates `ruff` from 0.4.9 to 0.5.0 - [Release notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.9...0.5.0)

Updates `pyright` from 1.1.367 to 1.1.370 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.367...v1.1.370)

Updates `mkdocs-material` from 9.5.26 to 9.5.28 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.26...9.5.28)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production
  dependency-group: lint-and-dev - dependency-name: mypy dependency-type: direct:production
  update-type: version-update:semver-patch dependency-group: lint-and-dev - dependency-name: ruff
  dependency-type: direct:production update-type: version-update:semver-minor dependency-group:
  lint-and-dev - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: mkdocs-material
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.9 (2024-06-14)

### Build System

- **deps**: Bump the lint-and-dev group across 1 directory with 2 updates
  ([`c6351ed`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c6351edc732dbdfe25b43b60b7409320508f04ad))

Bumps the lint-and-dev group with 2 updates in the / directory:
  [pyright](https://github.com/RobertCraigie/pyright-python) and
  [mkdocs-material](https://github.com/squidfunk/mkdocs-material).

Updates `pyright` from 1.1.365 to 1.1.367 - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.365...v1.1.367)

Updates `mkdocs-material` from 9.5.25 to 9.5.26 - [Release
  notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.25...9.5.26)

--- updated-dependencies: - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch dependency-group: lint-and-dev - dependency-name: mkdocs-material
  dependency-type: direct:production update-type: version-update:semver-patch dependency-group:
  lint-and-dev ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.8 (2024-06-14)

### Build System

- **deps**: Bump dawidd6/action-download-artifact from 5 to 6
  ([`1564e20`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1564e20d570cb4651d720935306ca77e9cde1f63))

Bumps [dawidd6/action-download-artifact](https://github.com/dawidd6/action-download-artifact) from 5
  to 6. - [Release notes](https://github.com/dawidd6/action-download-artifact/releases) -
  [Commits](https://github.com/dawidd6/action-download-artifact/compare/v5...v6)

--- updated-dependencies: - dependency-name: dawidd6/action-download-artifact dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.7 (2024-06-14)

### Build System

- **deps**: Bump ruff from 0.4.7 to 0.4.9
  ([`f39bef8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f39bef82626eba4df6b99060e529e61a13e19502))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.7 to 0.4.9. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.7...v0.4.9)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Continuous Integration

- Merge all dependabot PRs into one using dependabot groups.
  ([`2352a54`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2352a540015d7d1ef32fb5302ecc50537a7ab1e1))


## v0.7.6 (2024-06-14)

### Build System

- **deps**: Bump pytest from 8.2.1 to 8.2.2
  ([`9787eb1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/9787eb1acac51f4acc02a5317983b778696ced49))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.2.1 to 8.2.2. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.2.1...8.2.2)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump dawidd6/action-download-artifact from 3.1.4 to 5
  ([`380fee0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/380fee0f731bcf480443f399b26b73227e86400a))

Bumps [dawidd6/action-download-artifact](https://github.com/dawidd6/action-download-artifact) from
  3.1.4 to 5. - [Release notes](https://github.com/dawidd6/action-download-artifact/releases) -
  [Commits](https://github.com/dawidd6/action-download-artifact/compare/v3.1.4...v5)

--- updated-dependencies: - dependency-name: dawidd6/action-download-artifact dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.5 (2024-06-07)

### Bug Fixes

- Only generate `mps:0` devices.
  ([`bafcdd3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bafcdd34ebf26474890684dfb1d126d288533781))

Because `torch.device('mps') != torch.device('mps:0')`, and tensors sent to either device will end
  up on `mps:0`, it feels fitting to only include `mps:0` in the device strategy, similar to how we
  only generate indexed `cuda` devices.

```python import torch

mps_device = torch.device("mps") mps_0_device = torch.device("mps:0") print(mps_device,
  mps_0_device, mps_device == mps_0_device) # mps mps:0 False # I expect these to be equal, because
  tensors on the mps device get placed on the mps:0 device

mps_tensor = torch.randn(2, 3, device=mps_device) mps_0_tensor = torch.randn(2, 3,
  device=mps_0_device) print(mps_tensor.device, mps_0_tensor.device, mps_tensor.device ==
  mps_0_tensor.device) # mps:0 mps:0 True # This matches what I expect ```


## v0.7.4 (2024-06-04)

### Build System

- **deps**: Bump pyright from 1.1.364 to 1.1.365
  ([`80ac03d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/80ac03de59d7d9c10824ddf611661366cab57463))

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.364 to 1.1.365. - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.364...v1.1.365)

--- updated-dependencies: - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.3 (2024-06-03)

### Build System

- **deps**: Update transformers requirement
  ([`803d9fb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/803d9fb626113e7d0800bee72ac401b40cfe9a2c))

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit
  the latest version. - [Release notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.0.0...v4.41.2)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump ruff from 0.4.5 to 0.4.7
  ([`7709d1e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7709d1e480624c9cb0421215d063b45855f3c43b))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.5 to 0.4.7. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.5...v0.4.7)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.2 (2024-05-28)

### Build System

- **deps**: Bump mkdocs-material from 9.5.24 to 9.5.25
  ([`55eb6fd`](https://github.com/qthequartermasterman/hypothesis-torch/commit/55eb6fd2ed7b28ab256d8e427b06c0e1e21bf930))

Bumps [mkdocs-material](https://github.com/squidfunk/mkdocs-material) from 9.5.24 to 9.5.25. -
  [Release notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.24...9.5.25)

--- updated-dependencies: - dependency-name: mkdocs-material dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.1 (2024-05-24)

### Build System

- **deps**: Update transformers requirement
  ([`a3167a4`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a3167a421bb5e94b66b27c27964596f4cae8a98b))

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit
  the latest version. - [Release notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.0.0...v4.41.1)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump ruff from 0.4.4 to 0.4.5
  ([`102bd96`](https://github.com/qthequartermasterman/hypothesis-torch/commit/102bd96f354ef73d7b848183af21ffb02fb6c96b))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.4 to 0.4.5. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.4...v0.4.5)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Chores

- **deps**: Update transformers requirement
  ([`ca6f76a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ca6f76a4d96f4fb60bb7ec4a56010ef247a54cb3))

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit
  the latest version. - [Release notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.0.0...v4.41.0)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump mkdocs-material from 9.5.23 to 9.5.24
  ([`e3b5bf9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e3b5bf9a0cc23769aecb336bf38c02d10e70c250))

Bumps [mkdocs-material](https://github.com/squidfunk/mkdocs-material) from 9.5.23 to 9.5.24. -
  [Release notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.23...9.5.24)

--- updated-dependencies: - dependency-name: mkdocs-material dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pytest from 8.2.0 to 8.2.1
  ([`cf6fb67`](https://github.com/qthequartermasterman/hypothesis-torch/commit/cf6fb673d4eeb551694808a118d96e7b57950d66))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.2.0 to 8.2.1. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.2.0...8.2.1)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump pyright from 1.1.359 to 1.1.363
  ([`45416ce`](https://github.com/qthequartermasterman/hypothesis-torch/commit/45416ceafa8788ef279828a84887682a5ccc63a1))

Bumps [pyright](https://github.com/RobertCraigie/pyright-python) from 1.1.359 to 1.1.363. - [Release
  notes](https://github.com/RobertCraigie/pyright-python/releases) -
  [Commits](https://github.com/RobertCraigie/pyright-python/compare/v1.1.359...v1.1.363)

--- updated-dependencies: - dependency-name: pyright dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump mkdocs-material from 9.5.22 to 9.5.23
  ([`b5ef3b8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b5ef3b84d2e948f2bf7ee341850a02b52c168704))

Bumps [mkdocs-material](https://github.com/squidfunk/mkdocs-material) from 9.5.22 to 9.5.23. -
  [Release notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.5.22...9.5.23)

--- updated-dependencies: - dependency-name: mkdocs-material dependency-type: direct:production
  update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.7.0 (2024-05-14)

### Bug Fixes

- :bug: :label: improve type hints that mypy complained about
  ([`b62c0f7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b62c0f766f7e82631cfe53ce1a362fd6ef6026c3))

BREAKING-CHANGE: hypothesis will no longer (incorrectly) generate a arbitrary CUDA torch.devices
  when using builds on `torch.cuda.device`.

- :bug: :label: remove support for `Mapping[str, Any]` as `elements` argument to `tensor_strategy`.
  ([`015abc0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/015abc0d77dfe0479e89e44bc74fe46ac0d77d7d))

Passing in a mapping, although supported by the `numpy` strategy used internally, is rarely used for
  generating tensors, and overly complicates the error handling for bfloat16 tensors.

BREAKING-CHANGE: Removed support for `Mapping[str, Any]` as `elements` argument to
  `tensor_strategy`.

### Code Style

- Enable ruff style rules.
  ([`680bacf`](https://github.com/qthequartermasterman/hypothesis-torch/commit/680bacfb1f99c3504635b0967f5725e249ffb670))

- Enable flake9-use-pathlib annotation via ruff.
  ([`fb60e9c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fb60e9ca073f62e8121553d3268f9eab9c86c2a0))

- Enable pyflakes annotation via ruff.
  ([`829bbf7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/829bbf7a4e82ad852ec10c9a72cc3ac230e8a9ee))

- Upgrade internal references to deprecated/moved python typing constructs to be compatible with
  python 3.9
  ([`04b15c1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/04b15c1f9cd17a7e85f9f8449fdf354739798591))

- Enable pycodestyle warning via ruff.
  ([`7b4d0c7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7b4d0c78ffac8fb62fccd7c03eac5747ad2dcf7c))

- Adopt perflint via ruff for internal code.
  ([`12ec834`](https://github.com/qthequartermasterman/hypothesis-torch/commit/12ec834f36e1d72f65708baf27c0f5e32335ea0a))

- Adopt refurb via ruff for internal code.
  ([`0fe5f13`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0fe5f13a8728aa6f58deb4a8b95088258775164a))

- Adopt isort via ruff for internal code.
  ([`2dc520d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2dc520d839d4f00080581bf3c4f7955e5db67b5b))

### Continuous Integration

- Enable mypy in ci
  ([`e43a139`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e43a13969f3e00bb30f1a16a2cfecf750af5a831))

- Enable mypy in pre-commit and use local ruff
  ([`5751de7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5751de7a37647806323c3fe5959c94701e10881e))

- Enable pyright in pre-commit
  ([`57b7a44`](https://github.com/qthequartermasterman/hypothesis-torch/commit/57b7a441532ab2ba33cd16457433db29a0574443))

- Enable pyright in CI
  ([`c7508c6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c7508c65d7a79291fd9ca513d52e4f1a35c4a9d3))

- Enable pyright in CI
  ([`ae70427`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ae70427883312ade461ccaa03fbcd8731df956be))

### Documentation

- :label: improve type hints for `transformer_strategy` by fixing missing `None` Type and incorrect
  return type.
  ([`c435e3c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c435e3c16e5016ab634a0b9c1d020c7e1dc02c1d))

- :label: improve type hints for `optimizer_strategy` by fixing missing `None` Type and incorrect
  return type.
  ([`4001a0c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4001a0c4fb0e8b94bd167baf3d1c2e76fe7c15af))

- :label: improve type hints for internal implementation details of `alternate` iterable util
  function.
  ([`3f85472`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3f85472baf44b121b31078024efc0537b39c3c71))

- :label: improve type hints for internal implementation by making some imports explicit.
  ([`e6ac523`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e6ac5233e6b669e6e3d414df9a01eb7e4c609820))

- :label: improve type hints for internal TorchRandomWrapper object.
  ([`af953ce`](https://github.com/qthequartermasterman/hypothesis-torch/commit/af953ced15294b8023078436e2b304f3eef55c46))


## v0.6.4 (2024-05-13)

### Build System

- Remove upper pin on hypothesis and torch range
  ([`bfe6953`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bfe695331d870897bacb5e692ba54f2eb532801c))

### Chores

- **deps**: Bump dawidd6/action-download-artifact from 2.24.3 to 3.1.4
  ([`48bc9e3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/48bc9e314b0d356eafd0dd14c31a5e1976f6a946))

Bumps [dawidd6/action-download-artifact](https://github.com/dawidd6/action-download-artifact) from
  2.24.3 to 3.1.4. - [Release notes](https://github.com/dawidd6/action-download-artifact/releases) -
  [Commits](https://github.com/dawidd6/action-download-artifact/compare/v2.24.3...v3.1.4)

--- updated-dependencies: - dependency-name: dawidd6/action-download-artifact dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump mkdocs-material from 9.4.6 to 9.5.22
  ([`34558be`](https://github.com/qthequartermasterman/hypothesis-torch/commit/34558be28f578d76887fa362c01827215b7bbcfd))

Bumps [mkdocs-material](https://github.com/squidfunk/mkdocs-material) from 9.4.6 to 9.5.22. -
  [Release notes](https://github.com/squidfunk/mkdocs-material/releases) -
  [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG) -
  [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.4.6...9.5.22)

--- updated-dependencies: - dependency-name: mkdocs-material dependency-type: direct:production
  update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump ruff from 0.4.3 to 0.4.4
  ([`aa33cf8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/aa33cf872497398e30ae176e5f4e7633cba1ebe4))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.3 to 0.4.4. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.3...v0.4.4)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Update transformers requirement
  ([`06102ea`](https://github.com/qthequartermasterman/hypothesis-torch/commit/06102ea4bd0afddcd843ff72d5f76d321bb6eaad))

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit
  the latest version. - [Release notes](https://github.com/huggingface/transformers/releases) -
  [Commits](https://github.com/huggingface/transformers/compare/v4.0.0...v4.40.2)

--- updated-dependencies: - dependency-name: transformers dependency-type: direct:production ...

Signed-off-by: dependabot[bot] <support@github.com>

### Continuous Integration

- Increase dependabot frequency
  ([`e44cd5f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e44cd5f45133d1d0915e4b1c12ccf8aa1cf8b000))

- Fix missing coverage comment by creating pytest-coverage.txt file during build
  ([`a8772c9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a8772c9abc14ab2a53aed3eb9c3c2c6beab97e52))

- Store hypothesis database in GitHub Actions to allow reproducing locally
  ([`fd62aca`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fd62acad596925d0ae58187767452df1bd6b9350))


## v0.6.3 (2024-05-12)

### Bug Fixes

- :bug: fix incompatible parameters when generating Adam optimizers on Torch 1.13.
  ([`d0ef6bb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d0ef6bb44b935879864915c15496986afafc9375))

Fix incompatible parameters: - fused is only available if cuda is available - fused is incompatible
  with differentiable

### Documentation

- Update pyproject toml classifiers, keywords, and urls.
  ([`e6d4a7c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e6d4a7c63921a097a8fc419c06c5483d4baa092c))

- **badges**: :memo: Add pypi badges for downloads and version to readme
  ([`00563e6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/00563e65d7e652bc5bcc51ca185f8b05d908c352))

- **version**: :memo: remove reference to python 3.8 in classifiers
  ([`03322e1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/03322e156f3c118ef10ea2d2395076088e5960d8))


## v0.6.2 (2024-05-10)

### Build System

- :bug: set dependency ranges for optimal compatability
  ([`4a25c1d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4a25c1dcd5e189df62ff8fe7fede4351447d415f))


## v0.6.1 (2024-05-10)

### Bug Fixes

- :bug: do not try to use the device as a context manager in torch<2.
  ([`3114162`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3114162fb77ed48ecb5d980b4e2b41c6184bc3ae))

- :bug: do not try to use the meta device as a context manager in torch<2.
  ([`ef0e47c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ef0e47c20a65606400b1335902417db0c88f0f79))

- :zap: remove overly-restrictive hypothesis deadline for transformers tests
  ([`d1c89f2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d1c89f2dceed4132dc363b63b1b27a75bd191d87))

### Build System

- :zap: remove unnecessary tee to avoid supressing error code
  ([`8716033`](https://github.com/qthequartermasterman/hypothesis-torch/commit/87160333a8ba121b710fedde3f29066e711e6c19))

- Fix incorrect reusable workflow path
  ([`ec36fc6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ec36fc68b1a0acf62902623ca67983c1fc699914))

- Test pytorch 1.13 in CI
  ([`6aff502`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6aff502b464bb3c5a43ca19acc4ff4854b104056))

- Convert workflow to reusable workflow for simplicity
  ([`b1aa17a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b1aa17a70bd93c51f8c9f9f297741f53c90fcb00))

- :sparkles: :memo: Add readthedocs configuration.
  ([`95ffac5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/95ffac52292a6290ad5a2f418c0e11d40c9c1af3))

### Documentation

- :sparkles: :memo: Add index page
  ([`510e3df`](https://github.com/qthequartermasterman/hypothesis-torch/commit/510e3dfedd2af3afae3b569183574ee223eb31f1))

- :sparkles: :memo: Add strategies reference to docs.
  ([`8fc0d95`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8fc0d95d89b06191e5aaa9bf8214f9e92f3caca5))

- :sparkles: :memo: Add compatability guide to docs.
  ([`ca3bada`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ca3badae4a2096f2ab84373c7118452cd4626e20))

- :sparkles: :memo: Disable top tabs on docs.
  ([`53164a2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/53164a2febb25f86630e2b26e27f01a941bfa8e1))

- :sparkles: :memo: Add quick start guide to docs.
  ([`2710504`](https://github.com/qthequartermasterman/hypothesis-torch/commit/27105049976e83a024af4cb5d1c6d8314005cf7f))

- :sparkles: :memo: Add quick start guide to docs.
  ([`a59871c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a59871c2755088c9954384bdca7e395a51f71868))

- :sparkles: :memo: Add contribuging guidelines to docs.
  ([`3f30767`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3f3076763b50de5a4c663faed4113490cb8d5ad2))

- :sparkles: :memo: Add changelog to docs.
  ([`05dc054`](https://github.com/qthequartermasterman/hypothesis-torch/commit/05dc05400bcf4c7b8d0da34822bd67b8150e67e6))

- :sparkles: :memo: Add changelog to docs.
  ([`ddb9598`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ddb95980bb5e9fda47af72977fcd33b1954be122))

- :sparkles: :memo: Add license file to docs.
  ([`06adb42`](https://github.com/qthequartermasterman/hypothesis-torch/commit/06adb42eaf466688b97878daf2395cb957536fee))

- :sparkles: Initial docsite set up.
  ([`274bb65`](https://github.com/qthequartermasterman/hypothesis-torch/commit/274bb6512912fab817c71f394a3ccfad124de625))

### Testing

- :bug: ignore runtime errors during module import
  ([`882f515`](https://github.com/qthequartermasterman/hypothesis-torch/commit/882f5156d4ceb9b7533dd8d10b2a854c0af2e472))

- :bug: ignore runtime errors during module import
  ([`5c89c79`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5c89c79ffedb88a5b9dce24a4cdbbf4354b7a82d))


## v0.6.0 (2024-05-09)


## v0.5.0 (2024-05-09)

### Bug Fixes

- :label: fix incorrect decorator typing
  ([`3e80d6a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3e80d6a0f71b6cde8f539150bffffe9ee338253b))

- :white_check_mark: designate officially supported versus unofficially supported transformers.
  ([`7d22190`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7d22190766613db31a220b0cda54bb79d73cc6b1))

By default, only officially supported transformer types are tested in CI, but unofficially supported
  transformers MAY or MAY NOT be compatible with the `transformer_strategy`. A test fully
  parametrized over ALL of the model types in `transformers` is available, and can be enabled when
  setting the environment variable `HYPOTHESIS_TORCH_TEST_UNSUPPORTED_TRANSFORMERS=True`.

### Build System

- 🔧 add py.typed
  ([`bef3985`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bef3985b6747e29f18ed45e7984945a6767190a9))

### Chores

- **deps**: Bump pytest from 8.1.1 to 8.2.0
  ([`75fd127`](https://github.com/qthequartermasterman/hypothesis-torch/commit/75fd127ec1fcbb64a95eb82dc0ae03e7faeee3fc))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.1.1 to 8.2.0. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.1.1...8.2.0)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:production update-type:
  version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump ruff from 0.4.1 to 0.4.3
  ([`c7e5d8d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c7e5d8d0c611a03dd03a8cc6373e4992e709919b))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.1 to 0.4.3. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/v0.4.1...v0.4.3)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:production update-type:
  version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

### Testing

- Ignore import errors while inferring available transformers in tests.
  ([`84185cb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/84185cb66fcec5f50aad09e38b0026624ca5862a))

- Disable deadline for occasionally slow tests
  ([`34ae9db`](https://github.com/qthequartermasterman/hypothesis-torch/commit/34ae9db1d2ef05433c87a25a4d17aa224c67b4ff))


## v0.4.3 (2024-04-28)

### Bug Fixes

- :bug: do not generate inf values if elements has infinity disabled for bfloat16 tensors.
  ([`cda8577`](https://github.com/qthequartermasterman/hypothesis-torch/commit/cda8577aebf2bed7d8c86a8e5ac1c1d19d5cd57c))

Before, if a float strategy that prevented infinities was provided to as `elements` to
  `tensor_strategy`, the resultant tensor could still occasionally have infinities because the
  strategy would generate float32 values that exceeded the maximium/minimum values for bfloat16.


## v0.4.2 (2024-04-27)

### Bug Fixes

- :bug: do not generate inf values if elements has infinity disabled for float16 and float32
  tensors.
  ([`8e9eb5d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8e9eb5daf6f94e121ad6554bb1a41fcd73ac8da0))

This fix does not work for all bfloat16 tensors.

### Features

- :sparkles: add support for more transformers strategies
  ([`7ac7508`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7ac75088956adf3ec5b06b9352d6ed7c0492ad59))

- :sparkles: add strategies for torch optimizer types and torch optimizer instances
  ([`5cf6181`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5cf6181ef6617eda19eb0b51658f835280421c63))

NOTE: The strategy for torch optimizers actually generates an "alternate constructor" for a torch
  optimizer that takes in only a torch module's parameters. The strategy will "pre-fill" all of the
  hyperparameters. If these hyparameters should be overridden, they can be specified as kwargs in
  the strategy.


## v0.4.1 (2024-04-24)

### Bug Fixes

- Mark bfloat16 as a floating dtype
  ([`38b4ed3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/38b4ed3425439525848375a5bd200786d3dfd236))


## v0.4.0 (2024-04-24)

### Features

- Register random torch state as a hypothesis entry point (so that torch state is always registered,
  even if hypothesis-torch is never imported).
  ([`eada00a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/eada00a8beb3632799a83256a2b24c3a4faa070b))

- Register random torch state with hypothesis
  ([`633bf82`](https://github.com/qthequartermasterman/hypothesis-torch/commit/633bf82aa3873452dbb674f7f0b18b8a378a3027))


## v0.3.1 (2024-04-24)

### Bug Fixes

- :truck: move test to test folder
  ([`e7460f7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e7460f7d11a84cc0a4791b90c02932505399bd5d))

### Continuous Integration

- Coverage report
  ([`36b8eb9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/36b8eb909fdd266b8469ccd3a2c162ebf1310af1))

### Testing

- Ignore coverage on pairwise.
  ([`0cec9ba`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0cec9baf36cfcb2fbd9d8f10abd5663237887b2e))


## v0.3.0 (2024-04-24)

### Continuous Integration

- Coverage report
  ([`3f80154`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3f8015442c1244f4b127d7bf98b6e8d07eae77d3))

- Use faster ci settings
  ([`e36cca7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e36cca712d76ed5583424868e9b0cb04f5855794))

### Features

- :sparkles: add pin_memory to tensor generation
  ([`dc42447`](https://github.com/qthequartermasterman/hypothesis-torch/commit/dc42447ec057ac7bc1939c1491fdd53c9e9bece2))

- :sparkles: add requires_grad to tensor generation
  ([`51bda34`](https://github.com/qthequartermasterman/hypothesis-torch/commit/51bda34b0e33f71708e43279969908dbe656be87))

- :sparkles: allow tensor strategy to sample over layout and memory format
  ([`af02d54`](https://github.com/qthequartermasterman/hypothesis-torch/commit/af02d542d84049c9ece7c738799c9472b8332c44))

- :sparkles: add layout argument to tensor strategy
  ([`a77069c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a77069cc8502f15c69b46fd16a92926645b4e9b5))

- :sparkles: add strategies for layout and memory format
  ([`153fa0b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/153fa0bd49c51c04c31784cbb83dd42e1f41dbe9))

### Refactoring

- :recycle: rename global private constant
  ([`3fcfac6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3fcfac64d9ccbe4cda70d1fc1ad2caa8af539bf0))

- :recycle: improve typing to enforce global constants
  ([`c46f53c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c46f53c86e3b9cfffb609a18a9d21e744002e91b))

### Testing

- :white_check_mark: unit tests for scalar tensors
  ([`9f543d6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/9f543d63b09def247bc1ca56b7089d977a1c79f1))


## v0.2.0 (2024-04-23)

### Continuous Integration

- Set hypothesis profile
  ([`bfecac5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bfecac520ad961687a258626a1b61d3220e6e150))

### Documentation

- :label: improve typing
  ([`0bd9170`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0bd917036cd11d09fc4da21fd18fc857cc950dca))

- Update root docstring
  ([`2f9395f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2f9395f7749a2914dc586471e8fe3d86fd3904f5))

### Features

- :recycle: :sparkles: allow overriding examples of activation functions
  ([`3746915`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3746915c9068da28ce6893dd8b2c1f407bd2db42))

- Add available dtypes and device sets to root imports
  ([`91f8ea3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/91f8ea3df5de2e1a16dc5571fc8ee0d5630ff40b))

### Refactoring

- :zap: :recycle: do not define dtype_strategy as as composite strategy to avoid overhead
  ([`e47ea82`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e47ea82aabba12f4a7e16865829e6b2ec3b59a2f))

- :zap: :recycle: do not define device_strategy as as composite strategy to avoid overhead
  ([`221d72a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/221d72a99dc3ca40a6cec3800a12833026dc46d2))

### Testing

- :fire: remove redundant type hints
  ([`bcf95c4`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bcf95c4b21f11cccc38fa9e593fa391ad47bd645))

- :white_check_mark: unit tests for activation strategy
  ([`dfa900e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/dfa900e47bf90d4cdfa4e278d6bd9ae928307aa2))


## v0.1.10 (2024-04-23)

### Bug Fixes

- Only generate sensible floats and integer values for the given dtype
  ([`8175a73`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8175a73bce4888a546215517145c0b85d5b4624d))

### Chores

- **deps**: Bump actions/setup-python from 2 to 5
  ([`ad754e1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ad754e1d75f802ef21fbec3ab4e0e74f9fc043cf))

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 2 to 5. - [Release
  notes](https://github.com/actions/setup-python/releases) -
  [Commits](https://github.com/actions/setup-python/compare/v2...v5)

--- updated-dependencies: - dependency-name: actions/setup-python dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

### Continuous Integration

- Set hypothesis profile
  ([`c2aae43`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c2aae43546887810aca3b64965d99f93857f2887))


## v0.1.9 (2024-04-22)

### Bug Fixes

- Only generate sensible floats for Softplus threshold
  ([`6d81c89`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6d81c89f516688fae34bedcb5a5254db11de92d5))

### Chores

- **deps**: Bump stefanzweifel/git-auto-commit-action from 4 to 5
  ([`77dcfa5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/77dcfa5cda44125a738f7338338c823e9c708d04))

Bumps
  [stefanzweifel/git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action)
  from 4 to 5. - [Release notes](https://github.com/stefanzweifel/git-auto-commit-action/releases) -
  [Changelog](https://github.com/stefanzweifel/git-auto-commit-action/blob/master/CHANGELOG.md) -
  [Commits](https://github.com/stefanzweifel/git-auto-commit-action/compare/v4...v5)

--- updated-dependencies: - dependency-name: stefanzweifel/git-auto-commit-action dependency-type:
  direct:production update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump actions/checkout from 3 to 4
  ([`1409079`](https://github.com/qthequartermasterman/hypothesis-torch/commit/140907957ed24f6adf196c9a4a0b01cb3ab9fe5f))

Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4. - [Release
  notes](https://github.com/actions/checkout/releases) -
  [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/actions/checkout/compare/v3...v4)

--- updated-dependencies: - dependency-name: actions/checkout dependency-type: direct:production
  update-type: version-update:semver-major ...

Signed-off-by: dependabot[bot] <support@github.com>

### Code Style

- Ruff
  ([`7d94775`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7d947759e6655052e39d6753deb881080db0e643))

### Continuous Integration

- Enable dependabot
  ([`42524ee`](https://github.com/qthequartermasterman/hypothesis-torch/commit/42524eef2f96134d6a8a4103925adc271460a15c))

- Enable dependabot
  ([`1e63f06`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1e63f06f995c1e329aa89ffefe73e09ca37254a7))

### Testing

- :white_check_mark: unit tests for linear strategy
  ([`5dbfe6e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5dbfe6e618acc4aea31d2a81419f1736509bfd01))


## v0.1.8 (2024-04-22)

### Bug Fixes

- Only mark MPS devices as available if MPS itself is available
  ([`d277350`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d277350ff3de4d359011a8b234aef5beff227880))

### Chores

- Pre-commit configuration
  ([`2c8efaa`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2c8efaa03c87a56cb3483fc1f07ca080b598ddd5))

### Code Style

- :rotating_light: ruff
  ([`8912c96`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8912c96eaa5e96e8b5d117989030e7c763ee4702))

- :rotating_light: ruff
  ([`6599c7d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6599c7d062c6eeaa09fcab5b5cdd64f8f1fe29c0))

- :rotating_light: ruff format
  ([`97f6e6e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/97f6e6e31f564442b9384b60717e0c1dc030fcc2))

### Continuous Integration

- Fix github actions
  ([`1b6d8b2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1b6d8b29b460579730954210fbb221db200a53d7))

- Fix github actions
  ([`a3abe85`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a3abe8564863bf5818fecc900b538d647051d528))

- Add PR build
  ([`3284a11`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3284a1168e75bb33f95a119406d1c73a85c28d26))

### Testing

- :white_check_mark: unit tests for tensors
  ([`50da775`](https://github.com/qthequartermasterman/hypothesis-torch/commit/50da77539f9d4d30165d6f136d46518b7991b00d))

- :white_check_mark: unit tests for iterable utils
  ([`f262c89`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f262c8936ac1dfc7b2d4b082d5478ad5111a3bf2))


## v0.1.7 (2024-04-21)

### Bug Fixes

- :label: typing fixes
  ([`a03d697`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a03d6979d47f9b2bd5c4a8328e9b1927fdc96339))

### Continuous Integration

- Use deploy key to bypass branch protection
  ([`22dd442`](https://github.com/qthequartermasterman/hypothesis-torch/commit/22dd442de7435f78eac1d7b6fddb3ecf8b6d67f6))

- Use uv to install requirements
  ([`a87ef0a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a87ef0a45fe74478f1a996ed1dd0883d00ab5bc9))

- Use uv to install requirements
  ([`3d4a0b0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3d4a0b02c31dd04f6f3c9a3bec946c81dab83f01))


## v0.1.6 (2024-04-21)

### Bug Fixes

- Semantic release reference in pyproject toml
  ([`7fe09c9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7fe09c9da9dcdb9d746ad08717870e6b43ecfa88))


## v0.1.5 (2024-04-21)

### Bug Fixes

- Clean up imports
  ([`fc93cd5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fc93cd5b56f605713272085329bbb5fcd1134f3d))


## v0.1.4 (2024-04-21)

### Bug Fixes

- Build command and dynamic version for setuptools
  ([`cd1889d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/cd1889dd687904b1f8a1a946bdf41f2d17ac6c0f))


## v0.1.3 (2024-04-21)

### Bug Fixes

- Allow manually launching release
  ([`f651484`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f651484d092ce20e4d93c3406309069e5c551af9))


## v0.1.2 (2024-04-21)

### Bug Fixes

- Upload to pypi using semantic release
  ([`98ac240`](https://github.com/qthequartermasterman/hypothesis-torch/commit/98ac24014307ca8ac6e14170652fd4448228ccd8))


## v0.1.1 (2024-04-21)

### Bug Fixes

- Fix semantic release settings
  ([`b702e85`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b702e85e319324a2904f73a003121aa7bd6ffd6d))

### Continuous Integration

- Publish to pypi
  ([`6d3bd54`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6d3bd54eaf0dc12ff705e6f3847e25c27bacb8d1))


## v0.1.0 (2024-04-21)

### Bug Fixes

- Add urls
  ([`6c8dd3d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6c8dd3d72463e133ec5695e38d0f590e694d9f50))

- Allow `unique` to be a strategy
  ([`50bedeb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/50bedeba2f54b1333fa38ccc06abe5010ab8f6ec))

- Rename parameter
  ([`1df242d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1df242dcc8f6ac3ea589f74614e942cd7b59bf18))

### Chores

- Specify optional dependencies
  ([`fe1b34e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fe1b34ea1dd58c8bd637b678a3901cde811ef0fa))

- Typing
  ([`8b184e0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8b184e0fa72dda66c75cbfe31929869e3cfebfd6))

- Set optional dependencies
  ([`64547b3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/64547b3cb5a7219aef3871e3d68eabcbcecb4b74))

- Pyproject toml
  ([`a1bfdaa`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a1bfdaa067915518600cdc5d187c8a2d75c346b5))

### Code Style

- :rotating_light: ruff
  ([`d653c6b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d653c6b8a2291a150d192f14c2b3f2f385828cc4))

- :rotating_light: ruff
  ([`3d4efaa`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3d4efaa4c44b235e33a8f7942d72f72eb733ff27))

- :rotating_light: ruff
  ([`2d4f14b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2d4f14b39ab4341bfdb39df48c51a513100aaf1c))

### Continuous Integration

- Fix master->main incorrectly named workflow branch
  ([`a110bd9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a110bd9f557fef5271f534d909cfa8f384281466))

- Semantic relase
  ([`5febe77`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5febe77ae294bd5cc42d52729fdfebb964fab759))

### Documentation

- :memo: write first README draft
  ([`1c5e799`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1c5e79981719887191868432d82aa6ea091fe544))

### Features

- Modify linear network strategy api
  ([`4c7d831`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4c7d831f7b1d61383da5b1254ea44fb897c4732a))

- Import transformer strategy into root if and only if transformers is installed
  ([`b314203`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b3142037e069fad2f4a659296c350558a58e9fd7))

- Import strategies into the root
  ([`eaa7a78`](https://github.com/qthequartermasterman/hypothesis-torch/commit/eaa7a78d5a8fdcccc35f577c33d4b50516d9efcb))

- Generate modules
  ([`ad8f103`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ad8f103e7b4f3b2608f0b12f7068c63f7b1903ef))

- Inspection_util.py
  ([`1d22dc8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1d22dc8b927dba4ec5b301503f791aef4a64ffe5))

- Generate hugging face transformers
  ([`74a1ae2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/74a1ae2f25afde8a676401dd3e65d3a8f43c6d54))

- Generate tensors
  ([`e9785d7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e9785d78c4d68e4fd0e80591319a5b3934031b5e))

- Dtype strategies
  ([`723f096`](https://github.com/qthequartermasterman/hypothesis-torch/commit/723f096bc36164f09cc6662fccb56e2bc2ae3f8b))

- Device strategies
  ([`1acab83`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1acab833ea64a71aedf134879ec07a9270a96b88))

### Testing

- Update device test
  ([`74e9b90`](https://github.com/qthequartermasterman/hypothesis-torch/commit/74e9b90ff5d5847b3ea861940518b8458a160e2c))
