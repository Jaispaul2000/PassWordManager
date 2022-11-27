
from rest_framework.viewsets import ViewSet,ModelViewSet
from PasswordApp.serializer import UserSerializer,PassWordSerializer,OrganizationSerializer
from rest_framework.response import Response
from PasswordApp.models import PassWordModel
from rest_framework import permissions,authentication
from rest_framework.decorators import action

class UserView(ViewSet):
    def create(self, request,*args, **kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

class PassWordView(ModelViewSet):
    serializer_class = PassWordSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer=PassWordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def get_queryset(self):
        return PassWordModel.objects.filter(user=self.request.user)


    def list(self,request,*args,**kwargs):
        qs=PassWordModel.objects.all()
        serializer=PassWordSerializer(qs,many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=PassWordModel.objects.get(id=id)
        serializer=PassWordSerializer(qs)
        return Response(data=serializer.data)

    def update(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        instance=PassWordModel.objects.get(id=id)
        serializer=PassWordSerializer(instance=instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def destroy(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=PassWordModel.objects.get(id=id)
        qs.delete()
        return Response(data="ok")


class OrganizationView(ModelViewSet):
    serializer_class = OrganizationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


    def create(self, request, *args, **kwargs):
        serializer=OrganizationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def get_queryset(self):
        return PassWordModel.objects.filter(user=self.request.user)










