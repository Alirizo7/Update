from .models import *
from rest_framework import serializers


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ('id','text')

class BlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Block
        fields = ('id','subtitle','time','price')

class PrikonsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prikons
        fields = ('id','text')

class PrikonstruktorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriKonstruktor
        fields = ('id','title','text')

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields  = ('id','title','text')

class ConsAnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsAnswers
        fields = ('id','name','types','price')


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


        

