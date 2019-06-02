from django.test import TestCase
from todo_list.models import Todo


class TodoModelTests(TestCase):
    @staticmethod
    def creating_a_todo_and_saving(title=None, text=None):
        todo = Todo()
        if title is not None:
            todo.title = title
        if text is not None:
            todo.text = text
        todo.save()

    def test_is_empty(self):
        """空の場合、中身が0であることをを検証"""
        self.assertEqual(Todo.objects.all().count(), 0)

    def test_is_not_empty(self):
        """Noneの場合、中身が1であることを検証"""
        self.creating_a_todo_and_saving()
        self.assertEqual(Todo.objects.all().count(), 1)

    def test_saving_and_retrieving_todo(self):
        """データ挿入の際、保存がうまくいくかを検証"""
        title, text = 'test', 'this is a test'
        self.creating_a_todo_and_saving(title, text)
        actual_todo = Todo.objects.last()
        self.assertEqual(actual_todo.title, title)
        self.assertEqual(actual_todo.text, text)
