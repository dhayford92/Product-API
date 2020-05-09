from django.urls import path
from .views import ProductApi, ProductDetail , ProductGeneric

urlpatterns = [
    path('product/', ProductApi.as_view()),
    path('generic/', ProductGeneric.as_view()),
    path('detailgenic/<int:id>/', ProductGeneric.as_view()),
    path('detail/<int:id>/', ProductDetail.as_view()),
]
