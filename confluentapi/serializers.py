from django.contrib.auth.models import User
from rest_framework import serializers
from confluentapi.models import Page


class UserSerializer(serializers.HyperlinkedModelSerializer):
    pages = serializers.HyperlinkedRelatedField(many=True, view_name='page-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'pages', ]


class PageSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    html_url = serializers.HyperlinkedIdentityField(view_name='page-html', format='html')

    class Meta:
        model = Page
        fields = ['url', 'id', 'html_url', 'title', 'markdown', 'html', 'owner', 'created', ]
