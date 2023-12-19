from django.urls import path
from .views import TermsView,PriceView

urlpatterns = [
    path('terms', TermsView.as_view(), name='terms'),
    path('price', PriceView.as_view(), name='price')
]
