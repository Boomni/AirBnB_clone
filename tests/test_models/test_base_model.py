#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json
import models


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        """ Automatically set BaseModel instance to self.bm """
        self.bm = BaseModel()

    def test_class_type(self):
        """Test for correct class type"""
        self.assertEqual(self.bm.__class__.__name__, "BaseModel")

    def test_class_docstring(self):
        """ Test for class documentation """
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_module_docstrings(self):
        """ Test for module documentation """
        self.assertTrue(len(models.base_model.__doc__) > 0)

    def test_init(self):
        """Test if no arguments passed, id, created_at and updated_at exists & are valid"""
        self.assertTrue(len(self.bm.__init__.__doc__) > 0)
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertTrue(hasattr(self.bm, "updated_at"))
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_adding_attributes(self):
        """Test for manually adding parameters to empty BaseModel"""
        self.bm.string = "I am coding"
        self.bm.number = 34
        self.bm.list = [1, 2, 3]
        self.bm.dict = {"a": 1}
        self.assertTrue(hasattr(self.bm, "string"))
        self.assertTrue(hasattr(self.bm, "number"))
        self.assertTrue(hasattr(self.bm, "list"))
        self.assertTrue(hasattr(self.bm, "dict"))
        self.assertEqual(type(self.bm.string), str)
        self.assertEqual(type(self.bm.number), int)
        self.assertEqual(type(self.bm.list), list)
        self.assertEqual(type(self.bm.dict), dict)

    def test_str(self):
        """ Test the output of __str__ method """
        self.assertTrue(len(self.bm.__str__.__doc__) > 0)
        bm_str = str(self.bm)
        self.assertEqual("[{}] ({}) {}".format(self.bm.__class__.__name__,
                                               self.bm.id,
                                               self.bm.__dict__), bm_str)
        self.assertIn("'id':", bm_str)
        self.assertIn("'created_at':", bm_str)
        self.assertIn("'updated_at':", bm_str)

    def test_save(self):
        """ Test to validate updated_at changes when saved """
        self.assertTrue(len(self.bm.save.__doc__) > 0)
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated_at, self.bm.updated_at)

    def test_to_dict(self):
        """Test to validate to_dict is output is correct"""
        self.assertTrue(len(self.bm.to_dict.__doc__) > 0)
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)
        self.assertIn('__class__', bm_dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

    def test_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        self.bm.name = "Boomni"
        self.bm.number = 1987
        d = self.bm.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_recreate_instance(self):
        """Test to create instances from to_dict"""
        self.bm.name = "Joseph"
        self.bm.number = 1993
        d = self.bm.to_dict()
        new_b = BaseModel(**d)
        self.assertEqual(self.bm.id, new_b.id)
        self.assertEqual(self.bm.created_at.isoformat(), new_b.created_at)
        self.assertEqual(self.bm.updated_at.isoformat(), new_b.updated_at)
        self.assertEqual(self.bm.name, new_b.name)
        self.assertEqual(self.bm.number, new_b.number)
        self.assertEqual(type(self.bm.id), str)
        self.assertEqual(self.bm.created_at.__class__.__name__, "datetime")
        self.assertEqual(self.bm.created_at.__class__.__name__, "datetime")
        self.assertEqual(type(new_b.id), str)
        self.assertEqual(new_b.created_at.__class__.__name__, "str")
        self.assertEqual(new_b.updated_at.__class__.__name__, "str")
        self.assertTrue(self.bm is not new_b)

    def test_string_input(self):
        """Passing a string for args"""
        b = BaseModel("Betty")
        self.assertEqual(self.bm.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(self.bm, "id"))
        self.assertTrue(hasattr(self.bm, "created_at"))
        self.assertTrue(hasattr(self.bm, "updated_at"))

    def test_from_dict(self):
        """ Verify instances from dictionary works correctly """
        bm_dict = self.bm.to_dict()
        bm2 = BaseModel(**bm_dict)
        self.assertIsInstance(bm2, BaseModel)
        self.assertEqual(bm2.id, self.bm.id)
        self.assertEqual(bm2.created_at, self.bm.created_at.isoformat())
        self.assertEqual(bm2.updated_at, self.bm.updated_at.isoformat())

    def test_json(self):
        """ Test json convertion of dictionary works correctly """
        bm_dict = self.bm.to_dict()
        bm_json = json.dumps(bm_dict)
        self.assertIsInstance(bm_json, str)
        bm_dict2 = json.loads(bm_json)
        self.assertIsInstance(bm_dict2, dict)
        self.assertEqual(bm_dict2, bm_dict)

    def test_all(self):
        """ Verify that all instances were retrieved """
        self.assertTrue(len(self.bm.all.__doc__) > 0)
        all_bm = BaseModel.all()
        assert self.bm in all_bm

    def test_kwargs(self):
        bm1_dict = self.bm.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(self.bm.id, bm2.id)
        self.assertEqual(self.bm.created_at.isoformat(), bm2.created_at)
        self.assertEqual(self.bm.updated_at.isoformat(), bm2.updated_at)

    def test_undefined_input(self):
        """Passing undefined input for args"""
        with self.assertRaises(NameError):
            b = BaseModel(Betsy)

    def test_inf_input(self):
        """Passing infinity input for args"""
        b = BaseModel(float("inf"))
        self.assertEqual(b.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_nan_input(self):
        """Passing NaN input for args"""
        b = BaseModel(float("nan"))
        self.assertEqual(b.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_string_kwargs(self):
        """Passing string input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**"Betty")

    def test_unknown_kwargs(self):
        """Passing unknown input for kwargs"""
        with self.assertRaises(NameError):
            b = BaseModel(**Betsy)

    def test_int_kwargs(self):
        """Passing int input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**1)

    def test_float_kwargs(self):
        """Passing float input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**1.2)

    def test_inf_kwargs(self):
        """Passing float input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**float("inf"))

    def test_nan_kwargs(self):
        """Passing float input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**float("nan"))

    def test_empty_dict(self):
        """Test for empty dict as an arg"""
        b = BaseModel(**{})
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_undefined_dict(self):
        """Test for undefined dict as an arg"""
        with self.assertRaises(NameError):
            b = BaseModel(**{Betty})

    def test_string_dict(self):
        """Test for string dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{"Betsy"})

    def test_int_dict(self):
        """Test for int dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{1})

    def test_float_dict(self):
        """Test for float dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{1.2})

    def test_inf_dict(self):
        """Test for inf dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{float("inf")})

    def test_nan_dict(self):
        """Test for nan dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{float("nan")})

    def test_None(self):
        """Test for None as an arg"""
        b = BaseModel(None)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_manual_kwargs(self):
        """Test for manually entering in kwargs"""
        b = BaseModel(id="74873652-ee4b-4eb4-8b92-6ccd09993bad",
                      created_at="2019-06-28T13:33:31.943447",
                      updated_at="2019-06-28T13:33:31.943460",
                      name="Tu")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "name"))

    def test_manual_kwargs_none(self):
        """Test for manually entering None in kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(id=None,
                          created_at=None,
                          updated_at=None,
                          name=None)
            self.assertTrue(hasattr(b, "id"))
            self.assertTrue(hasattr(b, "created_at"))
            self.assertTrue(hasattr(b, "updated_at"))
            self.assertTrue(hasattr(b, "name"))

    def test_manual_kwargs_int(self):
        """Test for manually entering int in kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(id=1,
                          created_at=1,
                          updated_at=1,
                          name=1)
            self.assertTrue(hasattr(b, "id"))
            self.assertTrue(hasattr(b, "created_at"))
            self.assertTrue(hasattr(b, "updated_at"))
            self.assertTrue(hasattr(b, "name"))

    def test_manual_kwargs_float(self):
        """Test for manually entering float in kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(id=1.1,
                          created_at=1.1,
                          updated_at=1.1,
                          name=1.1)
            self.assertTrue(hasattr(b, "id"))
            self.assertTrue(hasattr(b, "created_at"))
            self.assertTrue(hasattr(b, "updated_at"))
            self.assertTrue(hasattr(b, "name"))

    def test_manual_kwargs_inf(self):
        """Test for manually entering inf in kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(id=float("inf"),
                          created_at=float("inf"),
                          updated_at=float("inf"),
                          name=float("inf"))
            self.assertTrue(hasattr(b, "id"))
            self.assertTrue(hasattr(b, "created_at"))
            self.assertTrue(hasattr(b, "updated_at"))
            self.assertTrue(hasattr(b, "name"))

    def test_manual_kwargs_nan(self):
        """Test for manually entering nan in kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(id=float("nan"),
                          created_at=float("nan"),
                          updated_at=float("nan"),
                          name=float("nan"))
            self.assertTrue(hasattr(b, "id"))
            self.assertTrue(hasattr(b, "created_at"))
            self.assertTrue(hasattr(b, "updated_at"))
            self.assertTrue(hasattr(b, "name"))

    def test_manual_kwargs_unknown(self):
        """Test for manually entering unknown in kwargs"""
        with self.assertRaises(NameError):
            b = BaseModel(id=f,
                          created_at=f,
                          updated_at=f,
                          name=f)
            self.assertTrue(hasattr(b, "id"))
            self.assertTrue(hasattr(b, "created_at"))
            self.assertTrue(hasattr(b, "updated_at"))
            self.assertTrue(hasattr(b, "name"))


if __name__ == "__main__":
    unittest.main()
