from turtle import title
from rest_framework import serializers
from base.models import tagdetails,textdetails


class tagDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = tagdetails
        fields = '__all__'

class textDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = textdetails
        fields = ['id','title','timestamp','created_user','textdata']
    def create(self,validated_data):
        tag_name = validated_data['title']
        a,f = tagdetails.objects.get_or_create(tag_title=tag_name)
        print (a.tag_title)
        return textdetails.objects.create(title=validated_data['title'],
                textdata = validated_data['textdata'],created_user=validated_data['created_user'],tag_id=a)
