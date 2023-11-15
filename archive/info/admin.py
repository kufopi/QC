from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.site_header ="Archive Backend"
admin.site.site_title = 'Student Info'

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    '''Admin View for Student'''

    list_display = ('matric','surname','gce','waec','passport',)
    list_filter = ('surname','gce','jamb','birth_cert')
    
    
    search_fields = ('surname','waec',)
    

