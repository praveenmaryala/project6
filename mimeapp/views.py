from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
data= """<table><tr><th>eid</th><th>ename</th><th>esal</th></tr>
<tr><td>1001</td><td>anil</td><td>2000</td></tr>
<tr><td>1002</td><td>praveen</td><td>3000</td</tr>
<tr><td>1003</td><td>laxman</td><td>4000</td></tr></table"""
class htmlview(View):
    def get(selfself,request):
        return HttpResponse(data,content_type="text/html")
class excelview(View):
    def get(self,request):
        return HttpResponse(data,content_type="text/excel")
class xmlview(View):
    def get(selfself,request):
        return HttpResponse(data,content_type="text/xml")


