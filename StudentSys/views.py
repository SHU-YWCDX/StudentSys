from django.shortcuts import render,redirect
from StudentSys import models
from StudentSys import forms
# Create your views here.



def addStu(request):
    try:
        NewStu = forms.Stu_Form(data=request.POST)
        if NewStu.is_valid():
            if models.StuInfo.objects.filter(Stu_Name=NewStu.Meta.model.Stu_Name) is not None:
                print("Username has existed")
            #print(NewStu)

            #print(request.POST.get('Stu_Department'))

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
    if not (request.session.get('is_login', None) == True) & (request.session.get('mode', None) == '管理员'):#判断登录的模式是不是管理员，不是管理员的话就调转到/logout
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
           # print(models.TchInfo.objects.filter(Tch_Username=NewTea.Meta.model.Tch_Username))
            if models.TchInfo.objects.filter(Tch_Username=NewTea.Meta.model.Tch_Username) is not None:
                print("Username has existed")
            #print(NewTea)
       # Tea=models.TchInfo(Tch_ID=request.POST.get('Tch_ID'),
       #                    Tch_Name=request.POST.get('Tch_Name'),
        #                   Tch_Department_id=request.POST.get('Tch_Department'),
        #                   Tch_Position=request.POST.get('Tch_Position'),
        #                   Tch_Username=request.POST.get('Tch_Username'),
        #                   Tch_Password=request.POST.get('Tch_Password')
        #                   )
        #Tea.save()
            else:
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
    if not (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='教师'):#判断登录模式是不是教师，不是就跳转到登录页
        return redirect('/login')
    #根据用户名筛选出登录的Teacher
    theTeacher = models.TchInfo.objects.filter(Tch_ID=request.session.get('user_id')).first()
    #筛选出该Teacher开设的课程(在OfferedCourse中筛选)
    OfferCrs_List = models.OfferedCourse.objects.filter(OCrs_Teacher=theTeacher)
    crsid=request.GET.get('tcrsid')#见Teacher.html 136行的url，此处的tcrsid参数就是从那里传过来的
    crs=models.OfferedCourse.objects.filter(id=crsid).first()
    #筛选出选了当前课程的学生(在选课表中筛选)
    SelectCrs_List = models.SelectCourse.objects.filter(SelCrs_Course=crs)

    print("*****************")
    if (request.method =='POST')&(request.POST.get('AddGrade')=='yes'):#判断是否是添加成绩的POST
        slctform = forms.Grade_Form(data=request.POST)
        if slctform.is_valid():
            slcStuID=slctform.cleaned_data['ID']
            slcStuGrade=slctform.cleaned_data['Grade']
            slcstu=models.StuInfo.objects.filter(Stu_ID=slcStuID).first()#根据ID筛选学生信息
            print(slcStuGrade)
            print(slcstu)
            slcitem=models.SelectCourse.objects.filter(SelCrs_Stu=slcstu, SelCrs_Course=crs).update(SelCrs_Grade=slcStuGrade)#根据学生和课程在选课表里筛选出对应的记录，把它的成绩进行更新
            print(slcitem)
    slctform = forms.Grade_Form()
    return render(request,'Teacher.html',{
        'OfferCrs_List' : OfferCrs_List,#前端需要的参数都传入
        'SelectCrs_List' : SelectCrs_List,
        'slctform' : slctform,
        'crs':crs
                                         })

#学生函数：
"""
先判断登录
前端左列显示三个链接：
1.选课
2.退课
3.已修课程(可看到成绩单)
选课:
后端筛选出开课表中所有信息在前端列出
前端可列出一张开课单，后端筛选出后以筛选出后在选课表填入相应信息
退课:
后端筛选出该学生选的所有课程在前端列出
前端可填相关信息，供后端正确筛选出，然后delete掉
已修课程：
列出该学生所有选课信息,（成绩为空的去掉，这个功能暂时不做，把该学生所有选课信息筛选出并列出就是成功）

前端参照Teacher
建议创建3个html
分别对应选课，退课，已修课程
"""

