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
    if not (request.session.get('is_login', None) == True) & (request.session.get('mode', None) == '管理员'):
        print(request.session.get('mode', None))
        return redirect('/logout')
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
    if not (request.session.get('is_login', None) == True) & (request.session.get('mode', None) == '管理员'):
        return redirect('/logout')
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
    if not (request.session.get('is_login', None) == True) & (request.session.get('mode', None) == '管理员'):
        return redirect('/logout')
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


def addOfferCrs(request):
    try:
        Newcrs = forms.OfrCrs_Form(data=request.POST)
        #print(NewStu)
        if Newcrs.is_valid():
            Newcrs.save()
            return redirect('ManagerOfrCrs')
    except:
        print("Add Student Error")

def deleteOfferCrs(request):
    #try:
        Delcrs = forms.OfrCrs_Form(data=request.POST)
        # print(NewStu)
        if Delcrs.is_valid():
            DelOfCrs=models.OfferedCourse.objects.filter(
                                                            OCrs_Term = Delcrs.cleaned_data['OCrs_Term'],
                                                            OCrs_Course = Delcrs.cleaned_data['OCrs_Course'],
                                                            OCrs_Teacher = Delcrs.cleaned_data['OCrs_Teacher'],
                                                            Ocrs_ClassTime = Delcrs.cleaned_data['Ocrs_ClassTime'],
            ).delete()
            return redirect('/')
    #except:
    #    print('删除失败，可能没有找到')


def ManagerOfrCrs(request):
    if not (request.session.get('is_login', None) == True) & (request.session.get('mode', None) == '管理员'):
        return redirect('/logout')
    OfferCrs_List = models.OfferedCourse.objects.all()
    #print(Crs_List)
    if (request.method != 'POST'):
        Offercrsform = forms.OfrCrs_Form()
    elif (request.method == 'POST') & (request.POST.get('AddOfferCrs') == 'yes'):
        print(request.POST.get('AddOfferCrs') )
        addOfferCrs(request)
    Offercrsform = forms.OfrCrs_Form()
    DelOfcrsform = forms.OfrCrs_Form()
    if (request.method == 'POST') & (request.POST.get('DeleteOfferCrs') == 'yes'):
        deleteOfferCrs(request)

    return render(request, 'ManagerOfferCourse.html', {
        'OfferCrs_List': OfferCrs_List,
        'Offercrsform': Offercrsform,
        'DelOfcrsform': DelOfcrsform,
    }
                  )

def Teacher(request):
    if not (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='教师'):
        return redirect('/login')
    theTeacher = models.TchInfo.objects.filter(Tch_ID=request.session.get('user_id')).first()
    OfferCrs_List = models.OfferedCourse.objects.filter(OCrs_Teacher=theTeacher)
    crs=request.GET.get('crs')
    print("选的课是")
    print(crs)
    SelectCrs_List = models.SelectCourse.objects.filter(SelCrs_Course=crs)
    slctform = forms.Select_Form()
    print("*****************")
    print(slctform)
    return render(request,'Teacher.html',{
        'OfferCrs_List' : OfferCrs_List,
        'SelectCrs_List' : SelectCrs_List,
        'slctform' : slctform,
                                            })

def login(request):
    if (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='管理员'):
        return redirect('/stu')
    message=''
    if (request.method != 'POST'):
        login_form=forms.login_form()
    else:
        login_form=forms.login_form(data=request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']

            #管理员登录
            if username == '123456':
                if password == '123456':
                    request.session['is_login'] = True
                    request.session['user_id'] = username
                    request.session['user_name'] = '管理员'
                    request.session['mode'] = '管理员'
                    return redirect('/stu')
                else:
                    message = "密码不正确！"
            else:
                message = "用户不存在！"
            #教师登录
            try:
                user = models.TchInfo.objects.get(Tch_Username=username)
                if user.Tch_Password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.Tch_ID
                    request.session['user_name'] = user.Tch_Name
                    request.session['mode'] = '教师'
                    return redirect('/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
            #学生登录
            try:
                user = models.StuInfo.objects.get(Stu_Username=username)
                if user.Stu_Password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.Stu_ID
                    request.session['user_name'] = user.Stu_Name
                    request.session['mode'] = '学生'
                    return redirect('/stu')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
    return render(request,'login.html',{'login_form':login_form,
                                        'message':message,
                                        })


def logout(request):
     if not request.session.get('is_login', None):
      # 如果本来就未登录，也就没有登出一说
      return redirect("/login")
     request.session.flush()
     # 或者使用下面的方法
     # del request.session['is_login']
     # del request.session['user_id']
     # del request.session['user_name']
     return redirect("/login")

def test(request):
    return render(request,'Teacher.html')