from rest_framework import serializers

from .models import Ad, Comment


class CommentSerializer(serializers.ModelSerializer):
    author_id = serializers.IntegerField(source='author.id', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    ad_id = serializers.IntegerField(source='ad.id', read_only=True)
    author_image = serializers.ImageField(source='author.image', read_only=True)

    class Meta:
        model = Comment
        fields = (
            'pk',
            'text',
            'author_id',
            'created_at',
            'author_first_name',
            'author_last_name',
            'ad_id',
            'author_image',
        )


class AdSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source='author.phone', read_only=True)
    author_first_name = serializers.CharField(source='author.first_name', read_only=True)
    author_last_name = serializers.CharField(source='author.last_name', read_only=True)
    author_id = serializers.IntegerField(source='author.id', read_only=True)

    class Meta:
        model = Ad
        fields = (
            'pk',
            'image',
            'title',
            'price',
            'phone',
            'description',
            'author_first_name',
            'author_last_name',
            'author_id',
        )


class AdDetailSerializer(AdSerializer):
    pass
