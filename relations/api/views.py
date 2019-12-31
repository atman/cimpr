from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from core.models import Contact
from .serializers import ContactSerializer


class ContactAPIView(mixins.CreateModelMixin,
                     generics.ListAPIView):
    """LIST & Create API View for Contacts"""

    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]

    serializer_class = ContactSerializer

    def get_queryset(self):
        qs = Contact.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(type__icontains=query)
        return qs

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
       serializer.save(user=self.request.user)


"""
DETAIL API VIEW
- Retrieve Details
- Update
- Delete
"""


class ContactDetailAPIView(generics.RetrieveAPIView,
                           mixins.UpdateModelMixin,
                           mixins.DestroyModelMixin,
                           ):


    #permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #authentication_classes = [SessionAuthentication]
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    lookup_field = 'pk'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    # can be overriddent to get the specific object
    # def get_object(self,*args, **kwargs):
    #   kwargs = self.kwargs
    #  kw_id = kwargs.get('id')
    # return Contact.objects.get(id=kw_id)

