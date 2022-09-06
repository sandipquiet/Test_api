from rest_framework import serializers
from .models import Product, Publication, Article, Student


# Register your models here.
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name', 'manufacturer', 'price_in_dollars']


class PublicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publication
        fields = ['title']

class StudentSerialization(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField(max_length=80)
    age = serializers.IntegerField()
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)



class StudentSerialization1(serializers.Serializer):

    name = serializers.CharField(max_length=80)
    age = serializers.IntegerField()
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.age = validated_data.get('age', instance.age)
        instance.save()
        return instance



