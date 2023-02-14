from django.db import models

# Create your models here.
class StuInfo(models.Model):
    Stu_ID=models.CharField(max_length=20)
    Stu_Name=models.CharField(max_length=10)
    Stu_Gender=models.CharField(max_length=5)
    Stu_Age=models.IntegerField()
    Stu_College=models.CharField(max_length=40)
    Stu_Username=models.CharField(max_length=50)
    Stu_Password=models.CharField(max_length=50)
    def __str__(self):
            """返回模型的字符串表示。"""
            return (self.Stu_ID)
