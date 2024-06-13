from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Problem
from .serializers import ProblemSerializer
from .utils import generate_signed_url
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView
)
import requests
from io import BytesIO
import base64
import os
from django.conf import settings
import random
from django.http import JsonResponse
from django.views import View
from .firebase import db


class ListProblemsView(ListCreateAPIView):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title', 'price', 'stock', 'rating', 'category','date_created','favorite']
    ordering_fields = ['title', 'price', 'stock', 'rating', 'category','date_created']
    search_fields = ['title', 'price', 'stock', 'rating', 'category','date_created']
    
    
    def create(self, request, *args, **kwargs):
        product_data = request.data
        serializer = ProblemSerializer(data=product_data)
        if serializer.is_valid():
            image_url = generate_signed_url('applied_ml', object_name=serializer.validated_data['title'])
            product_data['image'] = image_url
            serializer.save()
            serializer.validated_data['image'] = image_url
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_queryset(queryset)
        return queryset
    
    def get(self, request):
        problems_ref = db.collection('problems')
        docs = problems_ref.stream()
        problems = [doc.to_dict() for doc in docs]
        return JsonResponse(problems, safe=False, status=200)
class AddProductView(View):
    def post(self, request):
        data = request.POST
        product_ref = db.collection('products').document()
        product_ref.set({
            'title': data.get('title'),
            'price': data.get('price'),
            'stock': data.get('stock'),
            'category': data.get('category')
        })
        return JsonResponse({'status': 'Product added successfully'}, status=201)

class ListProductsView(View):
    def get(self, request):
        products_ref = db.collection('products')
        docs = products_ref.stream()
        products = [doc.to_dict() for doc in docs]
        return JsonResponse(products, safe=False, status=200)



# Create your views here.
# class ProductViewSet(viewsets.ModelViewSet) : 
#     queryset = Product.objects.all() 
#     serializer_class = ProductSerializer
    
# class ProductCreateView(APIView) : 
#     def post(self, request):
#         products_data = request.data.get("products",[])
#         serializer = ProductSerializer(data=products_data, many=True)
#         if serializer.is_valid():
#             # print(serializer)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class ProductCategoryView(APIView) : 
#     def get(self, request, category) : 
#         products = Product.objects.filter(category=category) 
        
#         serializer = ProductSerializer(products, many=True) 
        
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
class SolveProblem(APIView):
    def post(self, request, *args, **kwargs) : 
        description = request.data.get("description",None) 
        image_data = request.data.get("image",None)
                
        if not description or not image_data: 
            return Response({"error": "error no information"}) 
        
        image_content = base64.b64decode(image_data)

        image_path = os.path.join(settings.MEDIA_ROOT, 'images', 'test.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_content)
        

        url = "https://d84b-34-16-163-161.ngrok-free.app" 
        payload = {
            "part" : "upper_body",
            "cloth_name" : cloth_name
        }
        
        files = {'image': open(image_path, 'rb')}
        
        response = requests.post(url,data=payload, files=files)
        print(response.status_code)
        if response.status_code == 200 : 
            encoded_image = response.json()["image"]
            
            response_data = {
                "result": cloth_name,
                "image": encoded_image
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        else : 
            print(f"Error: {response.status_code}")
            print(response.text)
class ListProductView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['title', 'price', 'stock', 'rating', 'category','date_created','favorite']
    ordering_fields = ['title', 'price', 'stock', 'rating', 'category','date_created']
    search_fields = ['title', 'price', 'stock', 'rating', 'category','date_created']
    
    
    def create(self, request, *args, **kwargs):
        product_data = request.data
        serializer = ProductSerializer(data=product_data)
        if serializer.is_valid():
            image_url = generate_signed_url('applied_ml', object_name=serializer.validated_data['title'])
            product_data['image'] = image_url
            serializer.save()
            serializer.validated_data['image'] = image_url
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filter_queryset(queryset)
        return queryset
        
class UpdateDeleteProductView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'product_id'
    
    
    def update(self, request, *args, **kwargs):
        product = self.get_object()
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rating_data = request.data.get('rating', {})
            if rating_data:
                rating_instance = product.rating
                rating_serializer = RatingSerializer(instance=rating_instance, data=rating_data)
                
                if rating_serializer.is_valid():
                    rating_serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        product.delete()
        rating = product.rating
        rating.delete()
        return Response(status=status.HTTP_200_OK)
    
class TryOnView(APIView) : 
    def post(self, request, *args, **kwargs) : 
        cloth_name = request.data.get("cloth_name",None) 
        image_data = request.data.get("image",None)
                
        if not cloth_name or not image_data: 
            return Response({"error": "cloth_name or image is required"}) 
        
        image_content = base64.b64decode(image_data)

        image_path = os.path.join(settings.MEDIA_ROOT, 'images', 'test.jpg')
        with open(image_path, 'wb') as f:
            f.write(image_content)
        

        url = "https://d84b-34-16-163-161.ngrok-free.app" 
        payload = {
            "part" : "upper_body",
            "cloth_name" : cloth_name
        }
        
        files = {'image': open(image_path, 'rb')}
        
        response = requests.post(url,data=payload, files=files)
        print(response.status_code)
        if response.status_code == 200 : 
            encoded_image = response.json()["image"]
            
            response_data = {
                "result": cloth_name,
                "image": encoded_image
            }
            
            return Response(response_data, status=status.HTTP_200_OK)
        else : 
            print(f"Error: {response.status_code}")
            print(response.text)

class RecommendationView(APIView) : 
    def post(self, request, *args, **kwargs) : 
        cloth_description = request.data.get("description",None) 
        
        if not cloth_description: 
            return Response({"error": "cloth_description is required"}) 
        
        cloth_description = cloth_description.split(",")
        
        url = "https://a842-34-125-126-162.ngrok-free.app"
        payload = {
            "cloth_description" : random.choice(cloth_description)
        }
        print(payload)
        response = requests.post(url, data=payload)
        print(response.status_code) 
        if response.status_code == 200 : 
            results = response.json()["results"]
            
            response_data = {"results" : results}
        
            return Response(response_data, status=status.HTTP_200_OK)
        else : 
            print(f"Error: {response.status_code}")
            print(response.text)
        
        
          
                
        