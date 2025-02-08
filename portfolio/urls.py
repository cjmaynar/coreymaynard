from django.urls import path

from .views import PortfolioList, PortfolioDetail

urlpatterns = [
    path('', PortfolioList.as_view(), name='portfolio_index'),
    path('<slug:slug>/', PortfolioDetail.as_view(), name='portfolio_detail'),
]
