# This whole thing is dependent on the drive paths found in `/dev/disk/by-path/`, which look like `pci-0000:00:14.0-usb-0:1.1.3:1.0-scsi-0:0:0:0`; the part we care about is the `1.1.3`, which is the "port path" for a given hub (not including the root port). 

# We're using string manipulation and parsing for this. In theory, if you had 10 or more USB ports, this would break; anything targeting string slices will need to be reworked later. I'm very tired.

# It's recommended not to use it in most circumstances because it's better to address by other identifiers, but here, the physical path is what we care about. https://docs.redhat.com/en/documentation/Red_Hat_Enterprise_Linux/5/html/Online_Storage_Reconfiguration_Guide/persistent_naming.html

import re
import gi
from gi.repository.Gio import Drive

from usb_utilities import get_all_usb_hubs

gi.require_version('UDisks', '2.0') 
import gi.repository.UDisks as UDisks # This is annoying, language server doesn't like it

def get_usb_devices_on_hub(hub_basename: str) -> list[Drive]:
    """
    Identify all USB drives connected through a specific USB hub.
    
    :param str hub_path: A USB hub's basename; expected to be in form 1-1.1(.1)+
    """

    drives_on_hub = []

    client = UDisks.Client.new_sync(None)
    manager = client.get_object_manager()

    usb_drives = [
        drive for obj in manager.get_objects()
        if isinstance(obj, UDisks.Object) and (drive := obj.get_drive()) and 'usb' in drive.get_property('connection-bus')
        ]

    for d in usb_drives:
        if (block := client.get_block_for_drive(d, True)):
            symlink_paths: list[str] = block.get_property('symlinks')

            id = ""
            for p in symlink_paths:
                if 'by-id' in p:
                    id = p
                elif 'by-path' in p:
                    match = re.search(r'usb[v\d]*-\d+:(\d+(?:\.\d+)*)', p) # WIP regex to strip port path
                    if match:
                        # Trim off the last port; we don't care which port on the hub the drive is on, and we don't care which root port the hub is plugged into (the n- at the beginning)
                        if match.group(1)[:-2].startswith(hub_basename[2:]): 
                            print("Found a drive under this path: ", p, "\n\twith ID:", id)
                            drives_on_hub.append(d)
                            break
    return drives_on_hub

def get_all_drives_on_all_hubs():

    """
    Temporary test function
    """
    hubs = get_all_usb_hubs()
    for hub in hubs:
        for subhub in hub:
            print(subhub.basename)
