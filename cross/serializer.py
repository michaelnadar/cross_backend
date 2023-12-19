# serializers.py

from rest_framework import serializers
from .models import Terms,Language,Price,User,Price_Article

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class TermsSerializer(serializers.ModelSerializer):
    lan = LanguageSerializer()
    class Meta:
        model = Terms
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    lan=LanguageSerializer()
    class Meta:
        model = User
        fields = '__all__'

class Price_ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price_Article
        fields = '__all__'