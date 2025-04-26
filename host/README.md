## Linux
### UDisks
#### GObject Type Hints
To get type hints working (targeting Pyright specifically), you'll need to generate the appropriate stubs. First, [generate the stubs](https://github.com/microsoft/pyright/blob/main/docs/type-stubs.md#generating-type-stubs-from-command-line) for the `gi.repository` namespace provided by [pygobject-stubs](https://github.com/pygobject/pygobject-stubs). To generate the Python stub for the UDisks module for GObject Introspection, `cd` to `./tools` and run `./generate_types.sh`. This runs the stub generator tool as described in the [pygobject-stubs contribution README](https://github.com/pygobject/pygobject-stubs/blob/master/CONTRIBUTING.md).

From there, the only way I've discovered to properly import it without conflicting with existing stubs is to use:
```py
import gi
gi.require_version('UDisks', '2.0') 
import gi.repository.UDisks as UDisks
```

If using Pyright, I also recommend adding this to your `pyrightconfig.json` to disable the missing module warning:
```json 
"reportMissingModuleSource": false
```
As a GIR module, UDisks isn't resolved until runtime.
