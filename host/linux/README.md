## To-Do
- [ ] Figure out how to use the `*Iface`s, so that I can get properties directly.
    - `Udisks.<DBus interface name>Iface.get_<property>(<var of type DBus interface name)` seems to be how I *would* access this, e.g. `UDisks.BlockIface.get_symlinks(block)`, but it gives me a `TypeError: 'property' object is not a callable`; I'm assuming I need to somehow get an instance of the interface? Doesn't seem like an obvious way to do so, unlike something like a client. In fairness, in the few PyGObject projects I've looked at, no one seems to use this; it might just be unavailable. 
- [ ] Figure out differences in `/dev/disk/by-path/usb{,v1,v2}`. I'm going to assume for now, since they all seem to be symlinks to the same drive according to Udisks, that this isn't really necessary, and I can just grab the first path I find.
- [ ] Truncate `USBDevice` class to only grab needed properties
- [ ] Eventually, fix string handling to ensure a user could have >10 root USB ports
