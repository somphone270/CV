# admin.site.register(Subject, SubjectAdmin)
from import_export import resources
from import_export.fields import Field
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from myapp.models import Subscription, Subject
from django.contrib import admin
from .models import MyModel

# Resource
class SubscriptionResource(resources.ModelResource):
    subject_names = Field(column_name='subject_names')

    def dehydrate_subject_names(self, obj):
        return ", ".join([s.name for s in obj.subject_set.all()])

    class Meta:
        model = Subscription
        fields = (
            'id', 'name', 'gender', 'name_eng', 'age','profile','Skills','birthday', 'email', 'province',
            'province_school','districts_school','village_school','Mo','Language','Language1','Language2','Nationality','Parents_contact',
            'districts', 'village', 'tel', 'from_school', 'academic_year','Religion','Other_Skill','Ability1','Ability2','Ability3','Work','School'
            'employee', 'semester', 'status', 'registered_at', 'subject_names','Language_Level','Language_Level2','Skill_full','Detail_Skill'
        )

# Subscription Admin
class SubscriptionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SubscriptionResource
    list_display = [
        'StudentID','gender', 'name','photo', 'name_eng','age', 'birthday', 'email', 'province','Facebook','subject',
        'districts', 'Current_village','Current_village','Current_districts','province', 'tel', 'from_school', 'academic_year',
        'employee', 'semester', 'status', 'registered_at'
    ]
    search_fields = ['name', 'email']
    list_filter = ['status']

    def get_subject_names(self, obj):
        return ", ".join([s.name for s in obj.subject_set.all()])
    get_subject_names.short_description = 'ສາຂາຮຽນ'

# Subject Admin
class SubjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name', 'is_premium', 'price', 'photo', 'description', 'promotion_end_at']
    search_fields = ['name']

# Register
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Subject, SubjectAdmin)

admin.site.register(MyModel, fields=('my_image_thumbnail',), readonly_fields=('my_image_thumbnail',))