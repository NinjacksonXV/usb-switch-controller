import gi
gi.require_version('UDisks', '2.0') 

from gi.repository import GLib
import gi.repository.UDisks as UDisks # This is annoying, language server doesn't like anything but this

from usb_utilities import get_block_devices_under_hub

G_VARIANT_TYPE_VARDICT = GLib.VariantType.new('a{sv}')

param_builder = GLib.VariantBuilder.new(G_VARIANT_TYPE_VARDICT)

def get_usb_drives_on_hub(hub_basename: str) -> list[UDisks.Object]:
    """
    Identify all USB drives connected through a specific USB hub.
    
    :param str hub_path: A USB hub's basename; expected to be in form 1-1(.1)+
    """
    drives_under_hub = []
    
    block_device_paths = get_block_devices_under_hub(hub_basename)

    client = UDisks.Client.new_sync(None)
    manager = client.get_object_manager()

    for obj in manager.get_objects():
        if isinstance(obj, UDisks.Object) \
                and (fs := obj.get_filesystem()) \
                and (fs.get_property('mount_points') != []) \
                and (block := obj.get_block()) \
                and (drive := client.get_drive_for_block(block)) \
                and ('usb' in drive.props.connection_bus):
                    device: str = block.props.device
                    for p in block_device_paths:
                        if device.startswith(p):
                            drives_under_hub.append(obj)
    return drives_under_hub


def unmount_all_devices_on_hub(hub_basename: str):
    # Unmount options - https://storaged.org/doc/udisks2-api/latest/gdbus-org.freedesktop.UDisks2.Filesystem.html#gdbus-method-org-freedesktop-UDisks2-Filesystem.Unmount
    optname = GLib.Variant.new_string('force')
    value = GLib.Variant.new_boolean(False)
    variant_value = GLib.Variant.new_variant(value)
    newsv = GLib.Variant.new_dict_entry(optname, variant_value)
    
    # Standard options - https://storaged.org/doc/udisks2-api/latest/udisks-std-options.html
    optname = GLib.Variant.new_string('auth.no_user_interaction')
    value = GLib.Variant.new_boolean(False)
    variant_value = GLib.Variant.new_variant(value)
    newsv = GLib.Variant.new_dict_entry(optname, variant_value)
    
    # TODO
    # Break this out into its own function/class
    param_builder.add_value(newsv)
    unmount_options = param_builder.end() 

    # Would it be worth "inlining" this function so we can use the cached `fs` instead of calling the DBus method again?
    for drive in get_usb_drives_on_hub(hub_basename):
        if (fs := drive.get_filesystem()):
            fs.call_unmount_sync(unmount_options)

