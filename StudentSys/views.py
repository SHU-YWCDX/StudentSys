from django.shortcuts import render,redirect
from StudentSys import models
from StudentSys import forms
# Create your views here.



def addStu(request):
    try:
        NewStu = forms.Stu_Form(data=request.POST)
        if NewStu.is_valid():
            print(NewStu)

            print(request.POST.get('Stu_Department'))

            NewStu.save()
            return redirect('ManagerStu')
    except:
        print("Add Student Error")

def deleteStu(request):
    try:
        DeleteStuID = request.POST.get('DeleteStuID')
        DeleteStu = models.StuInfo.objects.filter(Stu_ID=DeleteStuID).first().delete()
        return redirect('ManagerStu')
    except:
        print('删除失败，可能没有找到')

def ManagerStu(request):
    Stu_List=models.StuInfo.objects.all()
    if (request.method != 'POST'):
        stuform=forms.Stu_Form()
    elif(request.method == 'POST') & (request.POST.get('AddStu')=='yes'):
        addStu(request)
    stuform = forms.Stu_Form()

    if(request.method == 'POST') & (request.POST.get('DeleteStu')=='yes'):
        deleteStu(request)

    return render(request, 'ManagerStudent.html',{
                                                    'Stu_List':Stu_List,
                                                    'stuform':stuform,
                                                    }
                                                        )

def addTea(request):
    try:
        NewTea = forms.Tea_Form(data=request.POST)
        if NewTea.is_valid():
            #print(NewTea)
       # Tea=models.TchInfo(Tch_ID=request.POST.get('Tch_ID'),
       #                    Tch_Name=request.POST.get('Tch_Name'),
        #                   Tch_Department_id=request.POST.get('Tch_Department'),
        #                   Tch_Position=request.POST.get('Tch_Position'),
        #                   Tch_Username=request.POST.get('Tch_Username'),
        #                   Tch_Password=request.POST.get('Tch_Password')
        #                   )
        #Tea.save()
            NewTea.save()
        return redirect('ManagerTch')
    except:
        print("Add Teacher Error")

def deleteTea(request):
    try:
        DeleteTeaID = request.POST.get('DeleteTeaID')
        DeleteTea = models.TchInfo.objects.filter(Tch_ID=DeleteTeaID).first().delete()
        return redirect('ManagerTch')
    except:
        print('Delete Teacher Error')

def ManagerTch(request):
    print(len("教授"))
    Tch_List = models.TchInfo.objects.all()
    print("*****------*****")
    print(Tch_List)
    if(request.method == 'POST') & (request.POST.get('AddTch') == 'yes'):
        print('1111')
        addTea(request)
    elif(request.method == 'POST') & (request.POST.get('DeleteTch') == 'yes'):
        deleteTea(request)
    teaform = forms.Tea_Form()
    context = {'Tch_List': Tch_List,
               'teaform': teaform,}
    return render(request, 'ManagerTeacher.html', context)

def addCrs(request):
    try:
        Newcrs = forms.Crs_Form(data=request.POST)
        #print(NewStu)
        if Newcrs.is_valid():
            Newcrs.save()
            return redirect('ManagerCrs')
    except:
        print("Add Student Error")

def deleteCrs(request):
    try:
        DeleteCrsID = request.POST.get('DeleteCrsID')
        #print(DeleteStuID)
        DeleteCrs = models.CourseInfo.objects.filter(Crs_ID=DeleteCrsID).first().delete()
        #print(DeleteStu)
        return redirect('ManagerStu')
    except:
        print('删除失败，可能没有找到')


def ManagerCrs(request):

    Crs_List = models.CourseInfo.objects.all()
    #print(Crs_List)
    if (request.method != 'POST'):
        crsform = forms.Crs_Form()
    elif (request.method == 'POST') & (request.POST.get('AddCrs') == 'yes'):
        print(request.POST.get('AddCrs') )
        addCrs(request)
    crsform = forms.Crs_Form()

    if (request.method == 'POST') & (request.POST.get('DeleteCrs') == 'yes'):
        deleteCrs(request)

    return render(request, 'ManagerCourse.html', {
        'Crs_List': Crs_List,
        'crsform': crsform,
    }
                  )


def index(request):
    return render(request,'ManagerTeacher.html')