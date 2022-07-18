import json
from django.shortcuts import get_object_or_404, render
from django.http import  HttpResponseRedirect, HttpResponse
from django.views.generic.detail import DetailView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .directors import allowed_users
from django.utils import timezone
from django.utils.timezone import datetime


@login_required(login_url = 'accounts/login')
# @allowed_users(allowed_roles=['admin'])
def index(request) :
    context = {
        'pro':Appointment.objects.order_by('-date'),
        'allapointment':Appointment.objects.order_by('-date').count,
        'allpending':Appointment.objects.filter(action="Pending").count,
        'alldone':Appointment.objects.filter(status="Attend").count,
        'allabsent':Appointment.objects.filter(status="Absent").count,
        'Compensate':Appointment.objects.filter(status="Compensate").count,
        
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
        photo = request.FILES.get('photo'),
        ID_photo = request.FILES.get('ID_photo'),
        uplode = request.FILES.get('uplode'),
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
def new_appointment(request):
    appoint_form = AppointForm(request.POST)
    if appoint_form.is_valid():
        appoint_form.save()
        messages.add_message(request, messages.INFO, 'Appointment created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating ,Or already exist Appointmentis .')
    return HttpResponseRedirect('appointments')


@login_required(login_url = 'accounts/login')
def appointments(request):
    appointments = Appointment.objects.order_by('-date')
    appoint_form = AppointForm()
    context = {
        'appointments': appointments,
        'appoint_form': appoint_form,
    }
    template = 'pages/appointments.html'
    return render(request, template, context)

def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    context = {
        'appointment': appointment
    }
    template = 'pages/appointment.html'
    return render(request, template, context)
    


def edit_appoint(request):
    if request.method == "POST":
        appointID = request.POST.get('appointID')
        appoint = get_object_or_404(Appointment, id=appointID)
        edit_appoint = AppointForm(request.POST, instance=appoint)
        if edit_appoint.is_valid():
            edit_appoint.save()
            messages.add_message(request, messages.INFO, 'Appointment updated successfully.')
            return HttpResponseRedirect('appointments')
        else:
            messages.add_message(request, messages.INFO, 'Invalid data!')
            return HttpResponseRedirect('appointments')
    else:
        appointID = request.GET.get('appointID')
        appoint = get_object_or_404(Appointment, id=appointID)
        edit_appoint_form = AppointForm(instance=appoint)

        return HttpResponse(
            json.dumps({
                'status': '1',
                'data' : json.dumps(edit_appoint_form.as_p())
            })
        )


def sections(request):
    sections = Section.objects.all()
    sec_form = SectionForm()
    context = {
        'sections':sections,
        'sec_form':sec_form,
    }
    template = 'pages/sections.html'
    return render(request, template, context)


class SectionView(DetailView):
    template_name = 'pages/section.html'
    model = Section


@login_required(login_url = 'accounts/login')
def new_section(request) :
    add_sec = SectionForm(request.POST)
    if add_sec.is_valid():
        add_sec.save()
        messages.add_message(request, messages.INFO, 'Sections created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Sections.')
    return HttpResponseRedirect('sections')


def edit_section(request):
    if request.method == "POST":
        secID = request.POST.get('secID')
        sec = get_object_or_404(Section, id=secID)
        edit_sec = SectionForm(request.POST, instance=sec)
        if edit_sec.is_valid():
            edit_sec.save()
            messages.add_message(request, messages.INFO, 'Section updated successfully.')
            return HttpResponseRedirect('sections')
        else:
            messages.add_message(request, messages.INFO, 'Invalid data!')
            return HttpResponseRedirect('sections')
    else:
        secID = request.GET.get('secID')
        sec = get_object_or_404(Section, id=secID)
        edit_sec_form = SectionForm(instance=sec)

        return HttpResponse(
            json.dumps({
                'status': '1',
                'data' : json.dumps(edit_sec_form.as_p())
            })
        )

def new_therapist(request):
    Therapist_form = TherapistForm(request.POST, request.FILES)
    if Therapist_form.is_valid():
        Therapist_form.save()
        messages.add_message(request, messages.INFO, 'Therapist created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Therapist.')
    return HttpResponseRedirect('therapists')

def therapists(request):
    therapists = Therapist.objects.all()
    therapist_form = TherapistForm()
    context = {
        'therapists':therapists,
        'therapist_form':therapist_form,
    }
    template = 'pages/therapists.html'
    return render(request, template, context)

class TherapistView(DetailView):
    template_name = 'pages/therapist.html'
    model = Therapist


def edit_therapist(request):
    if request.method == "POST":
        therapistID = request.POST.get('therapistID')
        therapist = get_object_or_404(Therapist, id=therapistID)
        edit_therapist = TherapistForm(request.POST, request.FILES, instance=therapist)
        if edit_therapist.is_valid():
            edit_therapist.save()
            messages.add_message(request, messages.INFO, 'Therapist updated successfully.')
            return HttpResponseRedirect('therapists')
        else:
            messages.add_message(request, messages.INFO, 'Invalid data!')
            return HttpResponseRedirect('therapists')
    else:
        therapistID = request.GET.get('therapistID')
        therapist = get_object_or_404(Therapist, id=therapistID)
        edit_therapist_form = TherapistForm(instance=therapist)

        return HttpResponse(
            json.dumps({
                'status': '1',
                'data' : json.dumps(edit_therapist_form.as_p())
            })
        )

def reports(request):

    context = {
   
    }
    template = 'pages/reports.html'
    return render(request, template, context)