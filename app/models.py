from django.db import models


class Testcase(models.Model):
    title = models.CharField(max_length=500)
    id = models.CharField(max_length=10)
    tag = models.CharField(max_length=20)
    result = models.BooleanField(default=False)
    
class TestSuite(models.Model):
    title = models.CharField(max_length=500)
    id = models.CharField(max_length=10)
    tag = models.CharField(max_length=20)
    run_count = models.IntegerField()
    testcase = models.ManyToManyField(Testcase)
    last_run = models.DateTimeField()
    
class TestRun(models.Model):
    title = models.CharField(max_length=500)
    id = models.CharField(max_length=10)
    run_count = models.IntegerField()
    testsuite = models.ManyToManyField(TestSuite)
    last_run = models.DateTimeField()
    
    