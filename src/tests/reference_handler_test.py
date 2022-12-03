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
        self.inputs = ["Testiavain","Testikirjailija","Testititle",1999,"Testikustantaja"]
        self.mock_filehandler = Mock(wraps= FileHandler("src/storage/testing_storage.csv"))
        self.mock_referencehandler = Mock(wraps = ReferenceHandler(self.mock_io,self.mock_filehandler))


    def test_generating_a_book_referance_calls_filehandlers_writing_method(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_filehandler.write_book_refs_to_file.assert_called()

    def test_generating_1_book_reference_creates_1_book_object(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        references = self.mock_referencehandler.get_references()

        bookref = Bookref("avain","kirjailija","title",1,"kustantaja")
        self.assertEqual(len(references),1)
        self.assertEqual(type(references[0]),type(bookref))

    def test_print_references_calls_io_if_not_empty(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.print_references()
        self.mock_io.write.assert_called()

    def test_print_references_outputs_as_expected(self):
        self.mock_referencehandler.generate_book_reference_object(self.inputs)
        self.mock_referencehandler.print_references()
        printed = self.mock_io.get_log()[0]
        self.assertEqual(printed,"key: Testiavain, author: Testikirjailija, title: Testititle, year: 1999, publisher: Testikustantaja")


