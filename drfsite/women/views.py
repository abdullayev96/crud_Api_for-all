from django.shortcuts import render
from django.forms import model_to_dict
from rest_framework.response import Response
from .serializers import WomenSerializer
from .models import Women
from rest_framework import generics
from rest_framework.generics import ListCreateAPIView,RetrieveDestroyAPIView, ListAPIView, RetrieveAPIView

from rest_framework.views import APIView


class WomenApiView(APIView):
    def get(self, request):
        # lst = Women.objects.all().values()
        # return Response({'posts':list(lst)})
        w = Women.objects.all()
        return Response({'posts':WomenSerializer(w, many=True).data})    #### many ga False qimmat bersak nima boladi AttributeError: Got AttributeError when attempting to get a value for field `title` on serializer `
                                                                                # WomenSerializer`.The serializer field might be named incorrectly and not match any attribute or key on the `QuerySet` instance.
                                                                                # Original exception text was: 'QuerySet' object has no attribute 'title'.

    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # post_new = Women.objects.create(
        #     title = request.data['title'],
        #     content = request.data['content'],
        #     cat_id = request.data['cat_id'],
        # )
        # print(post_new)

        return Response({"posts": serializer.data})   #### data berilmasa   ###TypeError: Object of type WomenSerializer is not JSON serializable


    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Put not allowed"})
        try:
            instance = Women.objects.get(pk=pk)
        except:
            return Response({"error": "Objects not exists"})

        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"posts": serializer.data})


    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error": "Method Delete not allowed"})

        return Response({"posts":" Don't delete post now  " +str(pk)})













# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class CategoryAPIView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class WomenList(ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

######   delete, and create

# class WomenList(ListCreateAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenDetail(RetrieveAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer

# class WomenDetail(RetrieveDestroyAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
# #
# class CategoryList(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

# class CategoryDetail(RetrieveAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer


# class CategoryDetail(RetrieveDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

##### create and get tanlab olish


# class WomenAPIView(ListCreateAPIView):   ####  bu api ni ozidan qoshish imkoni beradi api ga
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class WomenDetail(RetrieveAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
#
# class CategoryAPIView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#
# class CategoryDetail(RetrieveAPIView):      ##### yakka holda chiqarib beradi
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer

