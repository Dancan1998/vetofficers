from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import VetOfficersSerializer
from .models import VetOfficers
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions


@api_view(['GET', 'POST', 'DELETE'])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def vetofficers_list(request):
    if request.method == 'GET':
        vetofficers = VetOfficers.objects.all()
        name = request.GET.get('name', None)
        if name is not None:
            vetofficers = vetofficers.filter(name__icontains=name)

        serializer = VetOfficersSerializer(vetofficers, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        serializer = VetOfficersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = VetOfficers.objects.all().delete()
        return JsonResponse({'message': '{} Vets were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@ api_view(['GET', 'PUT', 'DELETE'])
def vetofficer_detail(request, pk):
    """
    Retrieve, update or delete a single object_tutorial.
    """
    try:
        vetofficer = VetOfficers.objects.get(pk=pk)
    except vetofficer.DoesNotExist:
        return Response({'message': 'What you are looking for does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VetOfficersSerializer(vetofficer)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        serializer = VetOfficersSerializer(vetofficer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        vetofficer.delete()
        return JsonResponse({'message': 'Vetofficer was deleted successfulyy'}, status=status.HTTP_204_NO_CONTENT)


# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
@ api_view(['GET'])
def vetofficers_list_published(request):
    """
    Filter vetoffice by condition
    """
    vetofficers = VetOfficers.objects.filter(published=True)
    if request.method == 'GET':
        serializer = VetOfficersSerializer(vetofficers, many=True)
        return JsonResponse(serializer.data, safe=False)
