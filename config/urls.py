from django.urls import path
from alunos import views

urlpatterns = [
    path('', views.index, name='index'), #Redireciona para index.html
    path('api/alunos/', views.alunos_api, name='alunos_api'),
    path('api/alunos/<int:pk>/', views.excluir_api, name='excluir_api')
]
