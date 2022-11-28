import unittest
from unittest.mock import Mock
from file_handler import FileHandler
from refclasses.bookref import Bookref

class Test_FileHandler(unittest.TestCase):
    def setUp(self):
        self.path = "src/storage/testing_storage.csv"
        file = open(self.path,"w")
        file.close()
        self.mock_filehandler = Mock(wraps = FileHandler(self.path))

    def test_read_book_references_does_nothing_if_references_are_empty(self):
        self.mock_filehandler.read_book_refs_from_file()
        refs = self.mock_filehandler.get_references()
        self.assertEqual(refs,[])
    
    def test_read_book_references_returns_book_objects_when_references_not_empty(self):
        file = open(self.path,"w")
        file.write("Testiavain;Testikirjailija;Testititle;1999;Testikustantaja"+"\n")
        file.close()
        bookrefs = self.mock_filehandler.read_book_refs_from_file()
        book = Bookref("avain","kirjailija","title",1,"kustantaja")
        self.assertEqual(len(bookrefs),1)
        self.assertEqual(type(book),type(bookrefs[0]))
    
    def test_writing_book_references_without_a_new_ref_returns_all_old_refs(self):
        file = open(self.path,"w")
        file.write("Testiavain;Testikirjailija;Testititle;1999;Testikustantaja"+"\n"
        +"avain2;kirjailija2;title2;2000;kustantaja2"+"\n")
        file.close()
        refs_in_the_beginning = self.mock_filehandler.read_book_refs_from_file()
        self.mock_filehandler.write_book_refs_to_file(refs_in_the_beginning)
        refs_in_the_end = self.mock_filehandler.get_references()
        self.assertEqual(refs_in_the_beginning,refs_in_the_end)


