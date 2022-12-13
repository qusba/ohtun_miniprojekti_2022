import unittest
from refclasses.bookref import Bookref

class Test_Bookref(unittest.TestCase):

    def setUp(self):
        self.bookref = Bookref("Testiavain","Testikirjailija_etunimi", "Testikirjailija_sukunimi", "Testititle", 1999, "Testikustantaja")
        self.tags = []
        self.tags.append("Fiktio")
        self.tags.append("Fakta")

    def test_getters_behave_as_intended(self):
        self.assertEqual(self.bookref.get_key(),"Testiavain")
        self.assertEqual(self.bookref.get_author_first_name(), "Testikirjailija_etunimi")
        self.assertEqual(self.bookref.get_author_last_name(), "Testikirjailija_sukunimi")
        self.assertEqual(self.bookref.get_title(), "Testititle")
        self.assertEqual(self.bookref.get_year(), 1999)
        self.assertEqual(self.bookref.get_publisher(), "Testikustantaja")

    def test_bookref_object_string_representation_prints_properly(self):
        printti = str(self.bookref)
        #self.assertEqual(printti,"key: Testiavain, author: Testinimi, title: Testititle, year: 1999, publisher: Testikustantaja")
        self.assertEqual(printti, "\033[0;33mkey\033[0m: \033[1;31mTestiavain\033[0m, \033[0;33mauthor\033[0m: \033[1;32mTestikirjailija_etunimi\033[0m, \033[1;32mTestikirjailija_sukunimi\033[0m, \033[0;33mtitle\033[0m: \033[1;34mTestititle\033[0m, \033[0;33myear\033[0m: \033[1;35m1999\033[0m, \033[0;33mpublisher\033[0m: \033[1;36mTestikustantaja\033[0m")

    def test_tag_setter_sets_tags(self):
        self.bookref.set_tags(self.tags)
        self.assertEqual(self.bookref.get_tags(), self.tags)

    def test_bookref_tags_are_in_print_if_they_exist(self):
        self.bookref.tags = self.tags
        printti = str(self.bookref)
        #self.assertEqual(printti,"key: Testiavain, author: Testinimi, title: Testititle, year: 1999, publisher: Testikustantaja")
        self.assertEqual(printti, "\033[0;33mkey\033[0m: \033[1;31mTestiavain\033[0m, \033[0;33mauthor\033[0m: \033[1;32mTestikirjailija_etunimi\033[0m, \033[1;32mTestikirjailija_sukunimi\033[0m, \033[0;33mtitle\033[0m: \033[1;34mTestititle\033[0m, \033[0;33myear\033[0m: \033[1;35m1999\033[0m, \033[0;33mpublisher\033[0m: \033[1;36mTestikustantaja\033[0m, \033[0;33mtagit\033[0m: \033[1;37mFiktio, Fakta\033[0m ")