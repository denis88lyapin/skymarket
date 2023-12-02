from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from .filters import AdFilter
from .models import Ad, Comment
from .paginators import AdsPagination
from .serializers import AdSerializer, CommentSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdAutorListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    pagination_class = AdsPagination

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = AdsPagination

    def get_queryset(self):
        ad_pk = self.kwargs.get('ad_pk')
        return Comment.objects.filter(ad_id=ad_pk)

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get('ad_pk')
        ad = Ad.objects.get(pk=ad_pk)
        serializer.save(author=self.request.user, ad=ad)

# from rest_framework import viewsets, generics
# from .models import Ad, Comment
# from .paginators import AdsPagination
# from .serializers import AdSerializer, CommentSerializer
#
#
# class AdViewSet(viewsets.ModelViewSet):
#     queryset = Ad.objects.all()
#     serializer_class = AdSerializer
#     pagination_class = AdsPagination
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
#
#
# class AdAutorListAPIView(generics.ListAPIView):
#     serializer_class = AdSerializer
#     pagination_class = AdsPagination
#
#     def get_queryset(self):
#         return Ad.objects.filter(author=self.request.user)
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     serializer_class = CommentSerializer
#     pagination_class = AdsPagination
#
#     def get_queryset(self):
#         return Comment.objects.filter(ad=self.kwargs.get('ad'))
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)
