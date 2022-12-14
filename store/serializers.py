from management.models import Management
from management.serializers import ManagementSerializer
from rest_framework.serializers import ModelSerializer, SerializerMethodField

from .models import Store


class StoreSerializer(ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class StoreListSerializer(ModelSerializer):
    Management = ManagementSerializer(many=True)

    class Meta:
        model = Store
        fields = "__all__"

    sub_total = SerializerMethodField()

    def get_sub_total(self, management):
        sub_total = 0
        transactions = Management.objects.filter(store_id=management.id)
        for i in transactions:

            if (
                i.type == "Débito"
                or i.type == "Crédito"
                or i.type == "Recebimento Empréstimo"
                or i.type == "Vendas"
                or i.type == "Recebimento TED"
                or i.type == "Recebimento DOC"
            ):

                sub_total = sub_total + i.value
            else:
                sub_total = sub_total - i.value
        return sub_total
