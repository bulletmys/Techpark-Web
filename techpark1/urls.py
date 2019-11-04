"""techpark1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from question import views as question_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', question_views.list_of_question, name='base'),
    path('ask/', question_views.new_question, name='new_question'),
    path('login/', question_views.login, name='login'),
    path('<int:page>/', question_views.list_of_question, name='page_num'),
    path('question/<int:num>/', question_views.answers, name='answers'),
    path('signup/', question_views.registration, name='register'),
    path('settings/', question_views.settings, name='settings'),
    path('tags/<str:name>/<int:page>/', question_views.tags_list, name="questions_tag"),
]
