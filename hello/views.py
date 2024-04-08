from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, World")

def nome(request):
    return HttpResponse("Meu nome é Vicencya Nayara")

def relatorio(request):
    return HttpResponse("Seus relatórios estão sendo construídos.")