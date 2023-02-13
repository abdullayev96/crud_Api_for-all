from rest_framework import serializers
import io
from .models import Women, Category
from rest_framework.serializers import ModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content

class WomenSerializer(serializers.Serializer):
    # title = serializers.CharField(max_length=300)
    # content = serializers.CharField()

    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()

#### new

    def create(self, validated_data):
        return Women.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_update = validated_data.get('time_update', instance.time_update)
        instance.is_published =  validated_data.get('is_published', instance.is_published)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        instance.save()
        return instance









# def encode():
#     model  = WomenModel('Dennis Ivy', 'Content: Dennis Ivy')
#     model_sr  = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json= JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Dennis Ivy","content":"Content: Dennis Ivy"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)



# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'content', 'time_create','time_update',  'cat_id')

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"
#
#
# class WomenSerializer(ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ('title', 'content', 'time_create','time_update',  'cat_id')
#
# class CategorySerializer(ModelSerializer):
#     class Meta:
#         model = Category
#         fields = "__all__"


