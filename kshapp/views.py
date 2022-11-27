import csv
import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.utils.timezone import datetime
from django.views.generic.detail import DetailView

from .directors import allowed_users
from .filters import OrderFilter
from .forms import *
from .models import *


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def index(request) :
    today = datetime.now().strftime('%Y-%m-%d')

    context = {
        'pro':Appointment.objects.order_by('-date'),
        'allapointment':Appointment.objects.filter(date=today).count(),
        'allpending':Appointment.objects.filter(action="Pending",date=today).count,
        'alldone':Appointment.objects.filter(status="Attend",date=today).count,
        'allabsent':Appointment.objects.filter(status="Absent",date=today).count,
        'Compensate':Appointment.objects.filter(status="Compensate",date=today).count,
        'male':Patient.objects.filter(gender="Male").count,
        }
    return render(request, 'pages/index.html',context)  


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def patients(request):
    patients = Patient.objects.all()
    patient_form = PatientForm()
    patient_type_form = PatientTypeForm()
    disability_form = DisabilityForm()
    patients_pagination = Paginator(patients, 10)
    page = request.GET.get('page', 1)
    try:
        patients = patients_pagination.page(page)
    except PageNotAnInteger:
        patients = patients_pagination.page(1)
    except EmptyPage:
        patients = patients_pagination.page(patients_pagination.num_pages)

    context = {
        'patients': patients,
        'patient_form': patient_form,
        'p_type_form': patient_type_form,
        'disability_form':disability_form
    }
    template = 'pages/patients.html'
    return render(request, template, context)


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def view_patient(request, pk):
    patient = get_object_or_404(Patient, id=pk)
    context = {
        'patient': patient
    }
    template = 'pages/patient.html'
    return render(request, template, context)


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
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
@allowed_users(allowed_roles=['admin'])
def new_patient_type(request):
    p_type = PatientTypeForm(request.POST)
    if p_type.is_valid():
        p_type.save()
        messages.add_message(request, messages.INFO, 'Patient type created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating patient type.')
    return HttpResponseRedirect('patients')


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def new_disability(request):
    dis_form = DisabilityForm(request.POST)
    if dis_form.is_valid():
        dis_form.save()
        messages.add_message(request, messages.INFO, 'Disability created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Disability.')
    return HttpResponseRedirect('patients')


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def new_appointment(request):
    appoint_form = AppointForm(request.POST)
    if appoint_form.is_valid():
        appoint_form.save()
        messages.add_message(request, messages.INFO, 'Appointment created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating ,Or already exist Appointmentis .')
    return HttpResponseRedirect('appointments')


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def appointments(request):
    appointments = Appointment.objects.order_by('-date')
    appoint_form = AppointForm()
    appointments_pagination = Paginator(appointments, 10)
    page = request.GET.get('page', 1)
    try:
        appointments = appointments_pagination.page(page)
    except PageNotAnInteger:
        appointments = appointments_pagination.page(1)
    except EmptyPage:
        appointments = appointments_pagination.page(appointments_pagination.num_pages)

    context = {
        'appointments': appointments,
        'appoint_form': appoint_form,
        

    }
    template = 'pages/appointments.html'
    return render(request, template, context)


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin', 'therapist'])
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, id=pk)
    context = {
        'appointment': appointment
    }
    template = 'pages/appointment.html'
    return render(request, template, context)
    

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
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

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def sections(request):
    sections = Section.objects.all()
    sec_form = SectionForm()
    context = {
        'sections':sections,
        'sec_form':sec_form,
    }
    template = 'pages/sections.html'
    return render(request, template, context)

@method_decorator(login_required(login_url = 'accounts/login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
class SectionView(DetailView):
    template_name = 'pages/section.html'
    model = Section


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def new_section(request) :
    add_sec = SectionForm(request.POST)
    if add_sec.is_valid():
        add_sec.save()
        messages.add_message(request, messages.INFO, 'Sections created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Sections.')
    return HttpResponseRedirect('sections')

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
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


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def new_therapist(request):
    therapist_group = Group.objects.get(name='therapist') 
    Therapist_form = TherapistForm(request.POST, request.FILES)
    if Therapist_form.is_valid():
        therapist_data = Therapist_form.cleaned_data
        Therapist_form.save()
        therapist = Therapist.objects.get(email = therapist_data['email'])
        therapist_group.user_set.add(therapist)
        messages.add_message(request, messages.INFO, 'Therapist created successfully.')
    else:
        messages.add_message(request, messages.INFO, 'Error while creating Therapist.')
    return HttpResponseRedirect('therapists')


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def therapists(request):
    therapists = Therapist.objects.all()
    therapist_form = TherapistForm()
    therapists_pagination = Paginator(therapists, 1)
    page = request.GET.get('page', 1)
    try:
        therapists = therapists_pagination.page(page)
    except PageNotAnInteger:
        therapists = therapists_pagination.page(1)
    except EmptyPage:
        therapists = therapists_pagination.page(therapists_pagination.num_pages)
    context = {
        'therapists':therapists,
        'therapist_form':therapist_form,
    }
    template = 'pages/therapists.html'
    return render(request, template, context)

@method_decorator(login_required(login_url = 'accounts/login'), name='dispatch')
@method_decorator(allowed_users(allowed_roles=['admin']), name='dispatch')
class TherapistView(DetailView):
    template_name = 'pages/therapist.html'
    model = Therapist


@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
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


#################################################
################# therapist profile #############
@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['therapist'])
def therapist_appointments(request):
    today = datetime.now().strftime('%Y-%m-%d')
    therapist = request.user.therapist

    appointments = request.user.therapist.appointments.filter(date=today).all()
    context = {
        'therapist':therapist,
        'appointments':appointments,
    }

    template = 'pages/therapist-home.html'
    return render(request, template, context)

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['therapist'])
def edit_therapist_appointment(request):
    if request.method == "POST":
        try:
            appID = request.POST.get('appID')
            appoint = get_object_or_404(Appointment, id=appID)
            status = request.POST.get('status')
            note = request.POST.get('note')
            appoint.status = status
            appoint.note = note
            appoint.action = 'Done'
            appoint.save()
            messages.add_message(request, messages.INFO, 'Appointment updated successfully.')
        except:
            messages.add_message(request, messages.INFO, 'Invalid data!')
        return HttpResponseRedirect('/therapist-appointments')
    else:
        appID = request.GET.get('appID')
        appoint = get_object_or_404(Appointment, id=appID)
        edit_appoint_form = AppointForm(instance=appoint)

        return HttpResponse(
            json.dumps({
                'status': '1',
                'data' : json.dumps(edit_appoint_form.as_p())
            })
        )

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['therapist'])
def therapist_all_appointments(request):
    therapist = request.user.therapist
    appointments = request.user.therapist.appointments.all()
    context = {
        'therapist':therapist,
        'appointments':appointments,
    }

    template = 'pages/therapist-all-appointments.html'
    return render(request, template, context)


# all Reports Views 
@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def reports(request):
    #appointments = Appointment.objects.all()
    myFilter = OrderFilter(request.GET, queryset=Appointment.objects.all())
    appointments = myFilter.qs
    context = {
        'appointments': appointments,
        'myFilter':myFilter

    }
    template = 'pages/reports.html'
    return render(request, template,context,)

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def patient_reports(request):
    context = {

    }

    template = 'pages/patient_reports.html'
    return render(request, template,context,)

@login_required(login_url = 'accounts/login')
@allowed_users(allowed_roles=['admin'])
def note(request):

    template = 'pages/note.html'
    return render(request, template)
