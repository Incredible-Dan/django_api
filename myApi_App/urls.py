from posixpath import basename
from django.urls import path, include
from .views import ArticleDetail, articles_list, article_detail, ArticleAPIView,GenericAPIView,ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [

    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', articles_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail),
    path('detail/<int:id>/', ArticleDetail.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view()),

]
