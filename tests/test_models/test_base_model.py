#!/usr/bin/python3
"""
Unittest for BaseModel class
"""
import unittest
import os
import pep8
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """TestBaseModel class"""

    @classmethod
    def setUPClass(cls):
        cls.base1 = BaseModel()
        cls.base1.name = "Praise"
        cls.base1.my_number = 23

    @classmethod
    def tearDownClass(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_style_check(self):
        """
        Test pep8 style
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_checking_for_function(self):
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_attributes(self):
        """Checks if the BaseModel has some particular attr"""
        self.assertTrue(hasattr(BaseModel, "__init__"))
        self.assertTrue(hasattr(BaseModel, "save"))
        self.assertTrue(hasattr(BaseModel, "to_dict"))

    def test_init(self):
        """Test the initialization"""
        self.assertTrue(isinstance(self.base1, BaseModel))

    def test_save(self):
        """Test save"""
        self.base1.save()
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)

