from rest_framework import serializers
from .models import VetOfficers


class VetOfficersSerializer(serializers.ModelSerializer):
    class Meta:
        model = VetOfficers
        fields = ['id', 'name', 'county',
                  'published', 'email', 'phone_no', 'id_no']
