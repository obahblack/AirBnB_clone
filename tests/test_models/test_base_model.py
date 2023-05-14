#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
<<<<<<< HEAD

    @classmethod
    def setUpClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Greg"
        cls.base1.my_number = 29
=======
    """TestBaseModel class"""

    @classmethod
    def setUPClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Praise"
        cls.base1.my_number = 23
>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
<<<<<<< HEAD
        Tests pep8 style
=======
        Test pep8 style
>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

<<<<<<< HEAD
    def test_checking_for_functions(self):
=======
    def test_checking_for_function(self):
>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
<<<<<<< HEAD
=======
        """Checks if the BaseModel has some particular attr"""
>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
<<<<<<< HEAD
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
=======
        """Test the initialization"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        """Test save"""
>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

    def test_to_dict(self):
<<<<<<< HEAD
=======
        """Testing the to_dict function for the dictionary"""
>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b
        base1_dict = self.base1.to_dict()
        self.assertEqual(self.base1.__class__.__name__, 'BaseModel')
        self.assertIsInstance(base1_dict['created_at'], str)
        self.assertIsInstance(base1_dict['updated_at'], str)

<<<<<<< HEAD

if __name__ == "__main__":
    unittest.main()
=======
if __name__ == "__main__":
    unittest.main()

>>>>>>> cc383c63fd3206b665ac534ee40903abaa2ca93b
