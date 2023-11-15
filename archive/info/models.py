from django.db import models

# Create your models here.

SESSION = [tuple([str(x)+'/'+str(x+1),str(x)+'/'+str(x+1)]) for x in range(2019,2023,1)]
GENDER = (
    ('M','M'),
    ('F','F'),
)

class Student(models.Model):
    matric = models.CharField( max_length=50,primary_key=True)
    surname = models.CharField( max_length=50)
    firstname = models.CharField(max_length=50)
    middlename =models.CharField(max_length=50,blank=True)
    gender = models.CharField(choices=GENDER, max_length=50)
    DoB = models.DateField(help_text='Date of Birth')
    department = models.CharField( max_length=50)
    graduating_year =models.CharField(choices=SESSION, max_length=50)
    gce = models.ImageField( upload_to='gce/', blank=True)
    waec =models.ImageField( upload_to='waec/', blank=True)
    jamb = models.ImageField( upload_to='jamb/', blank=True)
    birth_cert = models.ImageField( upload_to='birth/', blank=True)
    passport = models.ImageField( upload_to='passport/', blank=True)
    date_reg = models.DateTimeField( auto_now=True)


    

    class Meta:
        verbose_name = ("Student")
        verbose_name_plural = ("Students")
        ordering = ['surname']

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse("Student_detail", kwargs={"pk": self.pk})
