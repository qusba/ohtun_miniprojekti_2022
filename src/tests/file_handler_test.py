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
        file.write("Testiavain;Testikirjailija_etunimi;Testikirjailija_sukunimi;Testititle;1999;Testikustantaja"+"\n")
        file.close()
        bookrefs = self.mock_filehandler.read_book_refs_from_file()
        book = Bookref("avain","kirjailija_etu","kirjailija_suku","title",1,"kustantaja")
        self.assertEqual(len(bookrefs),1)
        self.assertEqual(type(book),type(bookrefs[0]))
    
    def test_writing_book_references_without_a_new_ref_returns_all_old_refs(self):
        file = open(self.path,"w")
        file.write("Testiavain;Testikirjailija_etunimi;Testikirjailija_sukunimi;Testititle;1999;Testikustantaja"+"\n"
        +"avain2;kirjailija_etu2;kirjailija_suku2;title2;2000;kustantaja2"+"\n")
        file.close()
        refs_in_the_beginning = self.mock_filehandler.read_book_refs_from_file()
        self.mock_filehandler.write_book_refs_to_file(refs_in_the_beginning)
        refs_in_the_end = self.mock_filehandler.get_references()
        self.assertEqual(refs_in_the_beginning,refs_in_the_end)

    def test_writing_ref_object_into_bib_file(self):
        book = Bookref("avain","kirjailija_etu","kirjailija_suku","title",1,"kustantaja")
        bib_file = open("src/storage/test.bib", "w")
        self.mock_filehandler.write_ref_object_into_bibtext_file(book, bib_file)
        bib_file.close()

        bib_file = open("src/storage/test.bib", "r")
        bib_file_lines = bib_file.readlines()
        self.assertEqual(bib_file_lines[0],"@book{avain,\n")
        self.assertEqual(bib_file_lines[1],"    author = {kirjailija_etu, kirjailija_suku},\n")
        self.assertEqual(bib_file_lines[2],"    title = {title},\n")
        self.assertEqual(bib_file_lines[3],"    year = {1},\n")
        self.assertEqual(bib_file_lines[4],"    publisher = {kustantaja},\n")
        self.assertEqual(bib_file_lines[5],"}\n")
        self.assertEqual(bib_file_lines[6],"\n")
        bib_file.close()

    def test_writing_multiple_ref_objects_to_bib_file(self):
        refs = [Bookref("avain","kirjailija_etu","kirjailija_suku","title",1,"kustantaja"),
                Bookref("avain2","kirjailija_etu2","kirjailija_suku2","title2",2,"kustantaja2")]
        self.mock_filehandler.set_references(refs)
        return_bit = self.mock_filehandler.write_bibtext_file("src/storage/test.bib")
        self.assertAlmostEqual(return_bit, 1)

        bib_file = open("src/storage/test.bib", "r")
        bib_file_lines = bib_file.readlines()
        self.assertEqual(bib_file_lines[0],"@book{avain,\n")
        self.assertEqual(bib_file_lines[1],"    author = {kirjailija_etu, kirjailija_suku},\n")
        self.assertEqual(bib_file_lines[2],"    title = {title},\n")
        self.assertEqual(bib_file_lines[3],"    year = {1},\n")
        self.assertEqual(bib_file_lines[4],"    publisher = {kustantaja},\n")
        self.assertEqual(bib_file_lines[5],"}\n")
        self.assertEqual(bib_file_lines[6],"\n")

        self.assertEqual(bib_file_lines[7],"@book{avain2,\n")
        self.assertEqual(bib_file_lines[8],"    author = {kirjailija_etu2, kirjailija_suku2},\n")
        self.assertEqual(bib_file_lines[9],"    title = {title2},\n")
        self.assertEqual(bib_file_lines[10],"    year = {2},\n")
        self.assertEqual(bib_file_lines[11],"    publisher = {kustantaja2},\n")
        self.assertEqual(bib_file_lines[12],"}\n")
        self.assertEqual(bib_file_lines[13],"\n")
        bib_file.close()

    def test_without_references_writing_bib_file_fails(self):
        self.mock_filehandler.set_references([])
        return_bit = self.mock_filehandler.write_bibtext_file("src/storage/test.bib")
        self.assertAlmostEqual(return_bit, 0)

    def test_remove_reference_works(self):
        file = open(self.path,"w")
        file.write("Testiavain1;Testikirjailija_etu;Testikirjailija_suku;Testititle;1999;Testikustantaja"+"\n")
        file.write("Testiavain2;Testikirjailija_etu;Testikirjailija_suku;Testititle;1999;Testikustantaja"+"\n")
        file.close()
        self.mock_filehandler.remove_reference_from_file("Testiavain2")
        refs = self.mock_filehandler.read_book_refs_from_file()
        self.assertEqual(len(refs),1)
        self.assertEqual(refs[0].get_key(),"Testiavain1")

    def test_remove_reference_doesnt_do_anything_with_wrong_key(self):
        file = open(self.path,"w")
        file.write("Testiavain;Testikirjailija_etu;Testikirjailija_suku;Testititle;1999;Testikustantaja"+"\n")
        file.close()
        self.mock_filehandler.remove_reference_from_file("Eilöydy")
        refs = self.mock_filehandler.read_book_refs_from_file()
        self.assertEqual(len(refs),1)
        self.assertEqual(refs[0].get_key(),"Testiavain")