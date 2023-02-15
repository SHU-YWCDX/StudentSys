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
