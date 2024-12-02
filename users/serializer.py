from rest_framework import serializers

from users.models import User
from users.validators import validate_mail, validate_pass


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[validate_mail])
    password = serializers.CharField(validators=[validate_pass])
    date_of_birth = serializers.DateField(validators=[])

    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        instance.is_active = True
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


