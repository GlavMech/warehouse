from rest_framework import serializers, validators
from api.models import ApiUser, Warehouse, Product, Shipment

class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)

    class Meta:
        model = ApiUser
        fields = ['id', 'username', 'email', 'password', 'group']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = ApiUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        if password := validated_data.get('password'):
            instance.set_password(password)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.group = validated_data.get('group', instance.group)
        instance.save()
        return instance

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = '__all__'

class ShipmentSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.exclude(shipments__isnull=False)
    )

    class Meta:
        model = Shipment
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['product'] = ProductSerializer(instance.product).data
        return rep
