from django.test import TestCase
from django.contrib.auth.models import User

from .models import User, Post, Comment, Like
from .factories import UserFactory, PostFactory, CommentFactory, LikeFactory

class TestModels(TestCase):
    def test_user_creation(self):
        user = UserFactory()
        self.assertTrue(isinstance(user, User))

    def test_post_creation(self):
        post = PostFactory()
        self.assertTrue(isinstance(post, Post))

    def test_comment_creation(self):
        comment = CommentFactory()
        self.assertTrue(isinstance(comment, Comment))

    def test_like_creation(self):
        like = LikeFactory()
        self.assertTrue(isinstance(like, Like))




