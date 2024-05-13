# CHANGELOG



## v0.6.4 (2024-05-13)

### Build

* build: remove upper pin on hypothesis and torch range ([`bfe6953`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bfe695331d870897bacb5e692ba54f2eb532801c))

### Chore

* chore(deps): bump ruff from 0.4.3 to 0.4.4

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.3 to 0.4.4.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.4.3...v0.4.4)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`aa33cf8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/aa33cf872497398e30ae176e5f4e7633cba1ebe4))

* chore(deps): bump mkdocs-material from 9.4.6 to 9.5.22

Bumps [mkdocs-material](https://github.com/squidfunk/mkdocs-material) from 9.4.6 to 9.5.22.
- [Release notes](https://github.com/squidfunk/mkdocs-material/releases)
- [Changelog](https://github.com/squidfunk/mkdocs-material/blob/master/CHANGELOG)
- [Commits](https://github.com/squidfunk/mkdocs-material/compare/9.4.6...9.5.22)

---
updated-dependencies:
- dependency-name: mkdocs-material
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`34558be`](https://github.com/qthequartermasterman/hypothesis-torch/commit/34558be28f578d76887fa362c01827215b7bbcfd))

* chore(deps): update transformers requirement

Updates the requirements on [transformers](https://github.com/huggingface/transformers) to permit the latest version.
- [Release notes](https://github.com/huggingface/transformers/releases)
- [Commits](https://github.com/huggingface/transformers/compare/v4.0.0...v4.40.2)

---
updated-dependencies:
- dependency-name: transformers
  dependency-type: direct:production
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`06102ea`](https://github.com/qthequartermasterman/hypothesis-torch/commit/06102ea4bd0afddcd843ff72d5f76d321bb6eaad))

* chore(deps): bump dawidd6/action-download-artifact from 2.24.3 to 3.1.4

Bumps [dawidd6/action-download-artifact](https://github.com/dawidd6/action-download-artifact) from 2.24.3 to 3.1.4.
- [Release notes](https://github.com/dawidd6/action-download-artifact/releases)
- [Commits](https://github.com/dawidd6/action-download-artifact/compare/v2.24.3...v3.1.4)

---
updated-dependencies:
- dependency-name: dawidd6/action-download-artifact
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`48bc9e3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/48bc9e314b0d356eafd0dd14c31a5e1976f6a946))

### Ci

* ci: increase dependabot frequency ([`e44cd5f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e44cd5f45133d1d0915e4b1c12ccf8aa1cf8b000))

* ci: fix missing coverage comment by creating pytest-coverage.txt file during build ([`a8772c9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a8772c9abc14ab2a53aed3eb9c3c2c6beab97e52))

* ci: store hypothesis database in GitHub Actions to allow reproducing locally ([`fd62aca`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fd62acad596925d0ae58187767452df1bd6b9350))

### Unknown

* Merge pull request #39 from qthequartermasterman/dependabot/github_actions/main/dawidd6/action-download-artifact-3.1.4

chore(deps): bump dawidd6/action-download-artifact from 2.24.3 to 3.1.4 ([`a83b029`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a83b02982708af8abd9140fcca6e4a8b44a0d026))

* Merge pull request #43 from qthequartermasterman/dependabot/pip/main/mkdocs-material-9.5.22

chore(deps): bump mkdocs-material from 9.4.6 to 9.5.22 ([`2f10d4c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2f10d4cc86cf14a68ac0ecdaa03675234aa0dd06))

* Merge pull request #45 from qthequartermasterman/remove-upper-dependency-pin

build: remove upper pin on hypothesis and torch range ([`0d0d472`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0d0d472322f3c6e95eb0aa0bee51ff36c0856dbb))

* Merge pull request #44 from qthequartermasterman/dependabot/pip/main/ruff-0.4.4

chore(deps): bump ruff from 0.4.3 to 0.4.4 ([`8513f17`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8513f17d96af15b29dbb4dd841033a1fefee5d36))

* Merge pull request #41 from qthequartermasterman/dependabot/pip/main/transformers-gte-4.0.0-and-lte-4.40.2

chore(deps): update transformers requirement from &lt;=4.40.0,&gt;=4.0.0 to &gt;=4.0.0,&lt;=4.40.2 ([`7e9a01a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7e9a01a328c0bef7dd358aeb73404c9839276dca))

