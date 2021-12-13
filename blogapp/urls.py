from django.urls import path
from .views import BlogListView,BlogDetailView,BlogCreateView,BlogUpdateView,BlogDeleteView

urlpatterns = [
    path('',BlogListView.as_view(),name='home' ),
    path('post/<int:pk>',BlogDetailView.as_view(),name='post_detail'),      # here we also get primary key which is returned by detail view
    path('post/new',BlogCreateView.as_view(),name='post_new'),
    path('post/<int:pk>/edit',BlogUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/delete',BlogDeleteView.as_view(),name='post_delete'),       #post/1/delete url pe blogdeleteview meh jo likha hua hai woh run karega include html page bhi wahi shoe hoga jo iss view meh likha gaya hai
]
