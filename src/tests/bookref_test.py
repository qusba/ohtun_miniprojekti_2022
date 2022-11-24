import unittest
from refclasses.bookref import Bookref

class Test_Bookref(unittest.TestCase):

    def setUp(self):
        self.bookref = Bookref("Testinimi", "Testititle", 1999, "Testikustantaja")

    def test_getterit_toimivat(self):
        self.assertEqual(self.bookref.get_author(), "Testinimi")
        self.assertEqual(self.bookref.get_title(), "Testititle")
        self.assertEqual(self.bookref.get_year(), 1999)
        self.assertEqual(self.bookref.get_publisher(), "Testikustantaja")
