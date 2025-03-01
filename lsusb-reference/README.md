These two files are the output of `lsusb -tv`, or `tree` with `verbosity`. 

The USB switch in question is `Port 002: Dev 013, If 0, Class=Hub, Driver=hub/4p, 480M ID 05e3:0610 Genesys Logic, Inc. Hub`, which is in turn connected to my [Uni Hub](https://www.amazon.com/dp/B07Q6YS7W2?ref_=ppx_hzsearch_conn_dt_b_fed_asin_title_1) `Port 001: Dev 005, If 0, Class=Hub, Driver=hub/5p, 480M ID 2109:2817 VIA Labs, Inc.`, which is in turn connected to the Thunderbolt 4 port on my Lenovo Intel E14 gen 6 `Bus 003.Port 001: Dev 001, Class=root_hub, Driver=xhci_hcd/12p, 480M ID 1d6b:0002 Linux Foundation 2.0 root hub`. Or at the very least, this matches the hardware configuration; I find it strange that these are all listed as `480M` which implies I'm getting USB 2.0 speeds all the way down. 

The Sabrent hub, to which all of my USB peripherals (i.e. those not needing anything above a few Mbps) is `Port 004: Dev 014, If 0, Class=Hub, Driver=hub/4p, 480M ID 05e3:0608 Genesys Logic, Inc. Hub`. 

The end goal is to effectively detect if the USB switch is connected or not connected, meaning that whatever user configuration file is needed will have to reference it directly. 