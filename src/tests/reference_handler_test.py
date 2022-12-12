import unittest
from reference_handler import ReferenceHandler
from file_handler import FileHandler
from refclasses.bookref import Bookref
from console_io import ConsoleIO
from unittest.mock import Mock, ANY

class Test_ReferenceHandler(unittest.TestCase):
    
    def setUp(self):
        file = open("src/storage/testing_storage.csv","w")
        file.close()

        self.mock_io = Mock(wraps = ConsoleIO())
        self.inputs = ["Testiavain","kirjailija_etu","kirjailija_suku","Testititle",1999,"Testikustantaja"]
        self.mock_filehandler = Mock(wraps= FileHandler("src/storage/testing_storage.csv"))
        self.mock_referencehandler = Mock(wraps = ReferenceHandler(self.mock_io,self.mock_filehandler))


    def test_generating_a_book_referance_calls_filehandlers_writing_method(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_filehandler.write_book_refs_to_file.assert_called()

    def test_generating_1_book_reference_creates_1_book_object(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        references = self.mock_referencehandler.get_references()

        bookref = Bookref("avain","kirjailija_etu","kirjailija_suku","title",1,"kustantaja")
        self.assertEqual(len(references),1)
        self.assertEqual(type(references[0]),type(bookref))

    def test_print_references_calls_io_if_not_empty(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.print_references(self.mock_filehandler.get_references())
        self.mock_io.write.assert_called()

    def test_print_references_in_oldest_first_order_outputs_as_expected(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.print_references(self.mock_filehandler.get_references())
        printed = self.mock_io.get_log()[0]
        self.assertEqual(printed,"\033[0;33mkey\033[0m: \033[1;31mTestiavain\033[0m, \033[0;33mauthor\033[0m: \033[1;32mkirjailija_etu\033[0m, \033[1;32mkirjailija_suku\033[0m, \033[0;33mtitle\033[0m: \033[1;34mTestititle\033[0m, \033[0;33myear\033[0m: \033[1;35m1999\033[0m, \033[0;33mpublisher\033[0m: \033[1;36mTestikustantaja\033[0m")

    def test_print_references_in_newest_first_order_outputs_as_expected(self):
        secondary_inputs = ["Toinenavain","Antti","Arvuuttaja","Toinentitle",2000,"Otava"]
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.generate_book_reference_object(secondary_inputs)
        self.mock_referencehandler.print_references(self.mock_referencehandler.reverse_the_reference_list())
        printed = self.mock_io.get_log()[0]
        self.assertEqual(printed, "\033[0;33mkey\033[0m: \033[1;31mToinenavain\033[0m, \033[0;33mauthor\033[0m: \033[1;32mAntti\033[0m, \033[1;32mArvuuttaja\033[0m, \033[0;33mtitle\033[0m: \033[1;34mToinentitle\033[0m, \033[0;33myear\033[0m: \033[1;35m2000\033[0m, \033[0;33mpublisher\033[0m: \033[1;36mOtava\033[0m")


    def test_print_references_in_alphabetical_order_outputs_as_expected(self):
        secondary_inputs = ["Toinenavain","Antti","Arvuuttaja","Toinentitle",2000,"Otava"]
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.generate_book_reference_object(secondary_inputs)
        self.mock_referencehandler.print_references(self.mock_referencehandler.sort_refs_to_alphabetical_order_by_author_surname())
        printed = self.mock_io.get_log()[0]
        self.assertEqual(printed, "\033[0;33mkey\033[0m: \033[1;31mToinenavain\033[0m, \033[0;33mauthor\033[0m: \033[1;32mAntti\033[0m, \033[1;32mArvuuttaja\033[0m, \033[0;33mtitle\033[0m: \033[1;34mToinentitle\033[0m, \033[0;33myear\033[0m: \033[1;35m2000\033[0m, \033[0;33mpublisher\033[0m: \033[1;36mOtava\033[0m")

    def test_print_refereces_in_reversed_alphabetical_order_outputs_as_expected(self):
        secondary_inputs = ["Toinenavain","Antti","Arvuuttaja","Toinentitle",2000,"Otava"]
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.generate_book_reference_object(secondary_inputs)
        self.mock_referencehandler.print_references(self.mock_referencehandler.sort_refs_to_reverse_alphabetical_order_by_author_surname())
        printed = self.mock_io.get_log()[0]
        self.assertEqual(printed,"\033[0;33mkey\033[0m: \033[1;31mTestiavain\033[0m, \033[0;33mauthor\033[0m: \033[1;32mkirjailija_etu\033[0m, \033[1;32mkirjailija_suku\033[0m, \033[0;33mtitle\033[0m: \033[1;34mTestititle\033[0m, \033[0;33myear\033[0m: \033[1;35m1999\033[0m, \033[0;33mpublisher\033[0m: \033[1;36mTestikustantaja\033[0m")
