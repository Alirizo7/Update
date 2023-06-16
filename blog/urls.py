from django.urls import path
from .views import *


urlpatterns = [
    path('textlist/',TextList.as_view(),name='text-list'),
    path('blocklist/',BlockList.as_view(),name='block-list'),
    path('prikons/',PrikonsList.as_view(),name='prikons'),
    path('prikonstruktor/',PrikonstruktorList.as_view(),name='prikonstruktor'),
    path('faqlist/',FaqList.as_view(),name='faq-list'),
    path('constanswer/',ConstAnswerList.as_view(),name='const-answer'),
    path('portfolio/',PortFolioSerializer.as_view(),name='portfolio'),
]