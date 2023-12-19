from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Terms,Price,User,Price_Article
from .serializer import TermsSerializer,PriceSerializer,UserSerializer,Price_ArticleSerializer
from rest_framework import serializers

# Create your views here.
class TermsView(APIView):
    def get(self, request):
        terms_data = Terms.objects.select_related('lan').all()
        queryset_list = list(terms_data)
        
        
        serializer = TermsSerializer(terms_data, many=True)
        # print(serializer.data)
        final = serializer.data[0]
        return Response(final, status=status.HTTP_200_OK)


class PriceView(APIView):
    def get(self,request):
        User_data = User.objects.select_related('lan').get(name="John Andre")
        user = UserSerializer(User_data)   
        Price_data = Price.objects.get(lan=User_data.lan.id)
        price = PriceSerializer(Price_data)
        Price_Article_data = Price_Article.objects.filter(lan=User_data.lan.id,user=User_data.id)
        price_article = Price_ArticleSerializer(Price_Article_data,many=True)
        final_page = {
            'user':user.data,
            'price_page':price.data,
            'price_article':price_article.data
        }
        print(final_page)
        return Response(final_page, status=status.HTTP_200_OK)
