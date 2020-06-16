from confluentapi.models import Page


def navbar(request):
    queryset = Page.objects.all()
    return {
        'pages': queryset,
    }