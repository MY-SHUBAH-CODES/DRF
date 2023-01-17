from django.shortcuts import HttpResponse,render
from .models import *
from .serializers import *

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def home(request):
    if request.method=='GET':
        mydata=request.body
        stream=io.BytesIO(mydata)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        print(id)
        if id==None:
            alldata=Student.objects.all()
            serializer=Studentserializer(alldata,many=True)
            jsondata=JSONRenderer().render(serializer.data)
            return HttpResponse(jsondata,content_type='application/json')
        obj=Student.objects.get(id=id)
        serializer=Studentserializer(obj)
        jsondata=JSONRenderer().render(serializer.data)
        return HttpResponse(jsondata,content_type='application/json')




    
    
    
    
    
    if request.method=='POST':
        mydata=request.body
        stream=io.BytesIO(mydata)
        pydata=JSONParser().parse(stream)
        serializer=Studentserializer(data=pydata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'save ho gaya'}
            jsondata=JSONRenderer().render(data=res['msg'])
            return HttpResponse(jsondata,content_type='application/json')
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')

    if request.method =='PUT':
        mydata=request.body
        stream=io.BytesIO(mydata)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=Student.objects.get(id=id)
        serializer=Studentserializer(stu,data=pydata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"bhai ho gaya update"}
            jsondata=JSONRenderer().render(res['msg'])
            return HttpResponse(jsondata,content_type='application/json')
        jsondata=JSONRenderer().render(serializer.errors)
        return HttpResponse(jsondata,content_type='application/json')



    if request.method=='DELETE':
        mydata=request.body
        stream=io.BytesIO(mydata)
        pydata=JSONParser().parse(stream)
        id=pydata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":"kar dia delete"}
        jsondata=JSONRenderer().render(res['msg'])
        return HttpResponse(jsondata,content_type='application/json')

def root(request):
    return render(request,'root.html',{"data":"Click"})


        
    








