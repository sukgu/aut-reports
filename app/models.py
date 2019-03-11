from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

class TestcaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class TestRunManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class CompareManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
class TestRun(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=500)
    run_count = models.IntegerField()
    last_run = models.DateTimeField()
    testrun = TestRunManager()
    passed = models.IntegerField()
    failed = models.IntegerField()
    
    def __str__(self):
        return self.title

class Testcase(models.Model):
    title = models.CharField(max_length=500)
    result = models.BooleanField(default=False)
    testrun = models.ForeignKey(TestRun, on_delete=models.CASCADE,default=1)
    testcase = TestcaseManager()
    
    def __str__(self):
        return self.title

    
class Document(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='',validators=[FileExtensionValidator(allowed_extensions=['xml','json','html'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    format = models.CharField(max_length=10, blank=False)
    #navigate_url = models.URLField()
    
    def __str__(self):
        return self.name
    
class CompareModel(models.Model):
    title = models.CharField(max_length=500)
    result_1 = models.BooleanField(default=False)
    result_2 = models.BooleanField(default=False)
    compare_manager = CompareManager
    
    def save(self, *args, **kwargs):
        pass

    class Meta:
        managed = False
    

    
    