#!/usr/bin/env python
'''
Using ciscoconfparse find the crypto maps that are not using AES (based-on the
transform set name). Print these entries and their corresponding transform set
name.
'''

import re
from ciscoconfparse import CiscoConfParse

def main():
    '''
    Using ciscoconfparse find the crypto maps that are not using AES (based-on
    the transform set name). Print these entries and their corresponding
    transform set name.
    '''
    cisco_file = 'cisco.txt'

    cisco_cfg = CiscoConfParse(cisco_file)
    crypto_maps = cisco_cfg.find_objects_wo_child(parentspec=r'crypto map CRYPTO',
                                                  childspec=r'AES')
    print "\nCrypto maps not using AES:"
    for entry in crypto_maps:
        for kid in entry.children:
            if 'transform' in kid.text:
                print kid.text
    print

if __name__ == "__main__":
    main()
