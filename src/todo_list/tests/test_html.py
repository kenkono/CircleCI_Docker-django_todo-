from todo_list.tests.setup import SetUpDatabase


class HtmlTests(SetUpDatabase):
    def test_index_page_returns_correct_html(self):
        """index.htmlが使用されるかを検証"""
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'todo_list/inde.html')

    def test_detail_page_returns_correct_html(self):
        """detail.htmlが使用されるかを検証"""
        response = self.c.get('/' + str(self.todo.id))
        self.assert_contains_title_text(response, self.todo.title, self.todo.text, status_code=200)
        self.assertTemplateUsed(response, 'todo_list/detail.html')

    def test_new_todo_page_returns_correct_html(self):
        """new_todo.htmlが使用されるかを検証"""
        response = self.c.get('/new_todo')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list/new_todo.html')

    def test_edit_todo_page_returns_correct_html(self):
        """edit_todo.htmlが使用されるかを検証"""
        response = self.c.get('/edit_todo/' + str(self.todo.id))
        self.assert_contains_title_text(response, self.todo.title, self.todo.text, status_code=200)
        self.assertTemplateUsed(response, 'todo_list/edit_todo.html')
