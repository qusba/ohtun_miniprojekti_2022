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

    def test_is_empty_works_with_empty_input(self):
        user_input = ""
        trial = self.validator.is_input_empty(user_input)
        self.assertEqual(trial,True)
    
    def test_is_empty_works_with_not_empty_input(self):
        user_input = "avain3"
        trial = self.validator.is_input_empty(user_input)
        self.assertEqual(trial,False)

    def test_is_input_a_number_works_with_a_number(self):
        user_input = "1994"
        trial = self.validator.is_input_a_number(user_input)
        self.assertEqual(trial,True)

    def test_is_input_a_number_works_with_a_non_number(self):
        user_input = "nineteen-ninety-four"
        trial = self.validator.is_input_a_number(user_input)
        self.assertEqual(trial,False)

    def test_is_number_positive_works_with_positive_numbers(self):
        user_input1 = "32"
        user_input2 = "0"
        trial1 = self.validator.is_number_positive(user_input1)
        trial2 = self.validator.is_number_positive(user_input2)

        self.assertEqual(trial1, True)
        self.assertEqual(trial2, True)

    def test_is_number_positive_works_with_negative_numbers(self):
        user_input = "-1999"
        trial = self.validator.is_number_positive(user_input)
        self.assertEqual(trial,False)