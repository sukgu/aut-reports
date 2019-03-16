'''
Created on 03-Mar-2019

@author: sushil
'''

from rest_framework import serializers
from app.models import RestTestRunModel

class TestRunSerializer(serializers.ModelSerializer):
    
    version = serializers.CharField(max_length=100)
    title = serializers.CharField(max_length=300)
    json = serializers.JSONField()
        
    class Meta:
        model = RestTestRunModel
        fields = ('version', 'title', 'json')
        
    def validate_version(self, version):
        if version == "":
            raise serializers.ValidationError("Version is compulsory !")
        
        return version
    
    def validate_title(self, title):
        if title == "":
            raise serializers.ValidationError("Title is compulsory !")
        
        return title
    
    def validate_json(self, json):
        for key in json:
            value = json[key]
            if value == "pass":
                pass
            elif value == "fail":
                pass
            else:
                raise serializers.ValidationError("JSON for TestRun should be in {\"testcase_name\":\"True/False\"} format.")
            
        return json