from rest_framework import serializers
from .models import Snippet, LANGUAGE_CHOICE, STYLE_CHOICE
from django.contrib.auth.models import User

# class SnippetSerializer(serializers.Serializer):
#     id=serializers.IntegerField(read_only=True)
#     title=serializers.CharField(allow_blank=True,required=False,max_length=100)
#     code=serializers.CharField(style={'base_template':'textarea.html'})
#     linenos=serializers.BooleanField(required=False)
#     language=serializers.ChoiceField(choices=LANGUAGE_CHOICE,default="python")
#     style=serializers.ChoiceField(choices=STYLE_CHOICE,default="friendly")

#     def create(self, validated_data):
#         return Snippet.objects.create(**validated_data)

#     def update(self,instance, validated_data):
#         instance.title=validated_data.get("title", instance.title)
#         instance.code = validated_data.get("code", instance.code)
#         instance.linenos = validated_data.get("linenos", instance.linenos)
#         instance.language = validated_data.get("language", instance.language)
#         instance.style = validated_data.get("style", instance.style)
#         instance.save()
#         return instance

# Using model serializer

# class SnippetSerializer(serializers.ModelSerializer):
#     owner=serializers.ReadOnlyField(source="owner.username")
#     class Meta:
#         model=Snippet
#         fields=["id","title","code","linenos","language","style","owner"]


# class UserSerializer(serializers.ModelSerializer):
#     snippets=serializers.PrimaryKeyRelatedField(many=True,queryset=Snippet.objects.all())
#     class Meta:
#         model=User
#         fields=['id','username','snippets']


# using hyperlinkedmodelserialzer

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    highlight = serializers.HyperlinkedIdentityField(
        view_name="snippet-highlight", format="html")

    class Meta:
        model = Snippet
        fields = ["url", "id", "highlight", "title",
                  "code", "linenos", "language", "style", "owner"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name="snippet-detail",  read_only=True)
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
