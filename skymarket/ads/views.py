from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from .filters import AdFilter
from .models import Ad, Comment
from .paginators import AdsPagination
from .permissions import IsOwnerOrReadOnly, IsAdminUserOrReadOnly
from .serializers import AdSerializer, CommentSerializer


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    pagination_class = AdsPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter
    permission_classes = [IsAdminUserOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class AdAutorListAPIView(generics.ListAPIView):
    serializer_class = AdSerializer
    pagination_class = AdsPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    pagination_class = AdsPagination
    permission_classes = [IsAuthenticated, IsAdminUserOrReadOnly]

    def get_queryset(self):
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        return Comment.objects.filter(ad=ad)

    def perform_create(self, serializer):
        ad_pk = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_pk)
        serializer.save(author=self.request.user, ad=ad)
