from django.db.models import *

import os

import django
from django.test import TestCase

# Create your tests here.
from myapp import predict

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'back.settings')
django.setup()

from myapp.models import *

posts = Post.objects.all()
for post in posts:
    post.post_senti = predict.senti(post.post_content)
    post.post_keywords = predict.ner(post.post_content)
    post.save()
