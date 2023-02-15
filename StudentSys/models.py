from django.db import models

# Create your models here.
class StuInfo(models.Model):
    Stu_ID=models.CharField(max_length=20,primary_key=True)
    Stu_Name=models.CharField(max_length=10)
    Stu_Gender=models.CharField(max_length=5)
    Stu_Age=models.IntegerField()
    Stu_College=models.CharField(max_length=40)
    Stu_Username=models.CharField(max_length=50)
    Stu_Password=models.CharField(max_length=50)
    def __str__(self):
        """返回模型的字符串表示。"""
        return (self.Stu_ID)

class TchInfo(models.Model):
    Tch_ID = models.CharField(max_length=20,primary_key=True)
    Tch_Name = models.CharField(max_length=10)
    Tch_College = models.CharField(max_length=40)
    Tch_Position = models.CharField(max_length=5)
    Tch_Username = models.CharField(max_length=50)
    Tch_Password = models.CharField(max_length=50)
    def __str__(self):
        """返回模型的字符串表示。"""
        return (self.Tch_ID)
