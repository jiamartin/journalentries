from django.urls import path
from . views import indexView, entryView, addView, updateEntryView

urlpatterns = [
   path('', indexView.as_view(), name='index'),
   path('entry/<int:pk>', entryView.as_view(), name='entry-detail'),
   path('write/', addView.as_view(), name='add'),
   path('entry/edit/<int:pk>', updateEntryView.as_view(), name='entry-edit'),
]