from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='reviews'),
    path('review/<slug:slug>/', views.PostDetail.as_view(), name='review_details'),
    path('like/<slug:slug>/', views.PostLike.as_view(), name='review_like'),
    path('leave_review/', views.LeaveReview.as_view(), name='leave_review'),
]
