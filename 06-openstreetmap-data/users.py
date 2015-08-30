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
    uids = set()
    if 'uid' in element.attrib:
        uids.add(element.attrib['uid'])
    for e in element:
        if 'uid' in e.attrib:
            uids.add(e.attrib['uid'])
    return uids


def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        users = get_user(element)

    return users


def test():

    users = process_map('example.osm')
    pprint.pprint(users)
    assert len(users) == 6



if __name__ == "__main__":
    test()