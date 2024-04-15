from django.urls import path
from testing import views

urlpatterns = [
    path('tests/', views.TestViewSet.as_view({'get': 'list'})),
    path('tests/<int:pk>/', views.TestViewSet.as_view({'get': 'retrieve'})),
    path('tests/<int:pk>/complete/', views.CompleteTestView.as_view()),
    path('tests/completed/', views.CompletedTestView.as_view({'get': 'list'})),
    path('user/', views.UserView.as_view()),
]
