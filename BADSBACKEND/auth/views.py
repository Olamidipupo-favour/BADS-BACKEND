from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import status
from django.http import HttpResponse as Response
from BADSBACKEND.auth.serializers import UserSerializer, GroupSerializer, AllergyUsersSerializer
from BADSBACKEND.auth.models import AllergyUsers
# jsonify
from django.http import JsonResponse
from .dapp import *


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllergySearchViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    # queryset = AllergyUsers.objects.all()
    serializer_class = AllergyUsersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        print(request.data)
        eth_address = request.data['eth_address']
        full_name = request.data['name']
        family_history = request.data['family_history']
        genotype = request.data['genotype']
        blood_group = request.data['blood_group']
        allergy = request.data['allergy']
        medical_history = request.data['medical_history']
        if (eth_address == None or full_name == None or family_history == None or genotype == None or blood_group == None or allergy == None or medical_history == None):
            return Response("All fields are required", status=status.HTTP_400_BAD_REQUEST)
        # check if user exists
        if get_patient(eth_address) != None:
            # update user
            print(get_patient(eth_address))
            update_patient(eth_address, full_name, family_history,
                           genotype, blood_group, allergy, medical_history)
            return Response("User updated", status=status.HTTP_200_OK)
        else:
            # create user
            update_patient(eth_address, full_name, family_history,
                        genotype, blood_group, allergy, medical_history)
            return Response("User created", status=status.HTTP_201_CREATED)

    def retrieve(self, request, *args, **kwargs):
        eth_address = request.query_params.get('eth_address')
        data = None
        try:
            data = get_patient(eth_address)
        except:
            pass
        if data == None:
            return Response("User not found", status=status.HTTP_404_NOT_FOUND)
        return JsonResponse(get_patient(eth_address), safe=False, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        eth_address = request.address['eth_address']
        delete_patient(eth_address)
        return Response("User deleted", status=status.HTTP_410_GONE)

    def update(self, request, *args, **kwargs):
        eth_address = request.data['eth_address']
        full_name = request.data['name']
        family_history = request.data['family_history']
        genotype = request.data['genotype']
        blood_group = request.data['blood_group']
        allergy = request.data['allergy']
        medical_history = request.data['medical_history']
        update_patient(eth_address, full_name, family_history,
                       genotype, blood_group, allergy, medical_history)
        return Response("User modified", status=status.HTTP_202_ACCEPTED)


class PingViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        return Response("Pong", status=status.HTTP_200_OK)
