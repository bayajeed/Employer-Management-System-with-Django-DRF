from rest_framework import serializers
from .models import Employer
from users.models import CustomUser

class EmployerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employer
        fields = [
            'id',
            'company_name',
            'contact_person_name',
            'email',
            'phone_number',
            'address',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'user']

    def validate_email(self, value):
        user = self.context['request'].user
        if Employer.objects.filter(user=user, email=value).exists():
            raise serializers.ValidationError("An employer with this email already exists.")
        return value

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)