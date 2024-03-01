from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf.urls.static import static
from django.conf import settings

from .views import PostListCreate,CommentListCreate,LikeCreateView



urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', PostListCreate.as_view(),name='post-list-create'),
    path('comments/', CommentListCreate.as_view(), name='comments-list-create'),
    path('likes/', LikeCreateView.as_view(), name='like-create'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)