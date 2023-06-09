#!/usr/bin/env python3

import subprocess
import optparse
import re


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
            parser.error("Please specify an interface use --help for more information")
    elif not options.new_mac:
            parser.error("Please specify the MAC address use --help for more information")
    return options

def change_mac(interface, new_mac):
    print("[success] Changing Mac Address for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "down", "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_curent_mac (interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read MAC Address")


options = get_arguments()
current_mac = get_curent_mac(options.interface)
print("current_mac = " + str(current_mac))
change_mac(options.interface, options.new_mac)
current_mac = get_curent_mac(options.interface)
if current_mac ==  options.new_mac:
    print("Mac Address was successfully changed to " + current_mac)
else:
    print("Mac Address did not get changed.")
