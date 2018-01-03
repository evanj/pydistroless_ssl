git_repository(
    name = "io_bazel_rules_docker",
    remote = "https://github.com/bazelbuild/rules_docker.git",
    commit = "5f58b022f191722d5771636478691ed13346b3ee",
)

# load(
#     "@io_bazel_rules_docker//container:container.bzl",
#     "container_pull",
#     container_repositories = "repositories",
# )

# # This is NOT needed when going through the language lang_image
# # "repositories" function(s).
# container_repositories()

# container_pull(
#   name = "python_base",
#   registry = "gcr.io",
#   repository = "distroless/python2.7",
#   # 'tag' is also supported, but digest is encouraged for reproducibility.
#   digest = "sha256:deadbeef",
# )

load(
    "@io_bazel_rules_docker//python:image.bzl",
    _py_image_repos = "repositories",
)

_py_image_repos()

# Specific Debian packages we want to add
http_file(
  name="libc_bin",
  url="http://http.us.debian.org/debian/pool/main/g/glibc/libc-bin_2.24-11+deb9u1_amd64.deb",
  sha256="1908a1b6092a0681e914bc02d5b52bceebb48d8e40203f97ae8cedf80694fd6f",
)

http_file(
  name="dash",
  url="http://http.us.debian.org/debian/pool/main/d/dash/dash_0.5.8-2.4_amd64.deb",
  sha256="5084b7e30fde9c51c4312f4da45d4fdfb861ab91c1d514a164dcb8afd8612f65",
)

http_file(
  name="strace",
  url="http://http.us.debian.org/debian/pool/main/s/strace/strace_4.15-2_amd64.deb",
  sha256="cf706ecb2c28692be056b31cbeef441dbf83e453a70c3a7a281fa0311ee28930",
)