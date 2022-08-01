from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    context = {}
    template = loader.get_template('home/index.html')
    return HttpResponse(template.render(context, request))