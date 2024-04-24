# CHANGELOG



## v0.3.0 (2024-04-24)

### Ci

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
