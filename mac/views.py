from django.http import HttpResponse

def index(request):
    text = '''<h1><a href = '/blog'>Blog</a><br>
            <a href = '/shop'>Shop</a><br></h1>'''
    return HttpResponse(text)