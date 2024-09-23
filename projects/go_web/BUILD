load("@io_bazel_rules_go//go:def.bzl", "go_binary")

go_binary(
    name = "main",
    srcs = ["main.go"],
    deps = [ "//projects/go_hello_world:hello_world",
    "@com_github_gorilla_mux//:mux"
    ]
)