from django.urls import path, re_path
from django_drf_todo_list import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = "django_drf_todo_list"
urlpatterns = [

    path('', views.home, name=''),
    path('index/', views.home, name='index'),
    path('home/', views.home, name='home'),

    # path('api/todo/<int:pk>/', views.todo, name='todo_pk'),
    # path('api/todo/', views.todo, name='todo'),

    re_path(r'^api/todo/(?P<pk>\d+)/$', views.todo, name='todo_pk'),  # GET(one) / PUT (PATCH) / DELETE
    re_path(r'^api/todo/$', views.todo, name='todo'),  # GET(all) / POST

    re_path(r"^token_jwt/$", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    re_path(r"^token_jwt/refresh/$", TokenRefreshView.as_view(), name="token_refresh"),
]
