from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=250)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)