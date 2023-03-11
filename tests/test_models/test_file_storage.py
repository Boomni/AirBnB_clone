import os
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def tearDown(self):
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        # Before adding any object, __objects should be empty
        self.assertEqual(self.storage.all(), {})
        # After adding an object, __objects should contain one item
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_new(self):
        # Adding a new object should increase the number of items in __objects
        self.assertEqual(len(self.storage.all()), 0)
        self.storage.new(self.model)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_reload(self):
        # Saving and reloading should not change the number of items in __objects
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_file_exists(self):
        # Saving should create the file if it doesn't exist
        self.storage.new(self.model)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload_file_not_found(self):
        # If the file doesn't exist, reload should not change __objects
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_invalid_json(self):
        # If the file contains invalid JSON, reload should not change __objects
        with open(FileStorage._FileStorage__file_path, "w") as f:
            f.write("{invalid json}")
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 0)

    def test_reload_obj_creation(self):
        # After reloading, __objects should contain instances of the correct classes
        user = User()
        self.storage.new(user)
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all()
        key = "{}.{}".format(user.__class__.__name__, user.id)
        self.assertTrue(key in objs)
        self.assertTrue(isinstance(objs[key], User))


if __name__ == '__main__':
    unittest.main()
