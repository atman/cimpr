from rest_framework import serializers
'''
SAMPLE FILE FOR RUNNING SCRIPTS IN THE SHELL
1) CREATE
2) UPDATE
3) DELETE
'''


from core.models import Contact
from relations.api.serializers import ContactSerializer

data = {"user": 1}

"""Create an object using Serializer"""
create_serializer = ContactSerializer(data=data)
if create_serializer.is_valid():
    create_serializer.save()


"""Update an object using Serializer"""
obj = Contact.objects.first()
data = {"user": 1, "first_name": "Test_Upate New", "email":"test4@test.com"}
update_serializer = ContactSerializer(obj, data)
if update_serializer.is_valid():
    update_serializer.save()

"""Delete an object using Serializer"""
obj = Contact.objects.last()
get_data_serializer = ContactSerializer(obj, data)

obj.delete()

###########################################


class CustomSerializer(serializers.Serializer):
    """Sample normal serializer"""
    content = serializers.CharField()
