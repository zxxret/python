from views.view import View
from controller.controller import Controller
from models.article import Article
from services.db import Db

class ArticlesController(Controller):
    

    def index(self, request, response):
        articles = Article.find_all()
        response.text = self.view.render_html('articles/articles.html', {'title' : 'MVC фреймворк ', 'h1' : 'Статья: ', 'articles' : articles})

    # def about(self, request, response):
    #     response.text = self.view.render_html('site/about.html', {'title' : 'О нас', 'h1' : 'Вы на странице "о нас"'})

    def view(self, request, response, id):
        article = Article.get_by_id(id)
        if article is None:
            response.status_code = 404
            response.text = self.view.render_html('errors/404.html', {'error' : 'Статья не найдена'})
            return
            
            
        response.text = self.view.render_html('articles/view.html', {'title' : f'MVC фреймворк - {article.get_name()}', 'h1' : f'Статья: {article.get_name()}', 'article' : article})
    
    def edit(self, request, response, id):
        article = Article.get_by_id(id)
        if article is None:
            response.status_code = 404
            response.text = self.view.render_html('errors/404.html', {'error' : 'Статья не найдена'})
            return
        if request.method == 'POST':
            article.set_name(request.POST['name'])
            article.set_text(request.POST['text'])
            article.save()
            response.status_code = 302
            response.headers = [('Location', f'/article/{article.get_id()}')]
            return

        response.text = self.view.render_html('articles/edit.html', {'title' : f'Редактирование - {article.get_name()}', 'article' : article})
    
    def add(self, request, response):
        article = Article()
        article.set_author_id(1)
        article.set_name('Новая статья')
        article.set_text('dsadsa')

        article.save()

    def delete(self, request, response, id):
        article = Article.get_by_id(id)
        if article is None:
            response.status_code = 404
            response.text = self.view.render_html('errors/404.html', {'error' : 'Статья не найдена'})
            return
        
        article.delete()
        response.status_code = 302
        response.headers = [('Location', '/articles')]

    
    


