from django.urls import resolve
from todo_list.views import index, detail, new_todo, delete_todo, edit_todo
from todo_list.tests.setup import SetUpDatabase


class UrlResolveTests(SetUpDatabase):
    def test_url_resolves_to_index_view(self):
        """/では、indexが呼び出される事を検証"""
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_url_resolves_to_detail_view(self):
        """/todo.id/では、detailが呼び出される事を検証"""
        found = resolve('/' + str(self.todo.id))
        self.assertEqual(found.func, detail)

    def test_url_resolves_to_new_todo_view(self):
        """/new_todo/では、new_todoが呼び出される事を検証"""
        found = resolve('/new_todo')
        self.assertEqual(found.func, new_todo)

    def test_url_resolves_to_delete_todo_view(self):
        """delete_todo/todo.id/では、delete_todoが呼び出される事を検証"""
        found = resolve('/delete_todo/' + str(self.todo.id))
        self.assertEqual(found.func, delete_todo)

    def test_url_resolves_to_edit_todo_view(self):
        """edit_todo/todo.id/では、edit_todoが呼び出される事を検証"""
        found = resolve('/edit_todo/' + str(self.todo.id))
        self.assertEqual(found.func, edit_todo)
