from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import CategoryCreateView, CategoryUpdateView, MixViewCategory, category_delete


app_name = 'categories'

urlpatterns =[
    path('', login_required(MixViewCategory.as_view()), name='category-index'),
    path('<int:pk>/update/', login_required(CategoryUpdateView.as_view()), name='category-update'),
    path('create/', login_required(CategoryCreateView.as_view()), name='category-create'),
    path('<int:pk>/delete/', login_required(category_delete), name='category-delete'),
]
