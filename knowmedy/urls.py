from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('find',views.find,name='find'),
    path('index',views.index,name='index'),
    path('search',views.search,name='search'),
    path('getdisease',views.get_disease,name='getdisease'),
    path('findtub',views.findtub,name='findtub'),
    path('likesincrease',views.likes_increase,name='likesincrease'),
    path('dislikesincrease',views.dislikes_increase,name='dislikesincrease')
]