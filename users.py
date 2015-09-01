#!/usr/bin/env python
# -*- coding: utf-8 -*-
import xml.etree.cElementTree as ET
import pprint
import re
"""
Your task is to explore the data a bit more.
The first task is a fun one - find out how many unique users
have contributed to the map in this particular area!

The function process_map should return a set of unique user IDs ("uid")
"""

def get_user(element):
    users = set()
    for e in element:
        if 'uid' in e.attrib:
            users.add(e.attrib['uid'])
    return users


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        users = get_user(element)

    return users


def test():

    users = process_map('san-francisco_california.osm')
    pprint.pprint(users)
    # assert len(users) == 1120



if __name__ == "__main__":
    test()