#选课
def addSelCrs(request):
        if not (request.session.get('is_login', None) == True) & (request.session.get('mode', None) == '学生'):
            return redirect('/login')
        #列出所有或者指定的课程
        #print('sssss')
        if (request.method == 'POST') & (request.POST.get('search') == 'yes'):
            crsinfo=models.CourseInfo.objects.filter(Crs_Name=request.POST.get('Crs_name'))
            print(crsinfo)
            OfrCrs_List=[]
            for crsitem in crsinfo:
                OfrCrs_List += models.OfferedCourse.objects.filter(OCrs_Course = crsitem)
            print('yes')
        else:
            OfrCrs_List = models.OfferedCourse.objects.all()
            #print('no')
        if (request.method == 'POST') & (request.POST.get('AddCrs') == 'yes'):
            New_SelCrs = forms.SelCrs_Form(data=request.POST)
            if New_SelCrs.is_valid():
                if models.SelectCourse.objects.filter(SelCrs_Stu=models.StuInfo.objects.get(Stu_ID=request.session['user_id']),
                                                      SelCrs_Course=New_SelCrs.cleaned_data['SelCrs_Course']).first() is not None:
                    print("You have chosen this course")
                else:
                    SeldCrs=New_SelCrs.cleaned_data['SelCrs_Course']
                    Stu=models.StuInfo.objects.filter(Stu_ID=request.session.get('user_id')).first()
                    print(Stu)
                    selCrs=models.SelectCourse(SelCrs_Stu=Stu,SelCrs_Course=SeldCrs)
                    selCrs.save()
        SelCrsform = forms.SelCrs_Form()
        #SelCrsform.Meta.model.SelCrs_Course.empty_label = "******"
        #print(SelCrsform.Meta.model.SelCrs_Course.empty_label)
        #print(SelCrsform.Meta.model.SelCrs_Course.queryset)
        searchform = forms.search_Crs()
        context = {'OfrCrs_List': OfrCrs_List,
                   'SelCrsform': SelCrsform,
                   'searchform': searchform}
        return render(request, 'addSelCrs.html', context)


#退课
def delSelCrs(request):
    if not (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='学生'):
        return redirect('/login')
    #获取学生的选课表
    SelCrs_List = models.SelectCourse.objects.filter(SelCrs_Stu=models.StuInfo.objects.get(Stu_ID=request.session['user_id']))
    if (request.method == 'POST') & (request.POST.get('DelCrs') == 'yes'):
        Delcrs = forms.stu_dele_form(data=request.POST)
#        print(Delcrs)
        if(Delcrs.is_valid()):
            if models.SelectCourse.objects.filter(id=Delcrs.cleaned_data['id'],
                                                  SelCrs_Stu=models.StuInfo.objects.get(Stu_ID=request.session['user_id'])).first() is None:
                print("You have not this course")
            else:
                models.SelectCourse.objects.filter(id=Delcrs.cleaned_data['id']).delete()
    #searchform = forms.search_Crs()
    Delcrs = forms.stu_dele_form()
    context = {'SelCrs_List': SelCrs_List,
               'Delcrs': Delcrs}
    return render(request, 'delSelCrs.html', context)
#已修课程
def viewSelCrs(request):
    if not (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='学生'):
        return redirect('/login')
    SelCrs_List = models.SelectCourse.objects.filter(SelCrs_Stu=models.StuInfo.objects.get(Stu_ID=request.session['user_id']))
    context = {'SelCrs_List': SelCrs_List}
    return render(request, 'viewSelCrs.html', context)

#学生函数
def Students(request):
    if not (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='学生'):
        return redirect('/login')
    return redirect('/student/select')

#登录功能实现
def login(request):
    if (request.session.get('is_login', None)==True) &( request.session.get('mode', None)=='管理员'):#判断是否登录过，登陆过就直接跳转到/stu,
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
                user = models.TchInfo.objects.filter(Tch_Username=username).first()
                if user.Tch_Password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.Tch_ID
                    request.session['user_name'] = user.Tch_Name
                    request.session['mode'] = '教师'
                    return redirect('/teacher')
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
                    return redirect('/student')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
    return render(request,'login.html',{'login_form':login_form,
                                        'message':message,
                                        })


def logout(request):
     if not request.session.get('is_login', None):#logout就是刷新session,即清空了登录信息，然后再跳转到login
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