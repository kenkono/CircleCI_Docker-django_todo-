from todo_list.tests.setup import SetUpDatabase
from todo_list.models import Todo


class CanSaveAPostRequestTests(SetUpDatabase):
    def test_edit_todo_can_save_a_post_request(self):
        """編集の際、保存がうまくいくかを検証"""
        title, text, todo_id = 'test1', 'this is a test1', self.todo.id
        self.c.post('/edit_todo/' + str(self.todo.id), {'title': title, 'text': text})
        response = self.c.get('/' + str(self.todo.id))
        self.assert_contains_title_text(response, title, text, status_code=200)

    def test_new_todo_can_save_a_post_request(self):
        """新規の際、保存がうまくいくかを検証"""
        title, text = 'test2', 'this is a test2'
        self.c.post('/new_todo', {'title': title, 'text': text})
        todo_id = Todo.objects.last().id
        response = self.c.get('/' + str(todo_id))
        self.assert_contains_title_text(response, title, text, status_code=200)
