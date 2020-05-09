from django.shortcuts import render
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics , mixins


class ProductGeneric(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin, mixins.DestroyModelMixin):
    search_fields = ['item', 'price']
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id=None):
        return self.destroy(request, id)



class ProductApi(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.http_204)
        return Response(serializer.errors, status = status.http_400_)


class ProductDetail(APIView):
    def get_detail(self, id):
        try:
            product = Product.objects.get(id = id)
        except Product.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        product = self.get_detail(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, id):
        product = self.get_detail(id)
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        product = self.get_detail(id)
        product.delete()
        return Response(status = status.HTTP_404_NOT_FOUND)
