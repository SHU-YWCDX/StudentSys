from django.db import models


# Create your models here.
class DepartInfo(models.Model):
    Dep_ID = models.CharField(max_length=3, primary_key=True)
    Dep_Name = models.CharField(max_length=20)
    Dep_Addr = models.CharField(max_length=40)
    Dep_PhoneNum = models.CharField(max_length=11)

    def __str__(self):
        return self.Dep_ID


class StuInfo(models.Model):
    Stu_ID = models.CharField(max_length=20, primary_key=True)
    Stu_Name = models.CharField(max_length=10)
    Stu_Gender = models.CharField(max_length=5)
    Stu_Age = models.IntegerField()
    Stu_Department = models.ForeignKey('DepartInfo', on_delete=models.CASCADE)
    Stu_Username = models.CharField(max_length=50)
    Stu_Password = models.CharField(max_length=50)

    # Stu_Department.Foreignkey('DepartInfo')
    def __str__(self):
        return self.Stu_ID


class TchInfo(models.Model):
    Tch_ID = models.CharField(max_length=20, primary_key=True)
    Tch_Name = models.CharField(max_length=10)
    # Tch_Department = models.CharField(max_length=40)
    Tch_Department = models.ForeignKey('DepartInfo', on_delete=models.CASCADE)
    Tch_Position = models.CharField(max_length=5)
    Tch_Username = models.CharField(max_length=50)
    Tch_Password = models.CharField(max_length=50)

    def __str__(self):
        return self.Tch_ID


class CourseInfo(models.Model):
    Crs_ID = models.CharField(max_length=20, primary_key=True)
    Crs_Name = models.CharField(max_length=10)
    Crs_Credit = models.IntegerField()
    Crs_Department = models.ForeignKey(DepartInfo, on_delete=models.CASCADE)
    Crs_DepartNum = models.IntegerField()

    # Crs_DepartNum.Foreignkey('DepartInfo')
    def __str__(self):
        return self.Crs_ID
