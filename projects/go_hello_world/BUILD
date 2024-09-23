load("@io_bazel_rules_go//go:def.bzl", "go_library", "go_test")

go_library(
    name = "hello_world",
    srcs = [
        "hello_world.go"
    ],
    importpath = "github.com/Mohammed-Ebrahim-Ahmed/bazel/projects/go_hello_world",
    visibility = ["//visibility:public"]
)

go_test(
    name = "hello_world_test",
    srcs = [
        "hello_world_test.go"
    ],
    embed = [":hello_world"]

)