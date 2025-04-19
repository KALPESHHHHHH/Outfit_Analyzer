# # outfit_recommender/core/urls.py

# from django.urls import path
# from . import views
# from .views import home 
# app_name = 'core'

# urlpatterns = [
#     path('', views.home, name='home'),  # Homepage
#     path('upload/', views.upload, name='upload'),  # Upload outfit image
#     path('recommendations/', views.recommendations, name='recommendations'),  # Recommendation list
#     path('recommendations/<int:pk>/', views.recommendation_detail, name='recommendation_detail'),  # Detail view
#     path('about/', views.about, name='about'),  # About page
# ]


from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('upload/', views.upload, name='upload'),  # Upload outfit image
    path('recommendations/', views.recommendations, name='recommendations'),  # Recommendation list
    path('recommendations/<int:pk>/', views.recommendation_detail, name='recommendation_detail'),  # Detail view
    path('about/', views.about, name='about'),  # About page
    path('fashion_feedback/', views.fashion_feedback_view, name='fashion_feedback'),  # Fashion feedback API
]
