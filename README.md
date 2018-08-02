# Distroless: python2.7 SSL root certificate bug

Distroless's base image used to have an incorrect OpenSSL configuration that was fixed with the following bug: https://github.com/GoogleCloudPlatform/distroless/issues/155

Unfortunately as of 2018-08-02, `rules_docker` has not been updated to include this fix. See: https://github.com/bazelbuild/rules_docker/issues/477

* Test the default `rules_docker` `py_image` rule: `bazel run :fetch_image`
* Test the most recent (as of 2018-08-02) `distroless/python2.7` image: `bazel run :fetch_with_latest_distroless`
* Test the default `rules_docker` `py_image` rule with the environment fix: `bazel run :fetch_with_env`
