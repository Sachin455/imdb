from rest_framework import serializers
from .models import Platform, Movie



class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only =True)
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()

    


    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.active = validated_data.get('active')
        instance.save()

        return instance
    
    #field level validation
    def validate_name(self,value):
        if len(value)<2:
            raise serializers.ValidationError("name is too short")
        return value
    
    def validate_description(self,value):
        if len(value)<2:
            raise serializers.ValidationError('description cannot be short')
        return value
    
    #object level validation
    def validate(self,data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description cannto be same")
        return data
    
    #validator 
        




class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = Platform
        fields = '__all__'