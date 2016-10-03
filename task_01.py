#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a really good docstring"""

def get_party_status(families,table_size = 6):

    guests = 0
    tables = 0
    for list_item in families:
        guest = guest + len(list_item)
        tables = tables + (-(-(len(list_item))//table_size))

    return(guests, tables)
    
