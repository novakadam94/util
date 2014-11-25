#
# Copyright (C) 2014 MTA SZTAKI
#
# Configuration primitives for the SZTAKI Cloud Orchestrator
#

import unittest

import occo.util as util

class DummyException(Exception):
    pass

class CoalesceTest(unittest.TestCase):
    def test_i_empty(self):
        self.assertIsNone(util.icoalesce([]))
    def test_i_default(self):
        self.assertEqual(util.icoalesce([], 5), 5)
    def test_i_first(self):
        self.assertEqual(util.icoalesce(('first', None, 'third')), 'first')
    def test_i_third(self):
        self.assertEqual(util.icoalesce((None, None, 'third')), 'third')
    def test_i_error(self):
        with self.assertRaises(DummyException):
            return util.icoalesce((None, None, None), DummyException(':P'))
    def test_empty(self):
        self.assertIsNone(util.coalesce())
    def test_first(self):
        self.assertEqual(util.coalesce('first', None, 'third'), 'first')
    def test_third(self):
        self.assertEqual(util.coalesce(None, None, 'third'), 'third')
    def test_error(self):
        with self.assertRaises(DummyException):
            return util.coalesce(None, None, None, DummyException(':P'))
    def test_flatten(self):
        l1, l2, l3 = [0, 1, 2, 3], [], [4, 5, 6]
        self.assertEqual(list(util.flatten([l1, l2, l3])), range(7))
    def test_rel_to_file(self):
        print util.rel_to_file('test.yaml')