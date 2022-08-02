from django.views.generic import ListView, DetailView, CreateView
from .forms import PostForm
from .models import Post

# Create your views here.
# def index(request):
#     context = {}
#     template = loader.get_template('blog/index.html')
#     return HttpResponse(template.render(context, request))


class HomeView(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-post_date']


class ArticleView(DetailView):
    model = Post
    template_name = 'blog/article.html'

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name: str = 'blog/add_post.html'
    # fields = ['title', 'author', 'body']

