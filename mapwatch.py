#!/usr/bin/env python3
'''
Fancy explanation goes here
'''

import os
import re
import requests
import sys
import time

BASE_URL="https://cp.originsro.org/character/mapstats/"
MAP_NAME="tha_t"
MAP_NAME2="thana_step"
WARNING_TRIGGER=5
F12_WARNING=True

DELAY_SECONDS=3

def dothething():
    response = requests.get(BASE_URL)

    if (response.status_code !=200):
        print ("error "+str(response.status_code))
        return False

    current = response.text.find(MAP_NAME)
    at_least_one = (current != -1)
    current2 = response.text.find(MAP_NAME2)
    at_least_one2 = (current2 != -1)


    while current != -1 or current2 != -1:
        player_count = re.search('<strong>(.*)</strong>', response.text[current:])
        player_count2 = re.search('<strong>(.*)</strong>', response.text[current2:])
        full_name = re.search('(.*)</dt>', response.text[current:])
        
        if player_count:

            if int(player_count.group(1)) >= WARNING_TRIGGER:
                print("!!! group warning !!!")
            if F12_WARNING and full_name.group(1) == "tha_t12":
                print("!!! activity on F12 !!!")

            print(str(player_count.group(1))+" player(s) in "+ full_name.group(1))

            current = response.text.find(MAP_NAME, current+1)
        
        if player_count2:
            if int(player_count2.group(1)) >= WARNING_TRIGGER:
                print("!!! group warning on thana_step!!!")
            
            print(str(player_count2.group(1))+" player(s) in "+ MAP_NAME2)
            
            current2 = response.text.find(MAP_NAME2, current2+1)

 
    if at_least_one:
        print("-----------------------")

    return True
    


def main():
    loop = True
    while (loop == True):
        loop = dothething()
        time.sleep(DELAY_SECONDS)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("  Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)