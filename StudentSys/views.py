from django.shortcuts import render,redirect
from StudentSys import models
from StudentSys import forms
# Create your views here.



def addStu(request):
    try:
        NewStu = forms.Stu_Form(data=request.POST)
        if NewStu.is_valid():
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
    Tea_List = models.TchInfo.objects.all()
    if(request.method == 'POST') & (request.POST.get('AddTch') == 'yes'):
        addTea(request)
    elif(request.method == 'POST') & (request.POST.get('DeleteTch') == 'yes'):
        deleteTea(request)
    teaform = forms.Tea_Form(request)
    context = {'Tea_List': Tea_List,
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
    print(Crs_List)
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