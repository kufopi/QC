from django.db import models
from datetime import date
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
SESSION = [tuple([str(x)+'/'+str(x+1),str(x)+'/'+str(x+1)]) for x in range(2019,2023,1)]
GENDER = (
    ('M','M'),
    ('F','F'),
)
DEPARTMENT = (
    ('Computer Science','Computer Science'),
    ('Physics','Physics'),
    ('Biochemistry','Biochemistry'),
    ('Microbiology','Microbiology'),
    ('Mathematics','Mathematics'),
    ('Chemistry','Chemistry'),
)


    


class Staff(models.Model):
    user = models.OneToOneField(User,  on_delete=models.CASCADE)
    staff_id = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,blank=True)
    first_name = models.CharField(max_length=50)
    gender = models.CharField(choices=GENDER, max_length=50)
    dob = models.DateField(help_text='Date of Birth', blank=True, null=True)
    doe = models.DateField(help_text='Date of Employment', null=True)
    cv_pdf = models.FileField( upload_to='CV', help_text='Your PDF CV',blank=True)
    registration_date = models.DateTimeField( auto_now=True)
    department  = models.CharField(choices=DEPARTMENT, default='Chemistry',max_length=50)
    phone = models.CharField(default='0801-2398-656', max_length=50)
    email = models.EmailField(default='you@chrislanduniversity.edu.ng', max_length=254)
    passport = models.ImageField(upload_to='passport/', blank=True,default='albinopin.jpg')
    """Model definition for Staff."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Staff."""

        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'

    def __str__(self):
        """Unicode representation of Staff."""
        return f'{self.surname} {self.first_name}'

    @property
    def service_year(self):
        today = date.today()
        age = relativedelta(today, self.doe)
        return f'{age.months+(age.years * 12)} months'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Staff.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.staff.save()



class Publication(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    
    article_title = models.CharField(max_length=50)
    co_authors= models.TextField(max_length=50)
    journal_name = models.CharField(max_length=50)
    publication_date = models.DateField(help_text="Date of Publication")
    abstract = models.TextField(help_text = "Enter the Abstract")
    reg_date = models.DateTimeField( auto_now=True)
    published = models.BooleanField(help_text='Has it been published?')

    """Model definition for Publications."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Publications."""

        verbose_name = 'Publication'
        verbose_name_plural = 'Publications'

    def __str__(self):
        """Unicode representation of Publications."""
        return f'{self.article_title}--- {self.publication_date}'

class Conference(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    conference_theme= models.CharField( max_length=50)
    organising_body = models.CharField( max_length=50)
    conference_date = models.DateField(help_text="Date of conference/Seminar")
    made_presentation = models.BooleanField()
    abstract = models.TextField(help_text = "Enter the Abstract")
    reg_date = models.DateTimeField( auto_now=True)
    """Model definition for Conference."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Conference."""

        verbose_name = 'Conference'
        verbose_name_plural = 'Conferences'

    def __str__(self):
        """Unicode representation of Conference."""
        return f'{self.conference_theme}'


class Book(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    book_title = models.CharField(max_length=50)
    co_authors= models.TextField(max_length=50)
    publisher = models.CharField(max_length=50)
    chapter_title = models.CharField(blank=True, max_length=50,help_text="Optional")
    """Model definition for Book."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Book."""

        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        """Unicode representation of Book."""
        return f'{self.book_title}'

class Promotion(models.Model):
    user = models.ForeignKey(Staff, on_delete=models.CASCADE)
    designation = models.CharField( max_length=50)
    promotion_date= models.DateField(help_text="Promotion effective from..")

    """Model definition for Promotion."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for Promotion."""

        verbose_name = 'Promotion'
        verbose_name_plural = 'Promotions'

    def __str__(self):
        """Unicode representation of Promotion."""
        return f'{self.user.staff_id}---{self.designation}---{self.promotion_date}'


