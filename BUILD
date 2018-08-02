load("@io_bazel_rules_docker//python:image.bzl", "py_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_image")

py_binary(
	name="fetch",
	srcs=["fetch.py"]
)

py_image(
	name="fetch_image",
	srcs=["fetch.py"],
	main="fetch.py",
)

container_image(
    name="distroless_with_env",
    base="@py_image_base//image",
    env={'SSL_CERT_FILE': '/etc/ssl/certs/ca-certificates.crt'},
)

# Works!!!
py_image(
    name = "fetch_with_env",
    srcs = ["fetch.py"], 
    main = "fetch.py",
    base = ":distroless_with_env",
)

py_image(
	name = "fetch_with_latest_distroless",
	srcs = ["fetch.py"],
	main = "fetch.py",
	base = "@recent_python_base//image")
