
load("@build_bazel_rules_nodejs//:index.bzl", "nodejs_binary")

nodejs_binary(
    name = "node_web",
    data = [
        "//projects/node_calculator:node_calculator",
        "@npm//express:express"
    ],
    entry_point = ":main.js",
)