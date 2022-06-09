
from django.db import models
from django.utils import timezone


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
    photo = models.ImageField(upload_to='images', null=True, blank=True)
    ID_photo = models.ImageField(upload_to='images', null=True, blank=True)
    uplode = models.ImageField(upload_to='images', null=True, blank=True)
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


class Therapist(models.Model):

    therapist_name = models.CharField(max_length=200, null=False, blank=False)
    phone = models.CharField(max_length=200, null=False, blank=False)
    email = models.CharField(max_length=200, null=False, blank=False)
    adress = models.CharField(max_length=200, null=False, blank=False)
    sections = models.ForeignKey(Section, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.therapist_name


class Appointment(models.Model):

    STATUS = (
        ('Attend', 'Attend'),
        ('Absent', 'Absent'),
        ('Excuse of Child', 'Excuse of Child'),
        ('Excuse of therapist', 'Excuse of therapist'),
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

    date = models.DateField(null=True, blank=True) 
    time = models.CharField(max_length=200, null=True, blank=True, choices=Time,unique=True)
    patient_name = models.ForeignKey(Patient, on_delete=models.CASCADE, null=False, blank=False)
    therapist_name = models.ForeignKey(Therapist, on_delete=models.CASCADE, null=False, blank=False)
    note = models.CharField(max_length=200, null=False, blank=False)
    status = models.CharField(max_length=200, null=True, blank=True, choices=STATUS)

    def __str__(self):
        return str(self.patient_name)
