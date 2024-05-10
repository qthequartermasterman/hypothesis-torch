# Compatability

## `hypothesis-torch` Release Policy

`hypothesis-torch` prefers backwards compatibility over backporting fixes, so we use
[Python Semantic Release](https://python-semantic-release.readthedocs.io/en/latest/) to manage versioning.
When new commits are made to the `main` branch, the version number is automatically updated based on the
types of changes made. Consequently, we generally only support the most recent version of `hypothesis-torch`.

Because we use [Trunk-based Development](https://trunkbaseddevelopment.com/), all releases are made directly from
`main`, which is always considered stable and in a releasable state. We do not have a separate `develop` branch or 
release branches (though every release corresponds to a tagged commit).

Documented APIs will not break except between major version bumps. Unless specifically noted, all documented APIs are 
considered public and stable.

!! warning
    
    During the current initial development phase (i.e. before the first major release), we may make breaking changes
    without bumping the major version number. This disclaimer will be removed once version 1.0.0 is released.

## `hypothesis` and `torch` Versions

In theory, `hypothesis-torch` should work with `hypothesis>=6.0.0` and `torch>=2.0.0`. However, because neither 
`hypothesis` nor `torch` support older versions, we do not currently test against old versions. In our CI, we test 
against the latest versions of `hypothesis` and `torch`. 

## Python Versions

`hypothesis-torch` is regularly tested in CI on CPython 3.9+.

Generally, we only officially support the latest patch version of each minor release of Python, but `hypothesis-torch`
should work on any version of Python 3.9 or later.

## Operating systems

`hypothesis-torch` is regularly tested in CI on Linux. It also is regularly tested locally on macOS, though this is not
currently part of our CI pipeline. We do not currently test on Windows, but we believe it should work there as well.

## Testing frameworks

`hypothesis-torch` is compatible with all testing frameworks that `hypothesis` supports. See the
[`hypothesis` docs]([Trunk-based Development](https://trunkbaseddevelopment.com/)) for more details.
