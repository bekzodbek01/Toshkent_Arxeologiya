from rest_framework import serializers
from items.models import Items


class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ('id', 'title', 'descriptions', 'video', 'image','downloads')
