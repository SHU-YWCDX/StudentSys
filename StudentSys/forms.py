from django import forms
from StudentSys import models


class Stu_Form(forms.ModelForm):
    class Meta:
        model = models.StuInfo
        fields = ('Stu_ID',
                  'Stu_Name',
                  'Stu_Gender',
                  'Stu_Age',
                  'Stu_Department',
                  'Stu_Username',
                  'Stu_Password',)

        labels = {'Stu_ID':'学号',
                  'Stu_Name':'姓名',
                  'Stu_Gender':'性别',
                  'Stu_Age':'年龄',
                  'Stu_Department':'院系',
                  'Stu_Username':'用户名',
                  'Stu_Password':'密码',}


class Crs_Form(forms.ModelForm):
    class Meta:
        model = models.CourseInfo
        fields = ('Crs_ID',
                  'Crs_Name',
                  'Crs_Credit',
                  'Crs_Period',
                  'Crs_Department',
                  )

        labels = {'Crs_ID':'课程号',
                  'Crs_Name':'课程名',
                  'Crs_Credit':'学分',
                  'Crs_Period': '学时',
                  'Crs_Department':'院系',}

class Tea_Form(forms.ModelForm):

    class Meta:
        model = models.TchInfo
        fields = ('Tch_ID',
                  'Tch_Name',
                  'Tch_Department',
                  'Tch_Position',
                  'Tch_Username',
                  'Tch_Password',)

        labels = {'Tch_ID':'工号',
                  'Tch_Name':'姓名',
                  'Tch_Department':'院系',
                  'Tch_Position':'职位',
                  'Tch_Username':'用户名',
                  'Tch_Password':'密码',}


class OfrCrs_Form(forms.ModelForm):
    class Meta:
        model = models.OfferedCourse
        fields = ('OCrs_Term',
                  'OCrs_Course',
                  'OCrs_Teacher',
                  'Ocrs_ClassTime',
                  )

        labels = {'OCrs_Term':'学期',
                  'OCrs_Course':'课程号',
                  'OCrs_Teacher':'教师',
                  'Ocrs_ClassTime':'上课时间',}



class login_form(forms.Form):
    username = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码",   max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))

