import unittest
import os.path
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models import storage

# model = BaseModel()
# model.save()


objects = FileStorage._FileStorage__objects
file = FileStorage._FileStorage__file_path


class TestFileStorage(unittest.TestCase):
    def test_file_path(self):
        model = BaseModel()
        model.save()
        """ self.assertEquals(os.path.isfile("file.json"), True) """
        self.assertEquals(file, "file.json")
        os.remove("file.json")

    def test_objects(self):
        model = BaseModel()
        model.save()
        self.assertEqual(type(objects), dict)

    def test_all(self):
        model = BaseModel()
        model.save()
        all_objs = storage.all()
        self.assertEquals(objects, all_objs)

    def test_new(self):
        model = BaseModel()
        FileStorage.new(FileStorage, model)
        self.assertNotEquals(objects[f"{model.__class__.__name__}.{model.id}"], None)

    def test_reload(self):
        obj = objects.copy()
        model = BaseModel()
        FileStorage.reload(FileStorage)
        self.assertNotEqual(obj, objects)
