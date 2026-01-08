from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Note


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Note
        fields = ['url', 'id', 'title', 'content', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    note = serializers.HyperlinkedRelatedField(
        many=True, view_name='note-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'note']
