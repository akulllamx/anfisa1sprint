from django.shortcuts import render


def index(request):
    template = 'homepage/index.html'
    # template = 'html_templates/index.html'
    return render(request, template)
