cmake_minimum_required(VERSION 3.31)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)
include($ENV{PICO_SDK_PATH}/external/pico_sdk_import.cmake)

project(pico-usb-switch)
set(CMAKE_C_STANDARD 11)
pico_sdk_init()

add_executable(pico-usb-switch usb_switch_controller.c)

target_link_libraries(pico-usb-switch pico_stdlib)

pico_add_extra_outputs(pico-usb-switch)

