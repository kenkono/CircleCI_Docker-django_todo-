from django.test import TestCase, Client
from todo_list.models import Todo


class SetUpDatabase(TestCase):
    def __init__(self, *args, **kwargs):
        super(SetUpDatabase, self).__init__(*args, **kwargs)
        self.c = Client()
        self.todo = Todo()

    def setUp(self):
        self.todo.title = 'test'
        self.todo.text = 'this is a test'
        self.todo.save()

    def assert_contains_title_text(self, response, title, text, status_code=200):
        self.assertContains(response, title, status_code=status_code)
        self.assertContains(response, text, status_code=status_code)
