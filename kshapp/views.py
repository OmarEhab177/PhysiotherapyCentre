from django.shortcuts import render
from django.http import  HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages


def index(request) :
    return render(request, 'pages/index.html')


def new(request) :
    if request.method == 'POST':
        add_pat = newform(request.POST)
        add_pat.save()
            
    context = {
        'form':newform(),
    }
    return render(request, 'pages/new.html', context)


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

def new_patient_type(request):
    p_type = PatientTypeForm(request.POST)
    if p_type.is_valid():
        p_type.save()
        messages.add_message(request, messages.INFO, 'Patient type created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating patient type.')
    return HttpResponseRedirect('patients')

def new_disability(request):
    dis_form = DisabilityForm(request.POST)
    if dis_form.is_valid():
        dis_form.save()
        messages.add_message(request, messages.INFO, 'Disability created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Disability.')
    return HttpResponseRedirect('patients')

def section(request) :
    return render(request, 'pages/sections.html')


def therapist(request) :
    if request.method == 'POST':
        add_thr = teacherform(request.POST)
        if add_thr.is_valid():
            add_thr.save()
    context = {
        'form':teacherform(),
        
    }
    return render(request, 'pages/therapist.html',context)


def appointment(request) :
    return render(request, 'pages/Appointment.html')
