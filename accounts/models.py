from django.db import models

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('patient', 'patient'),
        ('doctor', 'doctor'),
        ('admin', 'admin'),
    ]

    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    role = models.CharField(max_length=8, choices=ROLE_CHOICES, default='patient')

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.username} - {self.role}"

class Doctor(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    user= models.ForeignKey(UserProfile, on_delete=models.CASCADE, to_field='user_id', related_name='doctor_profile')
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)

    class Meta:
        db_table = 'doctor'

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty}"


class TimeSlot(models.Model):
    timeslot_id = models.AutoField(primary_key=True)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, to_field='doctor_id',related_name='timeslots')
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        db_table = 'timeslot'

    def __str__(self):
        return f"{self.doctor.name} - {self.date} ({self.start_time} - {self.end_time})"


class Appointment(models.Model):
    appointment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, to_field='user_id', related_name='user_profile')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, to_field='doctor_id',related_name='appointments')
    date = models.DateField()
    time = models.TimeField()
    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'appointment'

    def __str__(self):
        return f"Appointment with Dr. {self.doctor.name} on {self.date} at {self.time}"