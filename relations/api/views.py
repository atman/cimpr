from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins
from core.models import Contact
from .serializers import ContactSerializer


# Create your views here.

class ContactListSearchAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, format=None):
        qs = Contact.objects.all()
        serializer = ContactSerializer(qs, many=True)
        return Response(serializer.data)

# CreateModelMixin --> Handles POST Data


class ContactAPIView(mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     generics.ListAPIView):

    permission_classes = []
    authentication_classes = []

    serializer_class = ContactSerializer

    def get_queryset(self):
        qs = Contact.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(type__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


    #def perform_create(self, serializer):
     #   serializer.save(user=self.request.user)


class ContactDetailAPIView(mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           generics.RetrieveAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    #lookup_field = 'id'

    # can be overriddent to get the specific object
    #def get_object(self,*args, **kwargs):
     #   kwargs = self.kwargs
      #  kw_id = kwargs.get('id')
       # return Contact.objects.get(id=kw_id)


class ContactUpdateAPIView(generics.UpdateAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDeleteAPIView (generics.DestroyAPIView):
    permission_classes = []
    authentication_classes = []
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
