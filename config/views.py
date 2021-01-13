from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    html = "<html><body>Hello</body></html>"
    return HttpResponse(html)

def template_test(request):
    return render(request, 'test.html')
