from django.db import models
from django.utils import timezone
from django.utils.timezone import datetime
from django.contrib.auth import get_user_model
User = get_user_model()


class Disability(models.Model):

    dis_type = models.CharField(max_length=200, null=False, blank=False)
    note = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.dis_type


class PatientType(models.Model):

    patient_type = models.CharField(max_length=200, null=False, blank=False)
    branch = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.patient_type


class Patient(models.Model):

    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    created = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=250, null=False, blank=False)
    patient_type = models.ForeignKey(PatientType, on_delete=models.CASCADE, null=False, blank=False)
    civil_Id = models.CharField(max_length=200, null=False, blank=False,unique=True)
    type_disability = models.ForeignKey(Disability, on_delete=models.CASCADE, null=False, blank=False) 
    Date_Of_Birth = models.DateField(null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    adress = models.TextField(null=False, blank=False)
    phone = models.CharField(max_length=50, null=False, blank=False)
    photo = models.ImageField(upload_to='images/patients', null=True, blank=True)
    ID_photo = models.ImageField(upload_to='images/patients', null=True, blank=True)
    uplode = models.FileField(upload_to='images/patients', null=True, blank=True)
    gender = models.CharField(max_length=200, null=True, blank=True, choices=GENDER)
    nationality = models.CharField(max_length=200, null=False, blank=False)
    parents_contact = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.name


class Section(models.Model):

    section_service = models.CharField(max_length=200, null=False, blank=False)
    main_section = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.section_service


class Therapist(User):
    phone = models.CharField(max_length=200, null=False, blank=False)
    adress = models.CharField(max_length=200, null=False, blank=False)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, null=False, blank=False)
    avtar = models.ImageField(upload_to='images/therapist', blank=True)
    
    def __str__(self):
        return self.name


class Appointment(models.Model):

    Action = (
        ('Pending', 'Pending'),
        ('Done', 'Done'),

    )    

    STATUS = (
        ('Attend', 'Attend'),
        ('Absent', 'Absent'),
        ('Compensate', 'Compensate'),

    )

    Time = (
        ("8", "8"),
        ("9", "9"),
        ("10", "10"),
        ("11", "11"),
        ("12", "12"),
        ("1", "1"),
        ("2", "2"),
    )

    created = models.DateTimeField(default=timezone.now)
    date = models.DateField(null=True, blank=True) 
    time = models.CharField(max_length=200, null=True, blank=True, choices=Time)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False, blank=False)
    service = models.ForeignKey (Section, on_delete=models.CASCADE, null=True, blank=True)
    note = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)
    action = models.CharField(max_length=200, null=True, blank=True, choices=Action,default='Pending')
    therapist = models.ForeignKey(Therapist, on_delete=models.CASCADE, null=False, blank=False, related_name='appointments')

    class Meta:
        unique_together = (('date', 'time', 'therapist'), ('date', 'time', 'patient'))

    def __str__(self):
        return str(self.patient)