* Merge pull request #38 from qthequartermasterman/dependabot-update

ci: increase dependabot frequency ([`229887c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/229887c488c17d42a974d3b2b3856ee8f7175f2f))

* Merge pull request #37 from qthequartermasterman/fix-coverage-txt

ci: fix missing coverage comment by creating pytest-coverage.txt file during build ([`56eb109`](https://github.com/qthequartermasterman/hypothesis-torch/commit/56eb109a2648bd791db5501245d9e528b86043c2))

* Merge pull request #36 from qthequartermasterman/github-actions-database

ci: store hypothesis database in GitHub Actions to allow reproducing failures locally ([`0a2eb72`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0a2eb729015492d22369475cddafa55a5fe6cfc8))


## v0.6.3 (2024-05-12)

### Documentation

* docs: update pyproject toml classifiers, keywords, and urls. ([`e6d4a7c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e6d4a7c63921a097a8fc419c06c5483d4baa092c))

* docs(badges): :memo: Add pypi badges for downloads and version to readme ([`00563e6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/00563e65d7e652bc5bcc51ca185f8b05d908c352))

* docs(version): :memo: remove reference to python 3.8 in classifiers ([`03322e1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/03322e156f3c118ef10ea2d2395076088e5960d8))

### Fix

* fix: :bug: fix incompatible parameters when generating Adam optimizers on Torch 1.13.

Fix incompatible parameters:
- fused is only available if cuda is available
- fused is incompatible with differentiable ([`d0ef6bb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d0ef6bb44b935879864915c15496986afafc9375))

### Unknown

* Merge pull request #35 from qthequartermasterman/update-pyproject-toml

docs: update pyproject toml classifiers, keywords, and urls. ([`0d3a3ab`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0d3a3abcae3bef2bd7b8d7873a74867cbe6b2060))

* Merge pull request #34 from CandiedCode/badges ([`f166a9e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f166a9eebb26cbd76d75f973f98e940acf02785c))

* Merge pull request #33 from CandiedCode/version ([`f9ff580`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f9ff580bfe14369951a8fe93b3bb289338e1a3bc))


## v0.6.2 (2024-05-10)

### Build

* build: :bug: set dependency ranges for optimal compatability ([`4a25c1d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4a25c1dcd5e189df62ff8fe7fede4351447d415f))

### Unknown

* Merge pull request #32 from qthequartermasterman/set-dependencies-ranges

build: :bug: set dependency ranges for optimal compatibility ([`71c52b7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/71c52b79a1e58ff7ff2dfa9b388f74577112ee79))


## v0.6.1 (2024-05-10)

### Build

