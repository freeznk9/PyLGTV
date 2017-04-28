# Introduce
LG TV device control By python with rs232c
if your LG TV has the serial(com, rs232), you can control your TV by this command.
I use this command for home assistant(automation) with kodi on s905x and Amazon Echodot ....

# Hardware Connection
PC/Raspberry Pi/Others ---(RS232C)--- LG TV

# Supported TV Model
http://www.lg.com/us/support-product/lg-42LY340C
42LY340C : tested
xxLY340C : same protocol
xxLY540C : same protocol
xxLX530H : maybe same...
other models : maybe...

# Commands
python cmd_lgtv.py power on/off/status

python cmd_lgtv.py volume status/[0~25]

python cmd_lgtv.py mute on/off/status

