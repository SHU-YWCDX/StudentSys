from django import forms
from StudentSys import models

class Stu_Form(forms.ModelForm):
    class Meta:
        model = models.StuInfo
        fields = ('Stu_ID',
                  'Stu_Name',
                  'Stu_Gender',
                  'Stu_Age',
                  'Stu_College',
                  'Stu_Username',
                  'Stu_Password',)

        labels = {'Stu_ID':'学号',
                  'Stu_Name':'姓名',
                  'Stu_Gender':'性别',
                  'Stu_Age':'年龄',
                  'Stu_College':'院系',
                  'Stu_Username':'用户名',
                  'Stu_Password':'密码',}




