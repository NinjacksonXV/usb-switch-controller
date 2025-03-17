This repository holds documentation and code for my USB switch controller; it's a Pi Pico W with some added ports and functionality, meant to cleanly control and automate a 4-port USB switch. Features include:
- [ ] A script meant to be bound to an OS event, such as a keybind, which will trigger the USB switch to the other computer
- [ ] Cleanly unmounting drives connected to the switch beforehand
- [ ] If a computer is turned on, and the other computer is turned off and had the switch connected to it, automatically switch to the on computer by wirelessly pinging the Pi Pico W
- And more (or more detailed descriptions of these features)
## Setup
`git clone` with `--recurse-submodules` to pull the [Raspberry Pi Pico SDK](https://github.com/raspberrypi/pico-sdk). For now, see `buildInputs` in `flake.nix` to get a WIP list of other dependencies. 

If using Nix (with experimental Nix commands enabled), you can run `nix develop` and set the `PICO_SDK_PATH` environment variable manually (`$PWD/pico-sdk`) or in the Nix shell hook. Alternatively, use [direnv](https://direnv.net/) with the [nix-direnv](https://github.com/nix-community/nix-direnv) module, which will automatically enter you into the Nix shell and set needed environment variables.

## Software Overview
### Getting USB Info
See [lsusb-reference/README.md](lsusb-reference/README.md)
## Hardware Overview
### USB Switch
My USB switch of choice for this project was the UGREEN USB switch, with 4 input ports and two output ports. It has a button on the chassis like most USB switches, but it has one standout feature: a USB mini port with an external button. The button itself was uninteresting to me; it's lightweight and rather ugly. But the port itself allows for trivial switching by bridging the data +/- pins.
- Amazon Link for 5Gbps Model ($49.99 USD): https://www.amazon.com/dp/B0D2QJMFCT
- Amazon Link for 10Gbps Model ($69.99 USD): https://www.amazon.com/dp/B0CH7T76RX

I also combined it with:

...this fairly generic Sabrent USB 2.0 hub; it seemed wasteful to have 5Gbps but only plug in a few bandwidth-light peripherals. I plugged this into one of the ports, leaving the other two free for highter-bandwidth devices.
- Amazon Link ($6.95): https://www.amazon.com/dp/B00L2442H0

...two USB 3.0 extension cables from Amazon basics, which will be installed on my desk for easy access to the high-speed ports.
- Amazon Link ($16.14 USD for 6-foot variant): https://www.amazon.com/dp/B014RWATK2

### Switcher Hardware
See [hardware/README](hardware/README.md) for a more in-depth overview.
#### Microcontroller
I went with a third-party Pi Pico W for its price, breadth of compatibility and documentation, and for this particular model, a USB-C port.
- AliExpress link ($5.00 USD): https://www.aliexpress.us/item/3256806674735573.html

The Pico W itself is configured as a USB device and will be connected to the switch itself; its power will come from another source, however, so that it can remain on and uninterurupted for wireless control.

#### Misc. Hardware
- 10pcs USB 2.0 Type A Female Jack Port ($0.98 USD): https://www.aliexpress.com/item/3256806189715509.html
    - Two of these are used in this project: one is to connect the Pico to the mini USB port on the switch, and the other is for an optional physical USB button. You could replace this with a mini USB port to use the original button, if desired; I plan to build a small button with a keyboard key switch.
- 18cm Mini USB 2.0 Cable ($1.07 USD): https://www.aliexpress.com/item/3256807031921854.html
- 10pcs USB 3.1 Type C Connecter ($1.70 USD): https://www.aliexpress.com/item/3256804675613750.html
    - This is for providing power to the Pi Pico.
- 20pcs Protoboard ($3.59 USD): https://www.aliexpress.com/item/3256805882382244.html
    - I'm using the 10x24 hole protoboard included in this kit.
- 50pcs Black M1.6 4mm Phillips Screws ($0.94 USD): https://www.aliexpress.com/item/3256802339245383.html
- 100pcs M1.6 3mm Heatset Inserts ($2.31 USD): https://www.aliexpress.com/item/3256804349544912.html
