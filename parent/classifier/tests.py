from django.test import TestCase
from classifier.models import Image

# Create your tests here.

# As the project grows, these can be separated into
# diferent files called test_models.py, test_views.py, test_forms.py


class ImageTestCase(TestCase):
    def setUp(self):
        Image.objects.create(
            name="test_image",
            url="http://www.example.com",
            data="../32948561978_746ed6b5ae_o_9H3LRWP.jpg",
            category="Mo",
        )
        Image.objects.create(
            name="test_image_2",
            url="http://www.example.com",
            data="../32948561978_746ed6b5ae_o_9H3LRWP.jpg",
            category="Ur",
        )


def test_image_model(self):
    image_1 = Image.objects.get(name="test_image")
    image_2 = Image.objects.get(name="test_image_2")
    self.assertEqual(image_1.category, "Mountain")
    self.assertEqual(image_2.category, "Urban")
    self.assertEqual(str(image_1), "test_image")
    self.assertEqual(str(image_2), "test_image_2")
