from rest_framework import serializers
from .models import Problem, Product, Rating

class ProblemSerializer(serializers.ModelSerializer) : 
    class Meta:
        model = Problem
        fields = ['description', 'solve', 'image','file']
        
    def create(self, validated_data):
        problem = Problem.objects.create(**validated_data)
        return problem

# class RatingSerializer(serializers.ModelSerializer) : 
#     class Meta:
#         model = Rating
#         fields = ['rate', 'count']

# class ProductSerializer(serializers.ModelSerializer) : 
#     rating = RatingSerializer(read_only=True)
#     class Meta : 
#         model = Product
#         fields = ['id','title','price','rating','stock','image','description','category','date_created','image_file_name','favorite']
    
#     def create(self, validated_data):
#         # rating_data = validated_data.pop('rating')
#         # rating_instance = Rating.objects.create(**rating_data)
#         # product_instance = Product.objects.create(rating=rating_instance, **validated_data)
#         # return product_instance
#         rating_data = validated_data.pop('rating', None)
#         product = Product.objects.create(**validated_data)
        
#         if rating_data:
#             # Use the RatingSerializer to validate and create the Rating instance
#             rating_serializer = RatingSerializer(data=rating_data)
#             if rating_serializer.is_valid():
#                 rating = rating_serializer.save()
#                 product.rating = rating
#                 product.save()
#             else:
#                 # If Rating data is not valid, raise a validation error
#                 raise serializers.ValidationError({'rating': rating_serializer.errors})

#         return product
       
        