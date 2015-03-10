#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01."""


# Import Python libs
import unittest

# Import User libs
import data
import task_01

class Task01TestCase(unittest.TestCase):
    """Test cases for Task 01"""

    testdata = [['Hugo', 'Horace', 'Helen', 'Hesther'],
               ['Finnegan', 'Florance', 'Foster'],
               ['Jim', 'Jen', 'Jill', 'Justin', 'Janice', 'Jacob', 'Megatron']]

    def test_small_set(self):
        """Tests a small party stats implementation with default table size."""
        expected = (14, 4)
        self.assertEqual(task_01.get_party_stats(self.testdata), expected)

    def test_table_size(self):
        """Tests that table size adjusts accordingly"""
        expected = (14, 6)
        returned = task_01.get_party_stats(families=self.testdata,
                                           table_size=3)


    def test_large_set(self):
        """Tests a large set of data"""
        tabsize = 8
        list_data = data.get_party_list()
        headct = sum([len(v) for v in list_data])
        tabct = sum([-(-len(v) // tabsize) for v in list_data])
        expected = (headct, tabct)
        returned = task_01.get_party_stats(list_data, tabsize)
        self.assertEqual(returned, expected)


if __name__ == '__main__':
    unittest.main()
