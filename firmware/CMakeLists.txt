cmake_minimum_required(VERSION 3.13...3.27)

# initialize pico-sdk from submodule
# note: this must happen before project()
include(pico-sdk/pico_sdk_init.cmake)

project(usb-switcher)

# initialize the Raspberry Pi Pico SDK
pico_sdk_init()

# rest of your project
