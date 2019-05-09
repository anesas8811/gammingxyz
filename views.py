from django.http import HttpResponse
from django import get_version

source = 'https://github.com/zeit/now-examples/tree/master/python-django'
css = '<link rel="stylesheet" href="/css/style.css" />'

def index(request):
    return HttpResponse("%s<h1>Welcome to gaming.xyz</h1><p>Want To Buy This Domain ?  Contact me ! Price Negotiable !</p><p>Contact me <a href='https://www.facebook.com/mrvincere1'>Here ! </a> </p>" % (css, source), content_type='text/html')
