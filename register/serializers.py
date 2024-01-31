from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    user_type = serializers.CharField(default='admin')
    password = serializers.CharField(min_length=8, write_only =True)

    class Meta:
        model = CustomUser
        fields = '__all__'
        #fields = ['email', 'username', 'password','user_type', "first_name", "last_name"]

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)

        user.save()

        return user

