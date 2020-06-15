from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from confluentapi.models import Page


class PageList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'page_list.html'

    def get(self, request):
        queryset = Page.objects.all()
        return Response({'pages': queryset})


class PageDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'page_detail.html'

    def get(self, request, pk):
        queryset = Page.objects.get(pk=pk)
        return Response({'page': queryset})
