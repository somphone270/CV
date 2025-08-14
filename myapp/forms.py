from django import forms
from myapp.models import Subject, Subscription
from django.forms.widgets import DateInput

class SubjectMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name

from django import forms
from django.forms.widgets import TextInput

class SubscriptionModelForm(forms.ModelForm):
    birthday = forms.DateField(
        label='ວັນເກີດ',
        required=True,
        input_formats=['%Y-%m-%d', '%d/%m/%Y'],
        widget=TextInput(attrs={
            'placeholder': 'YYYY-MM-DD',
            'onfocus': "this.type='date'",
            'onblur': "if(this.value==''){this.type='text'}"
        })
    )


    # subject_set = SubjectMultipleChoiceField(
    #     queryset=Subject.objects.order_by('-is_premium'),
    #     required=True,
    #     label='ສາຂາຮຽນທີ່ສົນໃຈ :',
    #     widget=forms.CheckboxSelectMultiple
    # )

    accepted = forms.BooleanField(
        required=True,
        label="ຂ້ອຍຢືນຢັ້ງວ່າຂໍ້ມູນທັງໝົດແມ່ນຖືກຕ້ອງ"
    )

    class Meta:
        model = Subscription
        fields = [
            'StudentID','gender', 'name', 'name_eng', 'age', 'birthday',
            'email', 'tel', 'province', 'districts', 'village',
            'from_school', 'academic_year', 'semester', 'employee', 'accepted'
        ]
        labels = {
            'StudentID':'ລະຫັດນັກຮຽນ',
            'gender': 'ເພດ',
            'name': 'ຊື່',
            'name_eng': 'ຊື່ (ພາສາອັງກິດ)',
            'age': 'ອາຍຸ',
            'birthday': 'ວັນເກີດ',
            'email': 'ອີເມວ',
            'tel': 'ເບີໂທ',
            'province': 'ແຂວງ',
            'districts': 'ເມືອງ',
            'village': 'ບ້ານ',
            'from_school': 'ມາຈາກໂຮງຮຽນ',
            'academic_year': 'ປີການສຶກສາ',
            'semester': 'ພາກຮຽນ',
            'employee': 'ພະນັກງານ',
            'Language_Level':'ທັກສາພາສາ',
            'Language_Level1':'ທັກສາພາສາ1',
            'Skill_full':'ທັກສະ',
            'accepted': 'ຢືນຢັ້ງຄວາມຖືກຕ້ອງ'
        }
        widgets = {
        'gender': forms.Select(),
}
