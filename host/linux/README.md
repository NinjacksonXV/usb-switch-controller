## To-Do
- [ ] Handle unmounting failure cleanly
    - To research: Is there a way to get the PID of the process that's keeping it busy?
- [ ] Replace [`fs.call_unmount_sync(unmount_options)`](https://storaged.org/doc/udisks2-api/latest/UDisksFilesystem.html#udisks-filesystem-call-unmount-sync) with [`fs.call_unmount(unmount_options)`](https://storaged.org/doc/udisks2-api/latest/UDisksFilesystem.html#udisks-filesystem-call-unmount)
    - Will need to run [`call_unmount_finish()`](https://storaged.org/doc/udisks2-api/latest/UDisksFilesystem.html#udisks-filesystem-call-unmount-finish) in the callback.
            
