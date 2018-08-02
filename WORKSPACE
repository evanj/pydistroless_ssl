git_repository(
    name = "io_bazel_rules_docker",
    remote = "https://github.com/bazelbuild/rules_docker.git",
    commit = "17805d11cf07c4390b24a09f3476fb264b5f20ad",
)

load(
    "@io_bazel_rules_docker//container:container.bzl",
    "container_pull",
    container_repositories = "repositories",
)

# This is NOT needed when going through the language lang_image
# "repositories" function(s).
container_repositories()

container_pull(
  name = "recent_python_base",
  registry = "gcr.io",
  repository = "distroless/python2.7",
  # 'tag' is also supported, but digest is encouraged for reproducibility.
  digest = "sha256:7a375215e39b12d64ff77d816f84f50dd972bfe4658c697bf6ef5f242ea69201",
)

load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()
