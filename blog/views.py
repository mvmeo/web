from django.http import HttpResponse
from django.template import loader
from django.views.generic import ListView, DetailView, CreateView

from .models import Post

# Create your views here.
# def index(request):
#     context = {}
#     template = loader.get_template('blog/index.html')
#     return HttpResponse(template.render(context, request))


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'


class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'

class AddPostView(CreateView):
    model = Post
    template_name: str = 'blog/add_post.html'
    fields = ['title', 'author', 'body']

