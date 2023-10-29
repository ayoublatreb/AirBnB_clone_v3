#!/usr/bin/python3

""" module containing tests for class City """

import unittest
from models.city import City  # Import City from the correct module

class TestCity(unittest.TestCase):
    """ tests for class City """

    def test_City_inheritance(self):
        """ test that City is a subclass of BaseModel """
        test_city = City()
        self.assertIsInstance(test_city, BaseModel)

    def test_City_attributes(self):
        """ test attributes """
        test_city = City()
        self.assertTrue("state_id" in test_city.__dict__)
        self.assertTrue("name" in test_city.__dict__)

    def test_state_id_type(self):
        """ test state_id data type """
        test_city = City()
        state_id = getattr(test_city, "state_id")
        self.assertIsInstance(state_id, str)

    def test_name_type(self):
        """ test name data type """
        test_city = City()
        name = getattr(test_city, "name")
        self.assertIsInstance(name, str)

if __name__ == '__main__':
    unittest.main()


