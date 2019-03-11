import django_tables2 as tables
from .models import Testcase,TestRun
from app.models import CompareModel


class TestcaseTable(tables.Table):
    title = tables.Column()
    result = tables.BooleanColumn(yesno="Pass,Fail")
    class Meta:
        model = Testcase
        template_name = 'django_tables2/bootstrap4.html'
        fields = ("title", "result")
        
class CompareModelTable(tables.Table):
    title = tables.Column()
    result_1 = tables.BooleanColumn(yesno="Pass,Fail",verbose_name="Result")
    result_2 = tables.BooleanColumn(yesno="Pass,Fail",verbose_name="Result")
    class Meta:
        model = CompareModel
        template_name = 'django_tables2/bootstrap4.html'
        fields = ("title", "result_1","result_2")
        
class TestRunTable(tables.Table):
    title = tables.Column()
    run_count = tables.Column(verbose_name="TC Count")
    last_run = tables.Column()
    passed = tables.Column()
    failed = tables.Column()
    class Meta:
        model = TestRun
        template_name = 'django_tables2/bootstrap4.html'
        fields = ("title", "run_count","passed","failed","last_run")