* build: :zap: remove unnecessary tee to avoid supressing error code ([`8716033`](https://github.com/qthequartermasterman/hypothesis-torch/commit/87160333a8ba121b710fedde3f29066e711e6c19))

* build: fix incorrect reusable workflow path ([`ec36fc6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ec36fc68b1a0acf62902623ca67983c1fc699914))

* build: test pytorch 1.13 in CI ([`6aff502`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6aff502b464bb3c5a43ca19acc4ff4854b104056))

* build: convert workflow to reusable workflow for simplicity ([`b1aa17a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b1aa17a70bd93c51f8c9f9f297741f53c90fcb00))

* build: :sparkles: :memo: Add readthedocs configuration. ([`95ffac5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/95ffac52292a6290ad5a2f418c0e11d40c9c1af3))

### Documentation

* docs: :sparkles: :memo: Add index page ([`510e3df`](https://github.com/qthequartermasterman/hypothesis-torch/commit/510e3dfedd2af3afae3b569183574ee223eb31f1))

* docs: :sparkles: :memo: Add strategies reference to docs. ([`8fc0d95`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8fc0d95d89b06191e5aaa9bf8214f9e92f3caca5))

* docs: :sparkles: :memo: Add compatability guide to docs. ([`ca3bada`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ca3badae4a2096f2ab84373c7118452cd4626e20))

* docs: :sparkles: :memo: Disable top tabs on docs. ([`53164a2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/53164a2febb25f86630e2b26e27f01a941bfa8e1))

* docs: :sparkles: :memo: Add quick start guide to docs. ([`2710504`](https://github.com/qthequartermasterman/hypothesis-torch/commit/27105049976e83a024af4cb5d1c6d8314005cf7f))

* docs: :sparkles: :memo: Add quick start guide to docs. ([`a59871c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a59871c2755088c9954384bdca7e395a51f71868))

* docs: :sparkles: :memo: Add contribuging guidelines to docs. ([`3f30767`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3f3076763b50de5a4c663faed4113490cb8d5ad2))

* docs: :sparkles: :memo: Add changelog to docs. ([`05dc054`](https://github.com/qthequartermasterman/hypothesis-torch/commit/05dc05400bcf4c7b8d0da34822bd67b8150e67e6))

* docs: :sparkles: :memo: Add changelog to docs. ([`ddb9598`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ddb95980bb5e9fda47af72977fcd33b1954be122))

* docs: :sparkles: :memo: Add license file to docs. ([`06adb42`](https://github.com/qthequartermasterman/hypothesis-torch/commit/06adb42eaf466688b97878daf2395cb957536fee))

* docs: :sparkles: Initial docsite set up. ([`274bb65`](https://github.com/qthequartermasterman/hypothesis-torch/commit/274bb6512912fab817c71f394a3ccfad124de625))

### Fix

* fix: :bug: do not try to use the device as a context manager in torch&lt;2. ([`3114162`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3114162fb77ed48ecb5d980b4e2b41c6184bc3ae))

* fix: :bug: do not try to use the meta device as a context manager in torch&lt;2. ([`ef0e47c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ef0e47c20a65606400b1335902417db0c88f0f79))

* fix: :zap: remove overly-restrictive hypothesis deadline for transformers tests ([`d1c89f2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d1c89f2dceed4132dc363b63b1b27a75bd191d87))

### Test

* test: :bug: ignore runtime errors during module import ([`882f515`](https://github.com/qthequartermasterman/hypothesis-torch/commit/882f5156d4ceb9b7533dd8d10b2a854c0af2e472))

* test: :bug: ignore runtime errors during module import ([`5c89c79`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5c89c79ffedb88a5b9dce24a4cdbbf4354b7a82d))

### Unknown

* Merge pull request #31 from qthequartermasterman/test-multiple-torch-versions

build: Test multiple torch versions ([`4ecabd9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4ecabd99dd5c3c1cdcd8df1b1199b6e89a2bf0f4))

* Merge pull request #29 from qthequartermasterman/docsite

docs: :sparkles: :memo: Add index page ([`46e3516`](https://github.com/qthequartermasterman/hypothesis-torch/commit/46e35169566eb5c8143edeed9f8169be39b751d2))

* Merge pull request #28 from qthequartermasterman/docsite

docs: Add support for docs rendered by `readthedocs`, powered by `mkdocs`. ([`e8de564`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e8de564122265d25686bd7504d4b1b2069b54ac5))


## v0.6.0 (2024-05-09)

### Unknown

* Merge pull request #18 from qthequartermasterman/optimizers

feat: :sparkles: add strategies for torch optimizers ([`fbefa06`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fbefa069ceea8ce997306239ae9fff43cfbffa4b))

* Merge branch &#39;main&#39; into optimizers ([`4eb2f4d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4eb2f4dd9017aca36895efd51fbf22b3e75bea30))


## v0.5.0 (2024-05-09)

### Build

* build: 🔧 add py.typed ([`bef3985`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bef3985b6747e29f18ed45e7984945a6767190a9))

### Chore

* chore(deps): bump pytest from 8.1.1 to 8.2.0

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.1.1 to 8.2.0.
- [Release notes](https://github.com/pytest-dev/pytest/releases)
- [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst)
- [Commits](https://github.com/pytest-dev/pytest/compare/8.1.1...8.2.0)

---
updated-dependencies:
- dependency-name: pytest
  dependency-type: direct:production
  update-type: version-update:semver-minor
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`75fd127`](https://github.com/qthequartermasterman/hypothesis-torch/commit/75fd127ec1fcbb64a95eb82dc0ae03e7faeee3fc))

* chore(deps): bump ruff from 0.4.1 to 0.4.3

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.4.1 to 0.4.3.
- [Release notes](https://github.com/astral-sh/ruff/releases)
- [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md)
- [Commits](https://github.com/astral-sh/ruff/compare/v0.4.1...v0.4.3)

---
updated-dependencies:
- dependency-name: ruff
  dependency-type: direct:production
  update-type: version-update:semver-patch
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`c7e5d8d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c7e5d8d0c611a03dd03a8cc6373e4992e709919b))

### Fix

* fix: :label: fix incorrect decorator typing ([`3e80d6a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3e80d6a0f71b6cde8f539150bffffe9ee338253b))

* fix: :white_check_mark: designate officially supported versus unofficially supported transformers.

By default, only officially supported transformer types are tested in CI, but unofficially supported transformers MAY or MAY NOT be compatible with the `transformer_strategy`. A test fully parametrized over ALL of the model types in `transformers` is available, and can be enabled when setting the environment variable `HYPOTHESIS_TORCH_TEST_UNSUPPORTED_TRANSFORMERS=True`. ([`7d22190`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7d22190766613db31a220b0cda54bb79d73cc6b1))

### Test

* test: ignore import errors while inferring available transformers in tests. ([`84185cb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/84185cb66fcec5f50aad09e38b0026624ca5862a))

* test:  disable deadline for occasionally slow tests ([`34ae9db`](https://github.com/qthequartermasterman/hypothesis-torch/commit/34ae9db1d2ef05433c87a25a4d17aa224c67b4ff))

### Unknown

* Merge pull request #19 from qthequartermasterman/transformers-tests

feat: :sparkles: add support for more transformers strategies ([`964a70f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/964a70f0ea027286cc614cf963e764e3bcbdbffa))

* Merge branch &#39;main&#39; into transformers-tests ([`aa6f06e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/aa6f06e242fbe5008c6e070b48099524eead0919))

* Merge pull request #23 from qthequartermasterman/dependabot/pip/main/pytest-8.2.0

chore(deps): bump pytest from 8.1.1 to 8.2.0 ([`a55308b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a55308be3956fe9de7aa39a48deacecc0121bc2a))

* Merge pull request #26 from qthequartermasterman/dependabot/pip/main/ruff-0.4.3

chore(deps): bump ruff from 0.4.1 to 0.4.3 ([`2ae1ae5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2ae1ae54a369912845a76b2cc7dfb3e94c769539))

* Merge pull request #25 from ringohoffman/py.typed

build: 🔧 add py.typed ([`b2e8557`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b2e8557d8b8b0f0263ba19a68409fbd719830136))


## v0.4.3 (2024-04-28)

### Fix

* fix: :bug: do not generate inf values if elements has infinity disabled for bfloat16 tensors.

Before, if a float strategy that prevented infinities was provided to as `elements` to `tensor_strategy`, the resultant tensor could still occasionally have infinities because the strategy would generate float32 values that exceeded the maximium/minimum values for bfloat16. ([`cda8577`](https://github.com/qthequartermasterman/hypothesis-torch/commit/cda8577aebf2bed7d8c86a8e5ac1c1d19d5cd57c))

### Unknown

* Merge pull request #21 from qthequartermasterman/fix-bfloat16-infinities

fix: :bug: do not generate inf values if elements has infinity disabled for bfloat16 tensors. ([`8398018`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8398018f7c5bd18307eafb7b8f30ffff044d6e64))


## v0.4.2 (2024-04-27)

### Feature

* feat: :sparkles: add support for more transformers strategies ([`7ac7508`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7ac75088956adf3ec5b06b9352d6ed7c0492ad59))

* feat: :sparkles: add strategies for torch optimizer types and torch optimizer instances

NOTE: The strategy for torch optimizers actually generates an &#34;alternate constructor&#34; for a torch optimizer that takes in only a torch module&#39;s parameters. The strategy will &#34;pre-fill&#34; all of the hyperparameters. If these hyparameters should be overridden, they can be specified as kwargs in the strategy. ([`5cf6181`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5cf6181ef6617eda19eb0b51658f835280421c63))

### Fix

* fix: :bug: do not generate inf values if elements has infinity disabled for float16 and float32 tensors.

This fix does not work for all bfloat16 tensors. ([`8e9eb5d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8e9eb5daf6f94e121ad6554bb1a41fcd73ac8da0))


## v0.4.1 (2024-04-24)

### Fix

* fix: mark bfloat16 as a floating dtype ([`38b4ed3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/38b4ed3425439525848375a5bd200786d3dfd236))

### Unknown

* Merge pull request #17 from qthequartermasterman/register-random-state

fix: mark bfloat16 as a floating dtype ([`57c0a5b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/57c0a5b1c0904c65f6deca1855b2708ea7f94944))


## v0.4.0 (2024-04-24)

### Feature

* feat: register random torch state as a hypothesis entry point (so that torch state is always registered, even if hypothesis-torch is never imported). ([`eada00a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/eada00a8beb3632799a83256a2b24c3a4faa070b))

* feat: register random torch state with hypothesis ([`633bf82`](https://github.com/qthequartermasterman/hypothesis-torch/commit/633bf82aa3873452dbb674f7f0b18b8a378a3027))

### Unknown

* Merge pull request #16 from qthequartermasterman/register-random-state

feat: Register PyTorch&#39;s random state with Hypothesis so that torch random is deterministic during testing ([`4d957a1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4d957a1a0ca51c92bb997265b53b94b0124aa005))

* Update issue templates ([`c7648bf`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c7648bf89b6bdb299f9191becfc47d2d998e56dd))


## v0.3.1 (2024-04-24)

### Fix

* fix: :truck: move test to test folder ([`e7460f7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e7460f7d11a84cc0a4791b90c02932505399bd5d))

### Test

* test: ignore coverage on pairwise. ([`0cec9ba`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0cec9baf36cfcb2fbd9d8f10abd5663237887b2e))

### Unknown

* Merge pull request #5 from qthequartermasterman/more-tensor-attributes

ci: coverage report ([`e04916e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e04916edd7f5c4a8c48bcdbf93fa0d5bdf789bfc))


## v0.3.0 (2024-04-24)

### Ci

* ci: coverage report ([`36b8eb9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/36b8eb909fdd266b8469ccd3a2c162ebf1310af1))

* ci: coverage report ([`3f80154`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3f8015442c1244f4b127d7bf98b6e8d07eae77d3))

* ci: use faster ci settings ([`e36cca7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e36cca712d76ed5583424868e9b0cb04f5855794))

### Feature

* feat: :sparkles: add pin_memory to tensor generation ([`dc42447`](https://github.com/qthequartermasterman/hypothesis-torch/commit/dc42447ec057ac7bc1939c1491fdd53c9e9bece2))

* feat: :sparkles: add requires_grad to tensor generation ([`51bda34`](https://github.com/qthequartermasterman/hypothesis-torch/commit/51bda34b0e33f71708e43279969908dbe656be87))

* feat: :sparkles: allow tensor strategy to sample over layout and memory format ([`af02d54`](https://github.com/qthequartermasterman/hypothesis-torch/commit/af02d542d84049c9ece7c738799c9472b8332c44))

* feat: :sparkles: add layout argument to tensor strategy ([`a77069c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a77069cc8502f15c69b46fd16a92926645b4e9b5))

* feat: :sparkles: add strategies for layout and memory format ([`153fa0b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/153fa0bd49c51c04c31784cbb83dd42e1f41dbe9))

### Refactor

* refactor: :recycle: rename global private constant ([`3fcfac6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3fcfac64d9ccbe4cda70d1fc1ad2caa8af539bf0))

* refactor: :recycle: improve typing to enforce global constants ([`c46f53c`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c46f53c86e3b9cfffb609a18a9d21e744002e91b))

### Test

* test: :white_check_mark: unit tests for scalar tensors ([`9f543d6`](https://github.com/qthequartermasterman/hypothesis-torch/commit/9f543d63b09def247bc1ca56b7089d977a1c79f1))

### Unknown

* Merge pull request #4 from qthequartermasterman/more-tensor-attributes

feat: :sparkles: More tensor attributes ([`c421dae`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c421daec6758123395582b999a338fccf21b8685))


## v0.2.0 (2024-04-23)

### Ci

* ci: set hypothesis profile ([`bfecac5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bfecac520ad961687a258626a1b61d3220e6e150))

### Documentation

* docs: :label: improve typing ([`0bd9170`](https://github.com/qthequartermasterman/hypothesis-torch/commit/0bd917036cd11d09fc4da21fd18fc857cc950dca))

* docs: update root docstring ([`2f9395f`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2f9395f7749a2914dc586471e8fe3d86fd3904f5))

### Feature

* feat: :recycle: :sparkles: allow overriding examples of activation functions ([`3746915`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3746915c9068da28ce6893dd8b2c1f407bd2db42))

* feat: add available dtypes and device sets to root imports ([`91f8ea3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/91f8ea3df5de2e1a16dc5571fc8ee0d5630ff40b))

### Refactor

* refactor: :zap: :recycle: do not define dtype_strategy as as composite strategy to avoid overhead ([`e47ea82`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e47ea82aabba12f4a7e16865829e6b2ec3b59a2f))

* refactor: :zap: :recycle: do not define device_strategy as as composite strategy to avoid overhead ([`221d72a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/221d72a99dc3ca40a6cec3800a12833026dc46d2))

### Test

* test: :fire: remove redundant type hints ([`bcf95c4`](https://github.com/qthequartermasterman/hypothesis-torch/commit/bcf95c4b21f11cccc38fa9e593fa391ad47bd645))

* test: :white_check_mark: unit tests for activation strategy ([`dfa900e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/dfa900e47bf90d4cdfa4e278d6bd9ae928307aa2))


## v0.1.10 (2024-04-23)

### Ci

* ci: set hypothesis profile ([`c2aae43`](https://github.com/qthequartermasterman/hypothesis-torch/commit/c2aae43546887810aca3b64965d99f93857f2887))

### Fix

* fix: only generate sensible floats and integer values for the given dtype ([`8175a73`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8175a73bce4888a546215517145c0b85d5b4624d))

### Unknown

* Merge pull request #3 from qthequartermasterman/dependabot/github_actions/main/actions/setup-python-5

chore(deps): bump actions/setup-python from 2 to 5 ([`68e0892`](https://github.com/qthequartermasterman/hypothesis-torch/commit/68e08926025565124d3bf5e58883656b9bec9a89))


## v0.1.9 (2024-04-22)

### Chore

* chore(deps): bump actions/setup-python from 2 to 5

Bumps [actions/setup-python](https://github.com/actions/setup-python) from 2 to 5.
- [Release notes](https://github.com/actions/setup-python/releases)
- [Commits](https://github.com/actions/setup-python/compare/v2...v5)

---
updated-dependencies:
- dependency-name: actions/setup-python
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`ad754e1`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ad754e1d75f802ef21fbec3ab4e0e74f9fc043cf))

* chore(deps): bump stefanzweifel/git-auto-commit-action from 4 to 5

Bumps [stefanzweifel/git-auto-commit-action](https://github.com/stefanzweifel/git-auto-commit-action) from 4 to 5.
- [Release notes](https://github.com/stefanzweifel/git-auto-commit-action/releases)
- [Changelog](https://github.com/stefanzweifel/git-auto-commit-action/blob/master/CHANGELOG.md)
- [Commits](https://github.com/stefanzweifel/git-auto-commit-action/compare/v4...v5)

---
updated-dependencies:
- dependency-name: stefanzweifel/git-auto-commit-action
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`77dcfa5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/77dcfa5cda44125a738f7338338c823e9c708d04))

* chore(deps): bump actions/checkout from 3 to 4

Bumps [actions/checkout](https://github.com/actions/checkout) from 3 to 4.
- [Release notes](https://github.com/actions/checkout/releases)
- [Changelog](https://github.com/actions/checkout/blob/main/CHANGELOG.md)
- [Commits](https://github.com/actions/checkout/compare/v3...v4)

---
updated-dependencies:
- dependency-name: actions/checkout
  dependency-type: direct:production
  update-type: version-update:semver-major
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt; ([`1409079`](https://github.com/qthequartermasterman/hypothesis-torch/commit/140907957ed24f6adf196c9a4a0b01cb3ab9fe5f))

### Ci

* ci: enable dependabot ([`42524ee`](https://github.com/qthequartermasterman/hypothesis-torch/commit/42524eef2f96134d6a8a4103925adc271460a15c))

* ci: enable dependabot ([`1e63f06`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1e63f06f995c1e329aa89ffefe73e09ca37254a7))

### Fix

* fix: only generate sensible floats for Softplus threshold ([`6d81c89`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6d81c89f516688fae34bedcb5a5254db11de92d5))

### Style

* style: ruff ([`7d94775`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7d947759e6655052e39d6753deb881080db0e643))

### Test

* test: :white_check_mark: unit tests for linear strategy ([`5dbfe6e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5dbfe6e618acc4aea31d2a81419f1736509bfd01))

### Unknown

* Merge pull request #2 from qthequartermasterman/dependabot/github_actions/main/stefanzweifel/git-auto-commit-action-5

chore(deps): bump stefanzweifel/git-auto-commit-action from 4 to 5 ([`37675d3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/37675d39951428c4e83cf70f6c3de0e5461b0a84))

* Merge pull request #1 from qthequartermasterman/dependabot/github_actions/main/actions/checkout-4

chore(deps): bump actions/checkout from 3 to 4 ([`ba59e35`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ba59e3512632d77fd6f1b134d829130552929896))


## v0.1.8 (2024-04-22)

### Chore

* chore: pre-commit configuration ([`2c8efaa`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2c8efaa03c87a56cb3483fc1f07ca080b598ddd5))

### Ci

* ci: fix github actions ([`1b6d8b2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1b6d8b29b460579730954210fbb221db200a53d7))

* ci: fix github actions ([`a3abe85`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a3abe8564863bf5818fecc900b538d647051d528))

* ci: add PR build ([`3284a11`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3284a1168e75bb33f95a119406d1c73a85c28d26))

### Fix

* fix: only mark MPS devices as available if MPS itself is available ([`d277350`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d277350ff3de4d359011a8b234aef5beff227880))

### Style

* style: :rotating_light: ruff ([`8912c96`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8912c96eaa5e96e8b5d117989030e7c763ee4702))

* style: :rotating_light: ruff ([`6599c7d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6599c7d062c6eeaa09fcab5b5cdd64f8f1fe29c0))

* style: :rotating_light: ruff format ([`97f6e6e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/97f6e6e31f564442b9384b60717e0c1dc030fcc2))

### Test

* test: :white_check_mark: unit tests for tensors ([`50da775`](https://github.com/qthequartermasterman/hypothesis-torch/commit/50da77539f9d4d30165d6f136d46518b7991b00d))

* test: :white_check_mark: unit tests for iterable utils ([`f262c89`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f262c8936ac1dfc7b2d4b082d5478ad5111a3bf2))


## v0.1.7 (2024-04-21)

### Ci

* ci: use deploy key to bypass branch protection ([`22dd442`](https://github.com/qthequartermasterman/hypothesis-torch/commit/22dd442de7435f78eac1d7b6fddb3ecf8b6d67f6))

* ci: use uv to install requirements ([`a87ef0a`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a87ef0a45fe74478f1a996ed1dd0883d00ab5bc9))

* ci: use uv to install requirements ([`3d4a0b0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3d4a0b02c31dd04f6f3c9a3bec946c81dab83f01))

### Fix

* fix: :label: typing fixes ([`a03d697`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a03d6979d47f9b2bd5c4a8328e9b1927fdc96339))


## v0.1.6 (2024-04-21)

### Fix

* fix: semantic release reference in pyproject toml ([`7fe09c9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/7fe09c9da9dcdb9d746ad08717870e6b43ecfa88))


## v0.1.5 (2024-04-21)

### Fix

* fix: clean up imports ([`fc93cd5`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fc93cd5b56f605713272085329bbb5fcd1134f3d))


## v0.1.4 (2024-04-21)

### Fix

* fix: build command and dynamic version for setuptools ([`cd1889d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/cd1889dd687904b1f8a1a946bdf41f2d17ac6c0f))


## v0.1.3 (2024-04-21)

### Fix

* fix: allow manually launching release ([`f651484`](https://github.com/qthequartermasterman/hypothesis-torch/commit/f651484d092ce20e4d93c3406309069e5c551af9))


## v0.1.2 (2024-04-21)

### Fix

* fix: upload to pypi using semantic release ([`98ac240`](https://github.com/qthequartermasterman/hypothesis-torch/commit/98ac24014307ca8ac6e14170652fd4448228ccd8))


## v0.1.1 (2024-04-21)

### Ci

* ci: publish to pypi ([`6d3bd54`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6d3bd54eaf0dc12ff705e6f3847e25c27bacb8d1))

### Fix

* fix: fix semantic release settings ([`b702e85`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b702e85e319324a2904f73a003121aa7bd6ffd6d))


## v0.1.0 (2024-04-21)

### Chore

* chore: specify optional dependencies ([`fe1b34e`](https://github.com/qthequartermasterman/hypothesis-torch/commit/fe1b34ea1dd58c8bd637b678a3901cde811ef0fa))

* chore: typing ([`8b184e0`](https://github.com/qthequartermasterman/hypothesis-torch/commit/8b184e0fa72dda66c75cbfe31929869e3cfebfd6))

* chore: set optional dependencies ([`64547b3`](https://github.com/qthequartermasterman/hypothesis-torch/commit/64547b3cb5a7219aef3871e3d68eabcbcecb4b74))

* chore:  pyproject toml ([`a1bfdaa`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a1bfdaa067915518600cdc5d187c8a2d75c346b5))

### Ci

* ci:  fix master-&gt;main incorrectly named workflow branch ([`a110bd9`](https://github.com/qthequartermasterman/hypothesis-torch/commit/a110bd9f557fef5271f534d909cfa8f384281466))

* ci: semantic relase ([`5febe77`](https://github.com/qthequartermasterman/hypothesis-torch/commit/5febe77ae294bd5cc42d52729fdfebb964fab759))

### Documentation

* docs: :memo: write first README draft ([`1c5e799`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1c5e79981719887191868432d82aa6ea091fe544))

### Feature

* feat: modify linear network strategy api ([`4c7d831`](https://github.com/qthequartermasterman/hypothesis-torch/commit/4c7d831f7b1d61383da5b1254ea44fb897c4732a))

* feat: import transformer strategy into root if and only if transformers is installed ([`b314203`](https://github.com/qthequartermasterman/hypothesis-torch/commit/b3142037e069fad2f4a659296c350558a58e9fd7))

* feat: import strategies into the root ([`eaa7a78`](https://github.com/qthequartermasterman/hypothesis-torch/commit/eaa7a78d5a8fdcccc35f577c33d4b50516d9efcb))

* feat: generate modules ([`ad8f103`](https://github.com/qthequartermasterman/hypothesis-torch/commit/ad8f103e7b4f3b2608f0b12f7068c63f7b1903ef))

* feat: inspection_util.py ([`1d22dc8`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1d22dc8b927dba4ec5b301503f791aef4a64ffe5))

* feat: generate hugging face transformers ([`74a1ae2`](https://github.com/qthequartermasterman/hypothesis-torch/commit/74a1ae2f25afde8a676401dd3e65d3a8f43c6d54))

* feat: generate tensors ([`e9785d7`](https://github.com/qthequartermasterman/hypothesis-torch/commit/e9785d78c4d68e4fd0e80591319a5b3934031b5e))

* feat: dtype strategies ([`723f096`](https://github.com/qthequartermasterman/hypothesis-torch/commit/723f096bc36164f09cc6662fccb56e2bc2ae3f8b))

* feat: device strategies ([`1acab83`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1acab833ea64a71aedf134879ec07a9270a96b88))

### Fix

* fix: add urls ([`6c8dd3d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/6c8dd3d72463e133ec5695e38d0f590e694d9f50))

* fix: allow `unique` to be a strategy ([`50bedeb`](https://github.com/qthequartermasterman/hypothesis-torch/commit/50bedeba2f54b1333fa38ccc06abe5010ab8f6ec))

* fix: rename parameter ([`1df242d`](https://github.com/qthequartermasterman/hypothesis-torch/commit/1df242dcc8f6ac3ea589f74614e942cd7b59bf18))

### Style

* style: :rotating_light: ruff ([`d653c6b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/d653c6b8a2291a150d192f14c2b3f2f385828cc4))

* style: :rotating_light: ruff ([`3d4efaa`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3d4efaa4c44b235e33a8f7942d72f72eb733ff27))

* style:  :rotating_light: ruff ([`2d4f14b`](https://github.com/qthequartermasterman/hypothesis-torch/commit/2d4f14b39ab4341bfdb39df48c51a513100aaf1c))

### Test

* test: update device test ([`74e9b90`](https://github.com/qthequartermasterman/hypothesis-torch/commit/74e9b90ff5d5847b3ea861940518b8458a160e2c))

### Unknown

* Initial commit ([`3935397`](https://github.com/qthequartermasterman/hypothesis-torch/commit/3935397d4c954855f855dc6281476063fd620e23))
