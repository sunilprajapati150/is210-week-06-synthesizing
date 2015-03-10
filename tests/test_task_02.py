#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02."""


# Import Python libs
import unittest

# Import User libs
import data
import task_02

class Task02TestCase(unittest.TestCase):
    """Test cases for Task 02"""

    fmtstr = 'Dear {},\nI look forward to meeting with you on {}.\nBest,\nMe'

    def test_small_set(self):
        """Tests a small data implementation"""
        listdata = [('Agatha', 'Monday, March 16, 2015 05:00PM'),
                ('Arthur', 'Monday, March 16, 2015 05:20PM')]
        expected = [self.fmtstr.format(*v) for v in listdata]
        returned = task_02.prepare_email(listdata)
        self.assertEqual(returned, expected)

    def test_large_set(self):
        """Tests a large set of data"""
        listdata = data.get_email_data(1000)
        expected = [self.fmtstr.format(*v) for v in listdata]
        returned = task_02.prepare_email(listdata)
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()
