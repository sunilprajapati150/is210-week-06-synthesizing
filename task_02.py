#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""a really good docstring"""

def prepare_email(appointments):
    email = 'Dear {},\nI look foward to meeting you on {}.\nBest, \nMe'
    new_list = []
    for list_item in appointments:
        name = list_item[0]
        date = list_item[1]
        new_list.append(email.format(name, date))
    return new_list
    
