#!/usr/bin/env python3
import unittest
from models.user import User


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_user_instance(self):
        self.assertIsInstance(self.user, User)

    def test_user_attributes(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_attribute_types(self):
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_user_inherited_attributes(self):
        self.assertTrue(hasattr(self.user, "id"))
        self.assertTrue(hasattr(self.user, "created_at"))
        self.assertTrue(hasattr(self.user, "updated_at"))

    def test_user_str_representation(self):
        expected = "[{}] ({}) {}".format(self.user.__class__.__name__,
                                         self.user.id,
                                         self.user.__dict__)
        self.assertEqual(str(self.user), expected)

    def test_user_to_dict_method(self):
        self.user.email = "me@yahoo.com"
        self.user.password = "my password"
        self.user.first_name = "Boomni"
        self.user.last_name = "Jonathan"
        dict_representation = self.user.to_dict()
        self.assertIsInstance(dict_representation, dict)
        self.assertEqual(dict_representation["email"], "me@yahoo.com")
        self.assertEqual(dict_representation["password"], "my password")
        self.assertEqual(dict_representation["first_name"], "Boomni")
        self.assertEqual(dict_representation["last_name"], "Jonathan")
        self.assertEqual(dict_representation["__class__"], "User")
        self.assertTrue("id" in dict_representation)
        self.assertTrue("created_at" in dict_representation)
        self.assertTrue("updated_at" in dict_representation)

    def test_user_save_method(self):
        self.user.save()
        self.assertNotEqual(self.user.created_at, self.user.updated_at)

if __name__ == '__main__':
    unittest.main()
