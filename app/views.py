'''
Created on 03-Mar-2019

@author: sushil
'''
from django.views.generic import TemplateView
from auth.models import TokenModel
from django import forms
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from allauth.socialaccount.models import SocialAccount
from app.models import Document, TestRun, Testcase, CompareModel
from datetime import datetime
from app.utils import get_object_from_json
from app.tables import TestRunTable, TestcaseTable, CompareModelTable
from django_tables2.config import RequestConfig

FILE_FORMAT_CHOICES = (
    ('json', 'Json'),
    ('xml', 'XML'),
    ('html', 'HTML'),
)

class Home(TemplateView):
    template_name = 'home.html'

@method_decorator(login_required, name="dispatch")   
class App(TemplateView):
    models = TokenModel
    template_name = 'app/home.html'
    
    def get(self, request, *args, **kwargs):
        data=SocialAccount.objects.get(user=request.user)
        provider=data.provider
        return render(request,self.template_name,{'user_data':data.extra_data,'provider':provider})
        
        
    
    
class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(label='Email')  
    comment = forms.CharField(widget=forms.Textarea)
    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass
    
class ContactView(FormView):
    template_name = 'about/contact.html'
    form_class = ContactForm
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)
    
class UploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document',)
    
class UploadView(FormView):
    template_name = 'app/upload.html'
    form_class = UploadForm
    
    def post(self, request, *args, **kwargs):
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            object_file = request.FILES['document']
            file_format = object_file.content_type
            file_name = object_file.name
            document = Document(user=request.user,name=file_name,document=object_file,format=file_format)
            document.save()
            testcase_list = get_object_from_json(settings.BASE_DIR+"/documents/"+file_name)
            passed = 0
            failed = 0
            for testcase in testcase_list:
                if testcase.result == "False":
                    failed+=1
                else:
                    passed+=1
            testrun = TestRun(user=request.user,title=datetime.now(),last_run=datetime.now(),run_count=len(testcase_list),passed=passed,failed=failed)
            testrun.save()
            for testcase in testcase_list:
                testcase.testrun = testrun
                testcase.save()
                

            return redirect('upload')
        return FormView.post(self, request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        return FormView.get(self, request, *args, **kwargs)
    
    def form_valid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
###########################################################
    
from chartjs.views.lines import BaseLineChartView


class LineChartJSONView(BaseLineChartView):
        
    def get_labels(self):
        testrun = TestRun.testrun.filter(user=self.request.user)
        data = [testrun[0].title,testrun[1].title]
        return data

    def get_providers(self):
        return ["Passed", "Failed"]

    def get_data(self):
        testruns = TestRun.testrun.filter(user=self.request.user)
        data1 = []
        data2 = []
        for test_run in testruns:
            pass_testcases = Testcase.testcase.filter(testrun = test_run).filter(result = 1)
            fail_testcases = Testcase.testcase.filter(testrun = test_run).filter(result = 0)
            data1.append(len(pass_testcases))
            data2.append(len(fail_testcases))
        data = [data1,data2]
        return data


line_chart = TemplateView.as_view(template_name='app/reports.html')
line_chart_json = LineChartJSONView.as_view()

def tbl_testrun(request):
    table = TestRunTable(TestRun.testrun.filter(user=request.user))
    RequestConfig(request).configure(table)
    return render(request, 'app/testrun_tbl.html', {'testrun': table})

def tbl_testcase(request,testrun_id):
    table = TestcaseTable(Testcase.testcase.filter(testrun=testrun_id))
    testrun = TestRun.testrun.filter(user=request.user)
    RequestConfig(request).configure(table)
    return render(request, 'app/testcase_tbl.html', {'testcase': table, "testrun_list":testrun})

def compare_reports(request,testrun_id1=1,testrun_id2=1):
    query1 = Testcase.testcase.filter(testrun=testrun_id1)
    query2 = Testcase.testcase.filter(testrun=testrun_id2)
    models = []
    for testcase1 in query1:
        for testcase2 in query2:
            if (testcase1.title == testcase2.title and testcase1.result != testcase2.result) or (testcase1.title == testcase2.title and testcase1.result == testcase2.result == False):
                models.append(CompareModel(title=testcase1.title,result_1=testcase1.result,result_2=testcase2.result))
    
    table = CompareModelTable(models)
    testrun = TestRun.testrun.filter(user=request.user)
    RequestConfig(request).configure(table)
    return render(request, 'app/compare_reports.html', {'testcase': table, "testrun_list":testrun})

def reports(request):
    table = TestcaseTable(Testcase.testcase.filter(testrun=1))
    testrun = TestRun.testrun.filter(user=request.user)
    RequestConfig(request).configure(table)
    return render(request, 'app/app.html', {'testcase': table, "testrun_list":testrun})

    
    