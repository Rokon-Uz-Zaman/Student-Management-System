from django.db import models

# Create your models here.



class Teacher(models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=255)
	Position=  models.CharField(max_length=255 ,choices = [('junior','junior'),('senior','senior')] )
	
	Address= models.TextField(max_length=255)
	Father = models.CharField(max_length=255)
	Mother = models.CharField(max_length=255)
	Date= models.DateTimeField(blank=True)
	Active_status = models.BooleanField()

	def __str__(self):
		return self.Name



class ClassName(models.Model):
	Class_Name = models.CharField(max_length=10, null=True)
	Session = models.CharField(max_length=10, null=True)
	Class_Teacher = models.OneToOneField(Teacher,on_delete=models.CASCADE)

	def __str__(self):
		return self.Class_Name



#classlist = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10')]
class Student(models.Model):
	id = models.AutoField(primary_key=True)
	
	Name = models.CharField(max_length=255)
	Roll= models.PositiveIntegerField(null=False)
	#Class_Name = models.CharField(max_length=255 ,choices = classlist , default = 'one')
	Class_Name = models.OneToOneField(ClassName,on_delete=models.CASCADE)
	Address= models.TextField(max_length=255)
	Gender =  models.CharField(max_length=255 ,choices = [('M','Male'),('F','Female')] )
	Father = models.CharField(max_length=255)
	Mother = models.CharField(max_length=255)
	#Birth_Date =  models.DateField(blank=True)

	Date= models.DateTimeField(blank=True)
	Active_status = models.BooleanField()

	def __str__(self):
		return self.Name



class Staff(models.Model):
	id = models.AutoField(primary_key=True)
	Name = models.CharField(max_length=255)
	Position=  models.CharField(max_length=255 ,choices = [('clerk','cleark'),('assistant','assistant')] )
	
	Address= models.TextField(max_length=255)
	Father = models.CharField(max_length=255)
	Mother = models.CharField(max_length=255)
	Date= models.DateTimeField(blank=True)
	Active_status = models.BooleanField()

	def __str__(self):
		return self.Name






'''
	
    
    
class Attendence(models.Model):
	roll = models.CharField(max_length=10, null=True)
	user=models.OneToOneField(Student,on_delete=models.CASCADE)
	date = models.DateField()
	cl=models.CharField(max_length=10)
	present_status = models.CharField(max_length=10)

	def __str__(self):
		return self.cl







    

'''