from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from confluentapi.models import Page


class Login(APIView):
    # permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        template = loader.get_template(self.template_name)
        return HttpResponse(template.render())

    def post(self, request):
        template = loader.get_template(self.template_name)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('web-page-list')
        else:
            return redirect('web-login')


class Logout(APIView):

    def get(self, request):
        logout(request)
        messages.add_message(self.request, messages.SUCCESS, 'You have been logged out.')
        return redirect('web-login')


class PageList(APIView):
    # permission_classes = (IsAuthenticated,)
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
