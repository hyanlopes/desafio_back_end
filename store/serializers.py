from rest_framework.serializers import ModelSerializer

from .models import Store


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

    def create(self, validated_data):
        print(validated_data)
        return Store.objects.create_user(**validated_data)
