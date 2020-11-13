import unittest

from majority import majority


class TestMajority(unittest.TestCase):

    def test_empty_input(self):
        input = []
        self.assertIsNone(majority(input))

    def test_no_majority_element(self):
        input = ['1', '2', '3']
        self.assertIsNone(majority(input))

        input = ['1', '1', '1', '2', '2', '2', '3']
        self.assertIsNone(majority(input))

        input = ['1', '1', '1', '3', '2', '2', '2']
        self.assertIsNone(majority(input))

        input = ['1', '2']
        self.assertIsNone(majority(input))

        input = ['1', '2', '1', '2']
        self.assertIsNone(majority(input))

        input = ['1', '1', '3', '2', '2', '1']
        self.assertIsNone(majority(input))

    def test_majority_element(self):
        input = ['1']
        self.assertEqual(majority(input), '1')

        input = ['1', '2', '1']
        self.assertEqual(majority(input), '1')

        input = ['1', '1', '1']
        self.assertEqual(majority(input), '1')

        input = ['1', '1', '2']
        self.assertEqual(majority(input), '1')

        input = ['1', '1', '1', '2', '3']
        self.assertEqual(majority(input), '1')