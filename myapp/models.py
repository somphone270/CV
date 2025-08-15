from django.db import models
from django.contrib.admin.decorators import display
from django.db.models import Model
from django.db.models.fields.files import ImageField
from django.template.loader import get_template


class Subject(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='subject_photos/', blank=True, null=True)
    description = models.TextField(blank=True, null=True, default='')
    price = models.CharField(max_length=255, null=True, blank=True, default='')
    is_premium = models.BooleanField(default=False)
    promotion_end_at = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    GENDER_CHOICES = [
        ('Mr', 'ຊາຍ'),
        ('Miss', 'ຍິງ'),
    ]
    Work = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]
    School = [
        ('YES', 'YES'),
        ('NO', 'NO'),
    ]

    STATUS = [
        ('unapproved', 'Unapproved'),
        ('approved', 'Approved'),
    ]

    # Personal Info
    # id = models.AutoField()
    StudentID = models.CharField(max_length=60, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    name = models.CharField(max_length=60)
    name_eng = models.CharField(max_length=60)
    age = models.CharField(max_length=10)
    birthday = models.DateField(null=True, blank=True)
    photo = models.ImageField(blank=True, null=True)
    Profile = models.TextField(blank=True, null=True, default='')
    Nationality = models.CharField(max_length=60, blank=True)
    Religion= models.CharField(max_length=60, blank=True)
    # Contact Info
    email = models.EmailField(max_length=60, unique=True)
    tel = models.CharField(max_length=20)
    province = models.CharField(max_length=60)
    districts = models.CharField(max_length=60)
    village = models.CharField(max_length=60)
    Current_province = models.CharField(max_length=60,blank=True)
    Current_districts = models.CharField(max_length=60 ,blank=True)
    Current_village = models.CharField(max_length=60,blank=True)
    Facebook = models.CharField(max_length=100, blank=True)
    Parents_contact = models.CharField(max_length=100, blank=True)

    # Education & Work
    from_school = models.CharField(max_length=60)
    academic_year = models.CharField(max_length=60)
    semester = models.CharField(max_length=60)
    employee = models.CharField(max_length=100, blank=True)
    subject = models.CharField(max_length=60,blank=True)
    province_school = models.CharField(max_length=60,blank=True)
    districts_school = models.CharField(max_length=60,blank=True)
    village_school = models.CharField(max_length=60,blank=True)
    Mo = models.CharField(max_length=60,blank=True)


    # System Fields
    Language = models.CharField(max_length=60 ,blank=True)
    Language1 = models.CharField(max_length=60 ,blank=True)
    Language2 = models.CharField(max_length=60 ,blank=True)
    Language_Level1 = models.TextField(blank=True, null=True, default='') 
    Language_Level2 = models.TextField(blank=True, null=True, default='')
    Skill = models.CharField(max_length=60 ,blank=True)
    Skill_full =models.TextField(blank=True, null=True, default='')
    Other_Skill = models.CharField(blank=True, null=True, default='')
    status = models.CharField(max_length=15, choices=STATUS, default='unapproved')
    registered_at = models.DateTimeField(auto_now_add=True)
    Ability1 = models.CharField(max_length=60 ,blank=True)
    Ability2 = models.CharField(max_length=60 ,blank=True)
    Ability3 = models.CharField(max_length=60 ,blank=True)
    Work = models.CharField(max_length=60 ,blank=True,choices=Work)
    School = models.CharField(max_length=60 ,blank=True,choices=School)
    Detail_Skill = models.CharField(blank=True, null=True, default='')
    
   

    def __str__(self):
        return f'{self.name} (id={self.id})'
    
    
class MyModel(Model):
    my_image_field = ImageField()

    # This is our new field. It renders a preview of the image before and post save.
    @display(description='Preview')
    def my_image_thumbnail(self):
        return get_template('my_image_thumbnail_template.html').render({
            'field_name': 'my_image_field',
            'src': self.my_image_field.url if self.my_image_field else None,
        })
