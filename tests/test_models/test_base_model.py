#!/usr/bin/env python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.bm = BaseModel()

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
