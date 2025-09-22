from django.shortcuts import render


def description(request):
    template = 'about/description.html'
    # template = 'html_templates/about.html'
    return render(request, template)
