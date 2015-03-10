#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Provides an interface to data-bearing functions."""

import datetime
import json
import os
import random
import time


def get_names():
    """Returns a list of names

    Returns:
        list: A list of names

    Examples:
        >>> get_names()
        ['JoAnne', 'Horace', ...]
    """
    fpath = os.path.dirname(os.path.abspath(__file__))
    fpath = os.path.join(fpath, 'names.json')

    fhandler = open(fpath, 'r')
    names = json.load(fhandler)
    fhandler.close()

    return names


def get_party_list():
    """Returns a random list of party participants

    Returns:
        list: A nested list of party attendees.

    Examples:
        >>> get_party_list()
        [['Jo', 'Michael', 'Jan'], ['Arty'], ...]
    """
    names = get_names()
    namect = len(names)
    families = random.randint(1, 300)

    attendees = []
    idx0 = 0
    while idx0 < families:
        idx0 += 1
        familyct = random.randint(1, 12)
        family = []
        idx1 = 0
        while idx1 < familyct:
            idx1 += 1
            family.append(names[random.randint(0, namect - 1)])
        attendees.append(family)

    return attendees


def get_email_data(email_count=300):
    """Returns a dictionary-style list of tuples for names and appointments.

    Args:
        email_count (int, optional): Amount of data to generate, Default 300.

    Returns:
        list: A list of two-item tuples.

    Examples:
        >>> get_email_data()
        [('Jo', 'Tuesday,  November 21, 2008 04:30PM'), ...]
    """
    names = get_names()
    namect = len(names)
    timestamp = time.time() + 259200

    data = []
    idx = 0
    while idx < email_count:
        idx += 1
        name = names[random.randint(0, namect - 1)]
        dtobj = datetime.datetime.fromtimestamp(timestamp)
        dtstr = dtobj.strftime('%A, %B %d, %Y %I:%M%p')
        data.append((name, dtstr))
        timestamp += 1200

    return data
