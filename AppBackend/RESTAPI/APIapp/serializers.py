from .models import Map, MapHasTags, MapHasLogo, Logo, Tag
from rest_framework import serializers

class TagSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

    class Meta:
        model = Tag


