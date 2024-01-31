from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .serializers import CustomUserSerializer
from .permissions import IsOwner, IsAdminUser,IsAdminUserOrIsOwner
from .models import CustomUser

class CreateAdminView(APIView):
    #permission_classes = [IsOwner, IsAdminUser]
    #permission_classes = [IsOwner]
    #permission_classes = [IsAdminUser]
    # permission_classes = [IsAdminUserOrIsOwner]

    def post(self, request):
        print(request.data)
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ListOwnerView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions

    def get(self, request):
        # Query for riders with user_type="rider"
        # riders = CustomUser.objects.all()
        owner = CustomUser.objects.filter(user_type ="owner")

        # Serialize the data
        if owner:
            serializer = CustomUserSerializer(owner, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data = "Errors", status=status.HTTP_404_NOT_FOUND)
    
class ListAdminView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions

    def get(self, request):
        # Query for riders with user_type="rider"
        # riders = CustomUser.objects.all()
        admins = CustomUser.objects.filter(user_type ="admin")

        # Serialize the data
        if admins:
            serializer = CustomUserSerializer(admins, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data = "Errors", status=status.HTTP_404_NOT_FOUND)

class OwnerRetrieveUpdateDeleteView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions
    serrializer_class = CustomUserSerializer
    def get(self, request, user_id:int):

        owner = CustomUser.objects.filter(user_type ="owner", pk=user_id)
        serializer = CustomUserSerializer(owner, many=True)
        return Response(data=serializer.data[0], status=status.HTTP_200_OK)
       
    def put(self, request: Request, user_id:int):
        rider = CustomUser.objects.filter(user_type ="owner", pk=user_id)

        serializer = self.serrializer_class(instance=rider, data=request.data)

        if serializer.is_valid():
            serializer.save()
 
            response = {"message": f"Owner {request.data['username']} Updated Successfully to {serializer.data['username']}", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, user_id:int):
        owner = CustomUser.objects.filter(user_type ="owner", pk=user_id)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AdminRetrieveUpdateDeleteView(APIView):
    # permission_classes = [IsOwner]  # You can set appropriate permissions
    serrializer_class = CustomUserSerializer
    def get(self, request, user_id:int):

        rider = CustomUser.objects.filter(user_type ="admin", pk=user_id)
        serializer = CustomUserSerializer(rider, many=True)
        return Response(data=serializer.data[0], status=status.HTTP_200_OK)
       
    def put(self, request: Request, user_id:int):
        admin = CustomUser.objects.filter(user_type ="admin", pk=user_id)

        serializer = self.serrializer_class(instance=admin, data=request.data)

        if serializer.is_valid():
            serializer.save()
 
            response = {"message": f"Admin {request.data['username']} Updated Successfully to {serializer.data['username']}", "data":serializer.data}
            return Response(data= response, status=status.HTTP_202_ACCEPTED)
        
        return Response(data= serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request: Request, user_id:int):
        admin = CustomUser.objects.filter(user_type ="admin", pk=user_id)
        admin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    permission_classes = []

    def get(self, request: Request):
        content = {
            "username":str(request.user),
            "auth": str(request.auth)
            }
        return Response(data=content, status= status.HTTP_200_OK)


