from django.urls import path
from .views import (
    MemberListView,
    MemberCreateView,
    MemberUpdateView,
    MemberDeleteView,
)

urlpatterns = [
    path('', MemberListView.as_view(), name='member_list'),
    path('member/new/', MemberCreateView.as_view(), name='member_new'),
    path('member/<int:pk>/edit/', MemberUpdateView.as_view(), name='member_edit'),
    path('post/<int:pk>/delete', MemberDeleteView.as_view(), name='member_delete'),
]