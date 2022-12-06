import unittest
from validate_reference import ValidateReference
from refclasses.bookref import Bookref

class Test_ValidateReference(unittest.TestCase):
    
    def setUp(self):
        self.references = []
        bookref1 = Bookref("avain1","kirjailija","title1",1,"kustantaja")
        bookref2 = Bookref("avain2","kirjailija","title2",1,"kustantaja")
        self.references.append(bookref1)
        self.references.append(bookref2)
        self.validator = ValidateReference()


    def test_key_already_exists(self):
        key = "avain1"
        self.assertEqual(self.validator.does_this_key_already_exist(key, self.references), True)

    def test_key_does_not_yet_exist(self):
        key = "avain"
        self.assertEqual(self.validator.does_this_key_already_exist(key, self.references), False)
