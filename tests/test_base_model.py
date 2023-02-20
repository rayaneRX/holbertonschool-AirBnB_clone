import unittest

from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_save(self):
        model = BaseModel()
        model_saved = model.save()
        self.assertNotEqual(model.updated_at, model_saved)

    def test_to_dict(self):
        model = BaseModel()
        self.assertEqual(type(model.to_dict()), dict)

    def test_id(self):
        model_1 = BaseModel()
        model_2 = BaseModel()
        self.assertNotEqual(model_1.id, model_2.id)

    def test_created_at(self):
        model = BaseModel()
        created_date = model.created_at
        model.save()
        check_create_date = model.created_at
        self.assertEqual(created_date, check_create_date)

    def test_str(self):
        model = BaseModel()
        self.assertEqual(model.__str__(), f"[BaseModel] ({model.id}) {model.__dict__}")
        """ self.assertEqual(type(model.__str__()), str) """
