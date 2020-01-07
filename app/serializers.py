from rest_framework import serializers
from app.models import URLMapper


class URLMapperSerializer(serializers.ModelSerializer):
    class Meta:
        model = URLMapper
        fields = ("url", "shorten_url", "create")
        extra_kwargs = {
            'shorten_url': {'read_only': True},
            'create': {'read_only': True}
        }
