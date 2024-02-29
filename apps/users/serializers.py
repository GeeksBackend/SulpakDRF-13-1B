from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',
                  'email', 'date_joined', 'phone')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User 
        fields = ('username','first_name','last_name','email', 'password', 'confirm_password', 'phone','date_joined')

    def validate(self, attrs):
        if attrs ['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({'password': 'Пароли отличаются'})
        elif len(attrs['password']) < 8 and len(attrs['confirm_password']) < 8:
            raise serializers.ValidationError({'password_len': 'Длина пароля меньше 8'})
        return attrs
    
    def create(self, validated_data):
        user = User.objects.create(
            username  = validated_data['username'],
            phone = validated_data['phone'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'] 
        )
        user.set_password(validated_data['password'])
        user.save()
        return user