from django.test import TestCase
from .models import Post


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(title="django", content="django",
                                        date_posted="2021-01-28", author="user")


def test_post_model(self):
    d = self.blog
    self.assertTrue(isinstance(d, Post))
    self.assertEqual(str(d), 'django')
