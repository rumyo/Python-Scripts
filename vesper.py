#!/usr/bin/env python3
'''
Fancy explanation goes here
'''

import os
import re
import requests
import sys
import time
from datetime import datetime

BASE_URL="https://cp.originsro.org/character/mapstats/"
MAP_NAME="jupe_core"
MAP_NAME2="juperos_02"
WARNING_TRIGGER=4
FLAGG=True

DELAY_SECONDS=60

def dothething():
    global FLAGG
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
        
        if player_count:
            FLAGG=False
            if int(player_count.group(1)) >= WARNING_TRIGGER:
                print("!!! group warning on jupe_core!!!")
            if int(player_count.group(1)) >= 1:
                print("!!! activity on jupe_core !!!")

            print(str(player_count.group(1))+" player(s) in "+ MAP_NAME)

            current = response.text.find(MAP_NAME, current+1)
            
        
        if player_count2:
            FLAGG=False
            if int(player_count2.group(1)) >= WARNING_TRIGGER:
                print("!!! group warning on juperos_02!!!")
            if int(player_count2.group(1)) >= 1:
                print("!!! activity on juperos_02 !!!")

            print(str(player_count2.group(1))+" player(s) in "+ MAP_NAME2)

            current2 = response.text.find(MAP_NAME2, current2+1)

    if current == -1 and FLAGG:
        print("no activity on jupe_core")

    if current == -1 and FLAGG:
        print("no activity on juperos_02")
 
    if at_least_one or at_least_one2:
        print(datetime.utcnow().strftime("%H:%M") + " Server Time")
        print("-------------------------------------------")

    FLAGG=True
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