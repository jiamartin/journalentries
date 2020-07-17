from django.urls import path
from . views import indexView, entryView, addView

urlpatterns = [
   path('', indexView.as_view(), name='index'),
   path('entry/<int:pk>', entryView.as_view(), name='entry-detail'),
   path('write/', addView.as_view(), name='add'),
]