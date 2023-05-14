#!/usr/bin/python3

import unittest
import os
import pep8
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.Testcase):

    @classmethod
    def setUpClass(cls):
        cls.city1 = City()
        cls.city1.name = "Ral"
        cls.city1.id = "NC"

    @classmethod
    def tearDownClass(cls):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_syle_check(self):
        """
        Tests pep8 syle
        """
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["models/city.py"])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_is_subclass(self):
        """
        Tests if the Class of city1 is a subclass of the main class BaseModel
        """
        self.assertTrue(issubclass(self.city1.__class__, BaseModel), True)

    def test_checking_for_comment(self):
        """
        Tests whether the City class has a docstring(comments)
        """
        self.assertIsNotNone(city.__doc__)

    def test_init(self):
        """
        Testing if values are equal as input
        """
        city = City(name="New York", state_id="NY")
        self.assertTrue(isinstance(city, BaseModel))
        self.assertTrue(city.name, "New York")
        self.assertTrue(city.state_id, "NY")

    def test_has_attributes(self):
        """
        Test is city1 has specific attributes in it's dictionary
        """
        self.assertTrue("id" in self.city1.__dic__)
        self.assertTrue("created_at" in self.city1.__dict__)
        self.assertTrue("updated_at" in self.city1.__dic__)
        self.assertTrue("name" in self.city1.__dic__)

    def test_attributes_are_strings(self):
        """
        Test if certain attributes are of type string
        """
        self.assertEqual(type(self.city1.name), str)
        self.assertEqual(type(self.city1.state_id), str)

    def test_save(self):
        """
        Testing whether the save method of the City class is working
        as expected
        """
        self.city1.save()
        self.assertNotEqual(self.city1.created_at, self.city1.updated_at)

    def test_to_dict(self):
        """
        Tests whether th City instance(city1) has to_dict method
        by checking if "to_dict is in the list of attributes
        """
        self.assertTrue(hasattr(self.city1, 'to_dict'))

if __name__ == "__main__":
    unittest.main()
