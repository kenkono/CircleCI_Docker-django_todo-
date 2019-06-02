from django.test import TestCase
from todo_list.forms import TodoForm
from todo_list.models import Todo


class TodoFormTests(TestCase):
    def test_valid(self):
        """正常な入力を行えばエラーにならないことを検証"""
        params = dict(title='test', text='this is a test')
        form = TodoForm(params, instance=Todo())
        self.assertTrue(form.is_valid())

    def test_either1(self):
        """何も入力しなければエラーになることを検証"""
        params = dict()
        form = TodoForm(params, instance=Todo())
        self.assertFalse(form.is_valid())
