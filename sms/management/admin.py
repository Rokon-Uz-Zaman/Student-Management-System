from django.contrib import admin 
from management.models import Student,Teacher,Staff,ClassName


admin.site.site_header = 'Student MS'
admin.site.site_title = 'Student MS'

class StudentAdmin(admin.ModelAdmin):
	list_display = ('Name','Class_Name','Roll','Active_status')
	list_filter = ('Name','Class_Name','Roll','Active_status')
	list_editable = ('Active_status',)



class TeacherAdmin(admin.ModelAdmin):
	list_display = ('Name','Position','Active_status')
	list_filter = ('Name','Position','Active_status')
	list_editable = ('Active_status',)


class ClassNameAdmin(admin.ModelAdmin):
	list_display = ('Class_Name','Session','Class_Teacher')
	list_filter = ('Class_Name','Session','Class_Teacher')

class StaffAdmin(admin.ModelAdmin):
	list_display = ('Name','Position','Active_status')
	list_filter = ('Name','Position','Active_status')
	list_editable = ('Active_status',)



# Register your models here.
admin.site.register(Student,StudentAdmin)
admin.site.register(Teacher,TeacherAdmin)
admin.site.register(ClassName,ClassNameAdmin)
admin.site.register(Staff,StaffAdmin)
#admin.site.register(Attendence)









