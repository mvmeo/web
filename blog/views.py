from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
# def index(request):
#     context = {}
#     template = loader.get_template('blog/index.html')
#     return HttpResponse(template.render(context, request))


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-id']


class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'