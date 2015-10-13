__author__ = 'bharre001c'

import requests
import json
import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Please enter IP address")
    parser.add_argument('-ip', '--ip', help="Enter ip address in this field")
    args = parser.parse_args()

    if not args.ip:
        print "Please Enter ip address"
    else:
        print requests.get("http://"+args.ip+":5000/getVersion").json()