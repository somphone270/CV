from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from myapp.forms import SubscriptionModelForm
from myapp.models import Subject
from django.http import HttpResponse
from myapp.models import Subscription
import xlwt



def home (request):
   all_users = Subscription.objects.all()
   context = {'users':all_users}
   return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def Borntobeaschool(request):
    return render(request, 'Borntobeaschool.html')

def Context(request):
    return render(request, 'Context.html')

def subscription(request):
    if request.method == 'POST':      
        form = SubscriptionModelForm(request.POST)
        if form.is_valid():          
            form.save()    
            return HttpResponseRedirect(reverse('subscription_done'))    
        else:
            print("Form Errors:", form.errors)  
    else: 
        form = SubscriptionModelForm()
    return render(request, 'subscription_form.html', {'form': form})

def subscription_done(request):
    return render(request, 'subscription_done.html')



def preview_all(request):
    return render(request, 'preview_all.html')


def subject_list(request):
     subjects = Subject.objects.all()
     return render(request, 'subject.html', {'subjects': subjects})  
 

def subject_detail(request, subject_id):
    one_subject = Subject.objects.get(id=subject_id)
    context = {'subject1': one_subject}
    return render(request, 'myapp/subject_detail.html', context)



def cv_detail(request, sub_id):
    one_sub =Subscription.objects.get(id=sub_id)
    context = {'sub1': one_sub}
    return render(request, 'myapp/Create_CV.html', context)



def studyimages(request):
    return render(request, 'studyimages.html')

# ✅ Export to Excel
def export_subscriptions_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="subscriptions.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Subscriptions')

    row_num = 0
    columns = [
        'ID', 'ຊື່', 'ຊື່ອັງກິດ', 'ເພດ', 'ອາຍຸ', 'ວັນເກີດ',
        'ອີເມວ', 'ໂທລະສັບ', 'ແຂວງ', 'ເມືອງ', 'ບ້ານ',
        'ຈາກໂຮງຮຽນ', 'ປີການສຶກສາ', 'ພາກຮຽນ', 'ສະຖານະ', 'ວັນທີ່ລົງທະບຽນ'
    ]

    for col_num, column_title in enumerate(columns):
        ws.write(row_num, col_num, column_title)

    rows = Subscription.objects.all().values_list(
        'id', 'name', 'name_eng', 'gender', 'age', 'birthday',
        'email', 'tel', 'province', 'districts', 'village',
        'from_school', 'academic_year', 'semester', 'status', 'registered_at'
    )

    for row in rows:
        row_num += 1
        for col_num, cell_value in enumerate(row):
            ws.write(row_num, col_num, str(cell_value))
    wb.save(response)
    return response