import unittest

import recls


class Test_recls(unittest.TestCase):

    def test_version(self):

        self.assertEqual('0.0.0.1', recls.__version__)
