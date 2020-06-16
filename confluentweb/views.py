from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from confluentapi.models import Page


def index(request):
    return render(request, template_name='index.html')


class Login(APIView):
    # permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'login.html'

    def get(self, request):
        return render(request, template_name=self.template_name)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('web-index')
        else:
            return redirect('web-login')


class Logout(APIView):

    def get(self, request):
        logout(request)
        messages.add_message(self.request, messages.SUCCESS, 'You have been logged out.')
        return redirect('web-login')


class PageDetail(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'page_detail.html'

    def get(self, request, pk):
        queryset = Page.objects.get(pk=pk)
        return Response({'page': queryset})
