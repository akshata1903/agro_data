# import imp
import imp
from django.shortcuts import render,HttpResponseRedirect,redirect
from pytz import timezone
from .forms import Cropform, Plotform, Soilform, Issueform, Toolform
# Diseaseform
from .models import Crop, Plot, Soil, Issue, Tool
# Disease
# from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def crudcrop(request):
    
    log_user = request.user
    cro = Crop.objects.filter(user=log_user)
    if request.method=="POST":
        fm = Cropform(request.POST)
        
        if fm.is_valid():
            loc = fm.cleaned_data['location']
            fieldcro = fm.cleaned_data['fieldcropid']
            croty = fm.cleaned_data['croptype']
            cropvar = fm.cleaned_data['cropvariety']
            name = fm.cleaned_data['name']
            expecyieldpeh = fm.cleaned_data['expecyieldpeh']
            avgplanthei = fm.cleaned_data['avgplanthei']
            expecperi = fm.cleaned_data['expecperi']
            tab = Crop(user=request.user,location=loc,fieldcropid=fieldcro,croptype=croty,cropvariety=cropvar,name=name,expecyieldpeh=expecyieldpeh,avgplanthei=avgplanthei,expecperi=expecperi)
            tab.save()
            fm = Cropform()

    else:
        fm = Cropform()
        
    return render(request,'tables/crudcrop.html',{'crop':cro,'form':fm})  

def editcrop(request,id):
    # log_user = request.user
    # cro = Crop.objects.filter(user=log_user)
    # context={}
    # check = Crop.objects.get(log_user.id)
    # if len(check)>0:
    #     data = Crop.objects.get(log_user.id)
    #     context["data"]=data
    if request.method=='POST':
        loc = request.POST['location']
        fieldcro = request.POST['fieldcropid']
        croty = request.POST['croptype']
        cropvar = request.POST['cropvariety']
        name = request.POST['name']
        expecyieldpeh = request.POST['expecyieldpeh']
        avgplanthei = request.POST['avgplanthei']
        expecperi = request.POST['expecperi']
        
        
        obj = Crop.objects.get(id=id)
        obj.location = loc
        obj.fieldcropid=fieldcro
        obj.croptype=croty
        obj.cropvariety=cropvar
        obj.name=name
        obj.expecyieldpeh=expecyieldpeh
        obj.avgplanthei=avgplanthei
        obj.expecperi=expecperi

        obj.save()
        return HttpResponseRedirect('/crudcrop/')

    else:
        pi = Crop.objects.get(id=id)
        return render(request, 'tables/editcrop.html',{'form':pi})

def deletecrop(request,id):
    if request.method=="POST":
        pi = Crop.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/crudcrop/')


def crudplot(request):
    
    log_user = request.user
    cro = Plot.objects.filter(user=log_user)
    if request.method=="POST":
        fm = Plotform(request.POST)
        
        if fm.is_valid():
            loc = fm.cleaned_data['location']
            field = fm.cleaned_data['field']
            farm = fm.cleaned_data['farm']
            farmer = fm.cleaned_data['farmer']
            plot = fm.cleaned_data['plot']
            rows = fm.cleaned_data['rows']
            columns = fm.cleaned_data['columns']
            plants = fm.cleaned_data['plants']
            tab = Plot(user=request.user,location=loc,field=field,farm=farm,farmer=farmer,plot=plot,rows=rows,columns=columns,plants=plants)
            tab.save()
            fm = Plotform()

    else:
        fm = Plotform()
        
    return render(request,'tables/crudplot.html',{'plot':cro,'form':fm}) 

def editplot(request,plot_id):
    
    if request.method=='POST':
        loc = request.POST['location']
        field = request.POST['field']
        farm = request.POST['farm']
        farmer = request.POST['farmer']
        plot = request.POST['plot']
        rows = request.POST['rows']
        columns = request.POST['columns']
        plants = request.POST['plants']
        
        
        obj = Plot.objects.get(id=plot_id)
        obj.location = loc
        obj.field=field
        obj.farm=farm
        obj.farmer=farmer
        obj.plot=plot
        obj.rows=rows
        obj.columns=columns
        obj.plants=plants
       
        obj.save()
        return HttpResponseRedirect('/crudplot/')

    else:
        pi = Plot.objects.get(id=plot_id)
        return render(request, 'tables/editplot.html',{'info':pi})

def deleteplot(request,plot_id):
    if request.method=="POST":
        pi = Plot.objects.get(pk=plot_id)
        pi.delete()
        return HttpResponseRedirect('/crudplot/')


#soil
def crudsoil(request):
    
    log_user = request.user
    cro = Soil.objects.filter(user=log_user)
    if request.method=="POST":
        fm = Soilform(request.POST)
        
        if fm.is_valid():
            loc = fm.cleaned_data['location']
            dailyweat = fm.cleaned_data['dailyweat']
            mintemp = fm.cleaned_data['mintemp']
            maxtemp = fm.cleaned_data['maxtemp']
            windspeed = fm.cleaned_data['windspeed']
            humidity = fm.cleaned_data['humidity']
            sunshinehrs = fm.cleaned_data['sunshinehrs']
            
            tab = Soil(user=request.user,location=loc,dailyweat=dailyweat,mintemp=mintemp,maxtemp=maxtemp,windspeed=windspeed,humidity=humidity,sunshinehrs=sunshinehrs)
            tab.save()
            fm = Soilform()

    else:
        fm = Soilform()
        
    return render(request,'tables/crudsoil.html',{'crop':cro,'form':fm}) 

