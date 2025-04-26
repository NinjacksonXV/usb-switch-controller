import os
from os.path import realpath

# https://www.usb.org/defined-class-codes#anchor_BaseClass09h
HUB_CLASS = "09"
HUB_SUBCLASS = "00"

class SysUsbDevice:
    """*DEPRECATED*
    A USB device as described in /sys/bus/usb/devices. Contains parameters equivalent to the files found in a given device directory.
    """
    
    def __init__(self, basename: str):
        self.basename = basename
        self.child_paths = []
        for filename in os.listdir(os.path.join("/sys/bus/usb/devices", basename)):
            file_path = os.path.join("/sys/bus/usb/devices/", basename, filename)
            if os.path.isdir(file_path) and basename in filename:
                self.child_paths.append(file_path)
            if os.path.isfile(file_path) and os.access(file_path, os.R_OK):
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    setattr(self, filename, f.read().rstrip())
    basename: str
    child_paths: list[str]

    configuration: str
    uevent: str
    bos_descriptors: str
    bMaxPacketSize0: str
    bDeviceClass: str
    bcdDevice: str
    bNumInterfaces: str
    bConfigurationValue: str
    manufacturer: str
    bNumConfigurations: str
    authorized: str
    descriptors: str
    dev: str
    speed: str
    idProduct: str
    urbnum: str
    devnum: str
    product: str
    maxchild: str
    bmAttributes: str
    bDeviceSubClass: str
    bMaxPower: str
    rx_lanes: str
    removable: str
    idVendor: str
    version: str
    avoid_reset_quirk: str
    remove: str
    bDeviceProtocol: str
    tx_lanes: str
    ltm_capable: str
    devpath: str
    busnum: str
    quirks: str

def get_block_devices_under_hub(hub_path):
    block_base = '/sys/block/'
    devices = []

    for block_dev in os.listdir(block_base):
        device_path = os.path.join(block_base, block_dev, 'device')
        if not os.path.islink(device_path):
            continue
        
        real_path = os.path.realpath(device_path)  # resolves symlinks
        
        if [p for p in real_path.split('/') if p.startswith(hub_path)]:
            devices.append(f'/dev/{block_dev}')

    return devices

def get_all_usb_hubs() -> list[list[SysUsbDevice]]:
    hubs: list[list[SysUsbDevice]] = []

    for file in os.listdir("/sys/bus/usb/devices/"):
        if 'usb' in file: # Filters out redundant symlinks 
            continue
        device = SysUsbDevice(file)
        try:
            if device.bDeviceClass == HUB_CLASS and device.bDeviceSubClass == HUB_SUBCLASS:
                unique_hub = True
                for hub in hubs:
                    for sub_hub in hub:
                        if sub_hub.bcdDevice == device.bcdDevice:
                            hub.append(device)
                            unique_hub = False
                            break
                    if unique_hub == False:
                        break
                if unique_hub:
                    hubs.append([device])
        except:
            continue
    return hubs 

def print_hub_tree(hubs: list[list[SysUsbDevice]]) -> None:
    for hub in hubs:
        hub.sort(key=lambda x: x.basename)
    hubs.sort(key=lambda x: x[0].basename)
    
    for hub in hubs:
        for subhub in hub:
            print(subhub.basename)
            for path in subhub.child_paths:
                if not any(path == sub_device for sub_device in subhub.child_paths):
                    device = SysUsbDevice(path)
                    print(device.basename)
