from unicodedata import name
from django.urls import URLPattern, path
from . import views
from todo.views import PostCreateView, PostListView, PostDetailView, PostDeleteView

urlpatterns = [
   path('task_list', PostListView.as_view(), name='task_list'),
   path('task_create', PostCreateView.as_view(), name='task_create'),
   path('task_detail/<int:pk>', PostDetailView.as_view(), name='task_detail'),
   path('task_update/<int:pk>', views.PostUpdateView.as_view(), name='task_update'),
   path('task_delete/<int:pk>', views.PostDeleteView.as_view(), name='task_delete')
]