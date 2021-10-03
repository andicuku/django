from django.urls import path
from .views import MixViewSource, SourceCreateView, SourceUpdateView, source_delete


app_name = 'sources'

urlpatterns =[
    path('', MixViewSource.as_view(), name='source-index'),
    path('<int:pk>/update/', SourceUpdateView.as_view(), name='source-update'),
    path('create/', SourceCreateView.as_view(), name='source-create'),
    path('<int:pk>/delete/', source_delete, name='source-delete'),
]
