#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.bm = BaseModel()

    def test_class_and_module_docstrings(self):
        self.assertTrue(len(self.bm.__doc__) > 0)

    def test_init(self):
        self.assertIsInstance(self.bm.id, str)
        self.assertIsInstance(self.bm.created_at, datetime)
        self.assertIsInstance(self.bm.updated_at, datetime)

    def test_str(self):
        bm_str = str(self.bm)
        self.assertIn("[BaseModel]", bm_str)
        self.assertIn("'id':", bm_str)
        self.assertIn("'created_at':", bm_str)
        self.assertIn("'updated_at':", bm_str)

    def test_save(self):
        old_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(old_updated_at, self.bm.updated_at)

    def test_to_dict(self):
        bm_dict = self.bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertIn('id', bm_dict)
        self.assertIn('created_at', bm_dict)
        self.assertIn('updated_at', bm_dict)
        self.assertIn('__class__', bm_dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')

    def test_from_dict(self):
        bm_dict = self.bm.to_dict()
        bm2 = BaseModel(**bm_dict)
        self.assertIsInstance(bm2, BaseModel)
        self.assertEqual(bm2.id, self.bm.id)
        self.assertEqual(bm2.created_at, self.bm.created_at)
        self.assertEqual(bm2.updated_at, self.bm.updated_at)

    def test_json(self):
        bm_dict = self.bm.to_dict()
        bm_json = json.dumps(bm_dict)
        self.assertIsInstance(bm_json, str)
        bm_dict2 = json.loads(bm_json)
        self.assertIsInstance(bm_dict2, dict)
        self.assertEqual(bm_dict2, bm_dict)

    def test_all(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm_list = BaseModel.all()
        self.assertIsInstance(bm_list, list)
        self.assertIn(bm1, bm_list)
        self.assertIn(bm2, bm_list)

    def test_delete(self):
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm_id = bm1.id
        bm1.delete()
        self.assertNotIn(bm1, BaseModel.all())
        self.assertIn(bm2, BaseModel.all())
        bm3 = BaseModel()
        bm3.id = bm_id
        self.assertEqual(bm3.id, bm_id)
        self.assertNotIn(bm3, BaseModel.all())

    def test_kwargs(self):
        bm1_dict = self.bm.to_dict()
        bm2 = BaseModel(**bm1_dict)
        self.assertEqual(self.bm.id, bm2.id)
        self.assertEqual(self.bm.created_at, bm2.created_at)
        self.assertEqual(self.bm.updated_at, bm2.updated_at)

    def test_00_class_type(self):
        """Test for correct class type"""
        b = BaseModel()
        self.assertEqual(b.__class__.__name__, "BaseModel")

    def test_00a_class_invalid(self):
        """Test for invalid class type"""
        with self.assertRaises(NameError):
            b = FunModel()

    def test_01_no_args(self):
        """Test for no arguments passed into BaseModel"""
        b = BaseModel()
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_02_correct_types_in_args(self):
        """Test for correct types in args"""
        b = BaseModel()
        self.assertEqual(type(b.id), str)
        self.assertEqual(b.created_at.__class__.__name__, "datetime")
        self.assertEqual(b.updated_at.__class__.__name__, "datetime")

    def test_03_adding_extra_parameters(self):
        """Test for manually adding parameters to empty BaseModel"""
        b = BaseModel()
        b.string = "Tu"
        b.number = 1106
        b.list = [1, 2, 3]
        b.dict = {"a": 1}
        self.assertTrue(hasattr(b, "string"))
        self.assertTrue(hasattr(b, "number"))
        self.assertTrue(hasattr(b, "list"))
        self.assertTrue(hasattr(b, "dict"))
        self.assertEqual(type(b.string), str)
        self.assertEqual(type(b.number), int)
        self.assertEqual(type(b.list), list)
        self.assertEqual(type(b.dict), dict)

    def test_04_str(self):
        """Test to validate __str__ method is working properly"""
        b = BaseModel()
        p = r'(^\[BaseModel]) (\(\w{8}-\w{4}-\w{4}-\w{4}-\w{12}\)) (\{.*}$)'
        prog = re.compile(p)
        match = prog.match(str(b))
        self.assertTrue(match is not None)

    def test_05_save(self):
        """Test to validate that updated_at is changed when saved"""
        b = BaseModel()
        first_time = b.updated_at
        sleep(.5)
        b.save()
        second_time = b.updated_at
        self.assertNotEqual(first_time, second_time)

    def test_06_to_dict(self):
        """Test to validate to_dict is outputting correctly"""
        b = BaseModel()
        b.name = "Tu"
        b.number = 1987
        d = b.to_dict()
        self.assertTrue('number' in d)
        self.assertTrue('name' in d)
        self.assertTrue('id' in d)
        self.assertTrue('created_at' in d)
        self.assertTrue('updated_at' in d)
        self.assertTrue('__class__' in d)

    def test_06a_to_dict_values(self):
        """Test to validate to_dict values are all strings"""
        b = BaseModel()
        b.name = "Tu"
        b.number = 1987
        d = b.to_dict()
        self.assertEqual(type(d['name']), str)
        self.assertEqual(type(d['number']), int)
        self.assertEqual(type(d['created_at']), str)
        self.assertEqual(type(d['updated_at']), str)
        self.assertEqual(type(d['id']), str)
        self.assertEqual(type(d['__class__']), str)

    def test_07_recreate_instance(self):
        """Test to create instances from to_dict"""
        b = BaseModel()
        b.name = "Tim"
        b.number = 1993
        d = b.to_dict()
        new_b = BaseModel(**d)
        self.assertEqual(b.id, new_b.id)
        self.assertEqual(b.created_at, new_b.created_at)
        self.assertEqual(b.updated_at, new_b.updated_at)
        self.assertEqual(b.name, new_b.name)
        self.assertEqual(b.number, new_b.number)
        self.assertEqual(type(new_b.id), str)
        self.assertEqual(new_b.created_at.__class__.__name__, "datetime")
        self.assertEqual(new_b.updated_at.__class__.__name__, "datetime")
        self.assertTrue(b is not new_b)

    def test_07a_string_input(self):
        """Passing a string for args"""
        b = BaseModel("Betty")
        self.assertEqual(b.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_07b_undefined_input(self):
        """Passing undefined input for args"""
        with self.assertRaises(NameError):
            b = BaseModel(Betsy)

    def test_07c_inf_input(self):
        """Passing infinity input for args"""
        b = BaseModel(float("inf"))
        self.assertEqual(b.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_07d_nan_input(self):
        """Passing NaN input for args"""
        b = BaseModel(float("nan"))
        self.assertEqual(b.__class__.__name__, "BaseModel")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_07e_string_kwargs(self):
        """Passing string input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**"Betty")

    def test_07f_unknown_kwargs(self):
        """Passing unknown input for kwargs"""
        with self.assertRaises(NameError):
            b = BaseModel(**Betsy)

    def test_07g_int_kwargs(self):
        """Passing int input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**1)

    def test_07h_float_kwargs(self):
        """Passing float input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**1.2)

    def test_07i_inf_kwargs(self):
        """Passing float input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**float("inf"))

    def test_07j_nan_kwargs(self):
        """Passing float input for kwargs"""
        with self.assertRaises(TypeError):
            b = BaseModel(**float("nan"))

    def test_08_empty_dict(self):
        """Test for empty dict as an arg"""
        b = BaseModel(**{})
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_08a_undefined_dict(self):
        """Test for undefined dict as an arg"""
        with self.assertRaises(NameError):
            b = BaseModel(**{Betty})

    def test_08b_string_dict(self):
        """Test for string dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{"Betsy"})

    def test_08c_int_dict(self):
        """Test for int dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{1})

    def test_08d_float_dict(self):
        """Test for float dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{1.2})

    def test_08e_inf_dict(self):
        """Test for inf dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{float("inf")})

    def test_08e_nan_dict(self):
        """Test for nan dict as an arg"""
        with self.assertRaises(TypeError):
            b = BaseModel(**{float("nan")})

    def test_09_None(self):
        """Test for None as an arg"""
        b = BaseModel(None)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))

    def test_10_manual_kwargs(self):
        """Test for manually entering in kwargs"""
        b = BaseModel(id="74873652-ee4b-4eb4-8b92-6ccd09993bad",
                      created_at="2019-06-28T13:33:31.943447",
                      updated_at="2019-06-28T13:33:31.943460",
                      name="Tu")
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        self.assertTrue(hasattr(b, "name"))

    def test_10a_manual_kwargs_none(self):
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

    def test_10b_manual_kwargs_int(self):
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

    def test_10c_manual_kwargs_float(self):
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

    def test_10d_manual_kwargs_inf(self):
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

    def test_10e_manual_kwargs_nan(self):
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

    def test_10e_manual_kwargs_unknown(self):
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