def editsoil(request,soil_id):
    
    if request.method=='POST':
        loc = request.POST['location']
        dailyweat = request.POST['dailyweat']
        mintemp = request.POST['mintemp']
        maxtemp = request.POST['maxtemp']
        windspeed = request.POST['windspeed']
        humidity = request.POST['humidity']
        sunshinehrs = request.POST['sunshinehrs']
        
        
        
        obj = Soil.objects.get(id=soil_id)
        obj.location = loc
        obj.dailyweat=dailyweat
        obj.mintemp=mintemp
        obj.maxtemp=maxtemp
        obj.windspeed=windspeed
        obj.humidity=humidity
        obj.sunshinehrs=sunshinehrs
        
       
        obj.save()
        return HttpResponseRedirect('/crudsoil/')

    else:
        pi = Soil.objects.get(id=soil_id)
        return render(request, 'tables/editsoil.html',{'form':pi})

def deletesoil(request,soil_id):
    if request.method=="POST":
        pi = Soil.objects.get(pk=soil_id)
        pi.delete()
        return HttpResponseRedirect('/crudsoil/')


#issue
def crudissue(request):
    
    log_user = request.user
    cro = Issue.objects.filter(user=log_user)
    if request.method=="POST":
        fm = Issueform(request.POST)
        
        if fm.is_valid():
            loc = fm.cleaned_data['location']
            issueid = fm.cleaned_data['issueid']
            solution = fm.cleaned_data['solution']
            
            
            tab = Issue(user=request.user,location=loc,issueid=issueid,solution=solution)
            tab.save()
            fm = Issueform()

    else:
        fm = Issueform()
        
    return render(request,'tables/crudissue.html',{'crop':cro,'form':fm}) 

def editissue(request,issue_id):
    
    if request.method=='POST':
        loc = request.POST['location']
        issueid = request.POST['issueid']
        solution = request.POST['solution']
        
      
        obj = Issue.objects.get(id=issue_id)
        obj.location = loc
        obj.issueid=issueid
        obj.solution=solution
        
        
       
        obj.save()
        return HttpResponseRedirect('/crudissue/')

    else:
        pi = Issue.objects.get(id=issue_id)
        return render(request, 'tables/editissue.html',{'form':pi})

def deleteissue(request,issue_id):
    if request.method=="POST":
        pi = Issue.objects.get(pk=issue_id)
        pi.delete()
        return HttpResponseRedirect('/crudissue/')


#Tool
def crudtool(request):
    
    log_user = request.user
    cro = Tool.objects.filter(user=log_user)
    if request.method=="POST":
        fm = Toolform(request.POST)
        
        if fm.is_valid():
            loc = fm.cleaned_data['location']
            
            toolid = fm.cleaned_data['toolid']
            toolname = fm.cleaned_data['toolname']
            rate = fm.cleaned_data['rate']
            # contact = fm.cleaned_data['contact']



            
            
            tab = Tool(user=request.user,location=loc,toolid=toolid,toolname=toolname,rate=rate)
            tab.save()
            fm = Toolform()

    else:
        fm = Toolform()
        
    return render(request,'tables/crudtool.html',{'crop':cro,'form':fm}) 

def edittool(request,tool_id):
    
    if request.method=='POST':
        loc = request.POST['location']
        
        toolid = request.POST['toolid']
        toolname = request.POST['toolname']
        rate = request.POST['rate']


        obj = Tool.objects.get(id=tool_id)
        obj.location = loc
       
        obj.toolid=toolid
        obj.toolname=toolname
        obj.rate=rate


       
        obj.save()
        return HttpResponseRedirect('/crudtool/')

    else:
        pi = Tool.objects.get(id=tool_id)
        return render(request, 'tables/edittool.html',{'form':pi})

def deletetool(request,tool_id):
    if request.method=="POST":
        pi = Tool.objects.get(pk=tool_id)
        pi.delete()
        return HttpResponseRedirect('/crudtool/')

#crop expert
def issueexpert(request):
    alldata = Issue.objects.all()
    return render(request,'tables/issueexpert.html',{'crop':alldata})

def editexpertissue(request,exissue_id):
    
    if request.method=='POST':
        loc = request.POST['location']
        issueid = request.POST['issueid']
        solution = request.POST['solution']
        
      
        obj = Issue.objects.get(id=exissue_id)
        obj.location = loc
        obj.issueid=issueid
        obj.solution=solution
        
        
       
        obj.save()
        return HttpResponseRedirect('/issueexpert/')

    else:
        pi = Issue.objects.get(id=exissue_id)
        return render(request, 'tables/issueeditexpert.html',{'form':pi})

def delexpertissue(request,exissue_id):
    if request.method=="POST":
        pi = Issue.objects.get(pk=exissue_id)
        pi.delete()
        return HttpResponseRedirect('/issueexpert/')


#otheruser
def otheruser(request):
    alldata = Tool.objects.all()
    return render(request,'tables/otheruser.html',{'crop':alldata})