load("@my_deps//:requirements.bzl", "requirement")
load("@io_bazel_rules_docker//python3:image.bzl", py_image= "py3_image")
load("@io_bazel_rules_docker//container:container.bzl", "container_push")

py_binary(
    name = "main",
    srcs = ["main.py"],
    deps = [
        "//projects/calculator:calculator", 
        requirement("Flask")
    ],
    main = "main.py"
)

py_image(
    name = "docker_main",
    srcs = ["main.py"],
    deps = [
        "//projects/calculator:calculator",
        requirement("Flask")
    ],
    main = "main.py"
)

container_push(
   name = "publish",
   image = ":docker_main",
   format = "Docker",
   registry = "index.docker.io",
   repository = "mohammedebrahim/flask_repo",
   tag = "v0.1",
)