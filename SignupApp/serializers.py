from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        extra_kwargs = {

            'password' : {'write_only':True}
            

        } 

    def save(self):
        account = User(

            email = self.validated_data['email'],
            username = self.validated_data['username'],

                    )

        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password':'Passwords should match'})
        account.set_password(password)
        account.save()
        return account


