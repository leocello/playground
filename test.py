import unittest

class TestApplication(unittest.TestCase):
    def test_1(self):
        self.assertEqual('foo'.upper(), 'FOO')
