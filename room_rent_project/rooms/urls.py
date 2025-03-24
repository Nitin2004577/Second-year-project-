from django.urls import path
from .views import LoginView, RegisterView, RoomListView, RoomCreateView, RoomDetailView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('rooms/', RoomListView.as_view(), name='room-list'),         # For users to list rooms
    path('rooms/create/', RoomCreateView.as_view(), name='room-create'),  # For admins to create rooms
    path('rooms/<int:pk>/', RoomDetailView.as_view(), name='room-detail'),  # For admins to update/delete
]