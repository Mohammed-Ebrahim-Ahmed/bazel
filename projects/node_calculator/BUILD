load("@npm//@bazel/jasmine:index.bzl","jasmine_node_test") 

filegroup(
    name= "node_calculator",
    srcs= ["calculator.js"],
    visibility = ["//visibility:public"]
)

jasmine_node_test(
    name = "calculator_test",
    srcs = ["calculator.spec.js"],
    data = [":node_calculator"]
)