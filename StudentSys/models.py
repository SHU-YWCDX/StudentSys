from django.db import models

# Create your models here.
class DepartInfo(models.Model):
    Dep_ID=models.CharField(max_length = 3, primary_key=True)
    Dep_Name=models.CharField(max_length = 20)
    Dep_Addr=models.CharField(max_length = 40)
    Dep_PhoneNum=models.CharField(max_length = 11)

    def __str__(self):
        return self.Dep_Name

class StuInfo(models.Model):
    Stu_ID=models.CharField(max_length=20, primary_key=True)
    Stu_Name=models.CharField(max_length=10)
    Stu_Gender=models.CharField(max_length=5)
    Stu_Age=models.IntegerField()
    Stu_Department=models.ForeignKey('DepartInfo',on_delete=models.CASCADE)
    Stu_Username=models.CharField(max_length=50)
    Stu_Password=models.CharField(max_length=50)

    #Stu_Department.Foreignkey('DepartInfo')
    def __str__(self):
        return self.Stu_ID

class TchInfo(models.Model):
    Tch_ID = models.CharField(max_length=20,primary_key=True)
    Tch_Name = models.CharField(max_length=10)
    Tch_Department = models.ForeignKey('DepartInfo',on_delete=models.CASCADE)
    Tch_Position = models.CharField(max_length=10)
    Tch_Username = models.CharField(max_length=50)
    Tch_Password = models.CharField(max_length=50)
    def __str__(self):
        return '['+self.Tch_ID+'] '+self.Tch_Name

class CourseInfo(models.Model):
    Crs_ID = models.CharField(max_length=20, primary_key=True)
    Crs_Name = models.CharField(max_length=10)
    Crs_Credit = models.IntegerField()
    Crs_Department = models.ForeignKey(DepartInfo,on_delete=models.CASCADE)
    Crs_Period = models.IntegerField()
   # Crs_DepartNum.Foreignkey('DepartInfo')
    def __str__(self):
        return '['+self.Crs_ID+'] '+self.Crs_Name

"""
CASCADE:这就是默认的选项，级联删除，你无需显性指定它。
PROTECT: 保护模式，如果采用该选项，删除的时候，会抛出ProtectedError错误。
SET_NULL: 置空模式，删除的时候，外键字段被设置为空，前提就是blank=True, null=True,定义该字段的时候，允许为空。
SET_DEFAULT: 置默认值，删除的时候，外键字段设置为默认值，所以定义外键的时候注意加上一个默认值。
SET(): 自定义一个值，该值当然只能是对应的实体了
"""

class OfferedCourse(models.Model):
    OCrs_Term = models.CharField(max_length=20)
    OCrs_Course = models.ForeignKey(CourseInfo, on_delete=models.PROTECT)
    OCrs_Teacher = models.ForeignKey(TchInfo, on_delete=models.PROTECT)
    Ocrs_ClassTime = models.CharField(max_length=50)

    def __str__(self):
        return self.OCrs_Term+' '+self.OCrs_Course.Crs_ID+' '+self.OCrs_Course.Crs_Name+' '+self.OCrs_Teacher.Tch_ID+' '+self.OCrs_Teacher.Tch_Name


class SelectCourse(models.Model):
    SelCrs_Stu=models.ForeignKey(StuInfo, on_delete=models.PROTECT)
    SelCrs_Course=models.ForeignKey(OfferedCourse,on_delete=models.PROTECT)
    SelCrs_Grade=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.SelCrs_Stu.Stu_ID + ' ' + self.SelCrs_Course.OCrs_Course.Crs_Name
