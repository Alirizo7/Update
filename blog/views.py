from django.shortcuts import render
from rest_framework import generics
from .serializers import *

# Create your views here.

# class ProductList(generics.ListAPIView):
#     queryset = Text.objects.all()
#     serializer_class = TextList


class TextList(generics.ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer

class BlockList(generics.ListAPIView):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer

class PrikonsList(generics.ListAPIView):
    queryset = Prikons.objects.all()
    serializer_class = PrikonsSerializer

class PrikonstruktorList(generics.ListAPIView):
    queryset = PriKonstruktor.objects.all()
    serializer_class = PrikonstruktorSerializer

class FaqList(generics.ListAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class ConstAnswerList(generics.ListAPIView):
    queryset = ConsAnswers.objects.all()
    serializer_class = ConsAnswersSerializer

class PortFolioSerializer(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


    
    



