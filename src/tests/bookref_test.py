import unittest
from refclasses.bookref import Bookref

class Test_Bookref(unittest.TestCase):

    def setUp(self):
        self.bookref = Bookref("Testiavain","Testinimi", "Testititle", 1999, "Testikustantaja")

    def test_getterit_toimivat(self):
        self.assertEqual(self.bookref.get_key(),"Testiavain")
        self.assertEqual(self.bookref.get_author(), "Testinimi")
        self.assertEqual(self.bookref.get_title(), "Testititle")
        self.assertEqual(self.bookref.get_year(), 1999)
        self.assertEqual(self.bookref.get_publisher(), "Testikustantaja")

    def test_olio_printataan_oikein(self):
        printti = str(self.bookref)
        self.assertEqual(printti,"key: Testiavain, author: Testinimi, title: Testititle, year: 1999, publisher: Testikustantaja")
