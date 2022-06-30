import json
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect, HttpResponse
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .directors import allowed_users


@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def index(request) :
    context = {
    #     'pro':appointment_models.objects.all(),
    #     'allapointment':appointment_models.objects.all().count,
    #     'allpending':appointment_models.objects.filter(status="pending").count,
    #     'alldone':appointment_models.objects.filter(status="Done").count,
        
        }
    return render(request, 'pages/index.html',context)  


@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def patients(request):
    patients = Patient.objects.all()
    patient_form = PatientForm()
    patient_type_form = PatientTypeForm()
    disability_form = DisabilityForm()

    context = {
        'patients': patients,
        'patient_form': patient_form,
        'p_type_form': patient_type_form,
        'disability_form':disability_form
    }
    template = 'pages/patients.html'
    return render(request, template, context)


@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def new_patient(request):
    p_type = request.POST.get('patient_type')
    t_disability = request.POST.get('type_disability')
    patient_type = PatientType.objects.filter(id=int(p_type)).first()
    type_disability = Disability.objects.filter(id=int(t_disability)).first()
    Patient.objects.create(
        name = request.POST.get('name'),
        patient_type = patient_type,
        civil_Id = request.POST.get('civil_Id'),
        type_disability = type_disability,
        Date_Of_Birth = request.POST.get('Date_Of_Birth'),
        email = request.POST.get('email'),
        adress = request.POST.get('adress'),
        phone = request.POST.get('phone'),
        photo = request.POST.get('photo'),
        ID_photo = request.POST.get('ID_photo'),
        uplode = request.POST.get('uplode'),
        gender = request.POST.get('gender'),
        nationality = request.POST.get('nationality'),
        parents_contact = request.POST.get('parents_contact'),
    )
    messages.add_message(request, messages.INFO, 'Patient created successfully.')
    return HttpResponseRedirect('patients')


def view_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    context = {
        'patient': patient
    }
    template = 'pages/patient.html'
    return render(request, template, context)


def delete_patient(request):
    patientID = request.POST['patientID']
    patient = get_object_or_404(Patient, id=patientID)
    patient.delete()
    return HttpResponse(
        json.dumps({
            'status': '1',
            'title': 'Delete Patient',
            'message': 'Patient Deleted Succeessfully'
        })
    )


def edit_patient(request):
    if request.method == "POST":
        patientID = request.POST.get('patientID')
        patient = get_object_or_404(Patient, id=patientID)
        edit_patient = PatientForm(request.POST, request.FILES, instance=patient)
        if edit_patient.is_valid():
            edit_patient.save()
            messages.add_message(request, messages.INFO, 'Patient updated successfully.')
            return HttpResponseRedirect('patients')
        else:
            messages.add_message(request, messages.INFO, 'Invalid data!')
            return HttpResponseRedirect('patients')
    else:
        patientID = request.GET.get('patientID')
        patient = get_object_or_404(Patient, id=patientID)
        edit_patient_form = PatientForm(instance=patient)

        return HttpResponse(
            json.dumps({
                'status': '1',
                'data' : json.dumps(edit_patient_form.as_p())
            })
        )

@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def new_patient_type(request):
    p_type = PatientTypeForm(request.POST)
    if p_type.is_valid():
        p_type.save()
        messages.add_message(request, messages.INFO, 'Patient type created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating patient type.')
    return HttpResponseRedirect('patients')


@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def new_disability(request):
    dis_form = DisabilityForm(request.POST)
    if dis_form.is_valid():
        dis_form.save()
        messages.add_message(request, messages.INFO, 'Disability created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Disability.')
    return HttpResponseRedirect('patients')


@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def section(request) :
    add_sec = SectionForm(request.POST)
    if add_sec.is_valid():
        add_sec.save()
        messages.add_message(request, messages.INFO, 'Section created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Section.')
    context = {
        'sec_form': SectionForm(),
    }
    return render(request, 'pages/sections.html',context)

