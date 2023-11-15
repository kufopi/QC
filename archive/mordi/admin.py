from django.contrib import admin

# Register your models here.
from .models import Book,Staff,Publication,Conference,Promotion

admin.site.site_header = "CONAS Staff Database"
admin.site.site_title = "CONAS Staff Records"

class PublicationInline(admin.TabularInline):
    model = Publication
    extra=1

class BookInline(admin.TabularInline):
    model = Book
    extra=0

class ConferenceInline(admin.TabularInline):
    model = Conference
    extra =0

class PromotionInline(admin.TabularInline):
    model = Promotion
    extra =0


@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id','surname','gender','passport')
    fields = [('staff_id','surname','middle_name','first_name'),('gender','dob','doe')]
    inlines = [PublicationInline,BookInline,ConferenceInline,PromotionInline]
    search_fields = ('surname',)


admin.site.register(Book)
admin.site.register(Publication)
admin.site.register(Conference)

admin.site.register(Promotion)




