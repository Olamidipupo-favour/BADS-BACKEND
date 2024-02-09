from django.contrib.auth.models import User, Group
from rest_framework import serializers
from BADSBACKEND.auth.models import AllergyUsers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class AllergyUsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AllergyUsers
        fields = ['name', 'eth_address', 'family_history',
                  'genotype', 'blood_group', 'allergy', 'medical_history']


class Allerguserializer(serializers.OrderedDict):
    class Meta:
        model = AllergyUsers
        fields = ['name', 'eth_address', 'family_history',
                  'genotype', 'blood_group', 'allergy', 'medical_history']
