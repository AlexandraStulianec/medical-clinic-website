from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import  logout
from django.contrib import messages
from .models import UserProfile, TimeSlot, Doctor, Appointment

#DOCTOR_USERNAMES = ['john_smith', 'keith_doe', 'michael_johnson']

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if UserProfile.objects.filter(username=username).exists():
            messages.error(request, "Username already taken. Try a different one.")
            return redirect('home')

        role = 'patient'

        user_profile = UserProfile(username=username, password=password, role=role)
        user_profile.save()

        messages.success(request, "Account created successfully. Please log in.")
        return redirect('home')

    return render(request, 'signup_popup.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = UserProfile.objects.get(username=username, password=password)
            #print(user)

            if user is not None:
                request.session['username'] = user.username
                request.session['role'] = user.role
                request.session['user_id'] = user.user_id

                role = user.role
                if role == 'patient':
                    return redirect('patient_dashboard')
                elif role == 'doctor':
                    return redirect('doctor_dashboard')
                elif role == 'admin':
                    return redirect('admin_dashboard')
                else:
                    messages.error(request, "Invalid role defined for user.")
                    return redirect('home')
            else:
                messages.error(request, "Invalid username or password.")
                return redirect('home')

        except UserProfile.DoesNotExist:
            messages.error(request, "User profile not found.")
            return redirect('home')

    return render(request, 'login_popup.html')


def patient_dashboard(request):
    username = request.session.get('username', None)
    role = request.session.get('role', None)

    if not username:
        return redirect('home')

    if role == 'patient':
        return render(request, 'patient_dashboard.html', {'username': username})
    else:
        return redirect('home')


def doctor_dashboard(request):
    username = request.session.get('username', None)
    role = request.session.get('role', None)

    if not username:
        return redirect('home')

    if role == 'doctor':
        return render(request, 'doctor_dashboard.html', {'username': username})
    else:
        return redirect('home')


def admin_dashboard(request):
    username = request.session.get('username', None)
    role = request.session.get('role', None)

    if not username:
        return redirect('home')

    if role == 'admin':
        return render(request, 'admin_dashboard.html', {'username': username})
    else:
        return redirect('home')


def logout_view(request):
    logout(request)
    request.session.flush()
    messages.success(request, "Logged out successfully.")
    return redirect('home')

def home(request):
    return render(request, 'login_popup.html')


def manage_availability(request):
    user_id = request.session.get('user_id', None)

    try:
        doctor = Doctor.objects.get(user_id=user_id)
        #print(doctor)
    except Doctor.DoesNotExist:
        messages.error(request, "Doctor not found.")
        return redirect('doctor_dashboard')

    if request.method == 'POST':
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']

        timeslot = TimeSlot(
            doctor_id=doctor.doctor_id,
            date=date,
            start_time=start_time,
            end_time=end_time
        )
        timeslot.save()

        messages.success(request, "Availability set successfully.")
        return redirect('display_timeslots')

    return render(request, 'doctor_dashboard.html')


def display_timeslots(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id', None)

        if not user_id:
            messages.error(request, "User not found.")
            return redirect('home')

        try:
            doctor = Doctor.objects.get(user_id=user_id)
        except Doctor.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect('doctor_dashboard')

        timeslots = TimeSlot.objects.filter(doctor=doctor).order_by('date', 'start_time')

        # if not timeslots:
        #     messages.warning(request, "No available time slots found.")
        return render(request, 'display_timeslots.html', {'timeslots': timeslots})

    else:
        messages.error(request, "Invalid request method.")
        return redirect('doctor_dashboard')


def display_patients_appointments(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id', None)

        if not user_id:
            messages.error(request, "User not found.")
            return redirect('home')

        try:
            doctor = Doctor.objects.get(user_id=user_id)
        except Doctor.DoesNotExist:
            messages.error(request, "Doctor not found.")
            return redirect('doctor_dashboard')

        appointments = Appointment.objects.filter(doctor=doctor)

        # if not appointments:
        #     messages.warning(request, "No appointments found.")
        return render(request, 'display_patients_app.html', {'appointments': appointments})

    else:
        messages.error(request, "Invalid request method.")
        return redirect('doctor_dashboard')



def display_users(request):
    if request.method == 'GET':
        username = request.session.get('username', None)
        user_id = request.session.get('user_id', None)

        users = UserProfile.objects.exclude(user_id=user_id)
        return render(request, 'display_users.html', {'users': users, 'username': username}, )

    elif request.method == 'POST':
        user_id_to_delete = request.POST.get('user_id')

        if user_id_to_delete:
            try:
                user_to_delete = UserProfile.objects.get(user_id=user_id_to_delete)
                user_to_delete.delete()
                messages.success(request, "User deleted successfully.")
            except UserProfile.DoesNotExist:
                messages.error(request, "User not found.")

        return redirect('display_users')
    else:
        messages.error(request, "Invalid request method.")
        return redirect('admin_dashboard')

def add_users(request):
    # user_id = request.session.get('user_id', None)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')

        if not username or not password or not role:
            messages.error(request, "All fields are required.")
            return redirect('add_users')

        if UserProfile.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('add_users')

        user = UserProfile(
            username=username,
            password=password,
            role=role
        )
        user.save()

        messages.success(request, "User added successfully.")
        return redirect('add_users')

    return render(request, 'add_users.html')

def book_appointment_patient(request):
    doctors = Doctor.objects.all()
    selected_doctor_id = request.GET.get('doctor_id', None)
    selected_date = request.GET.get('date', None)
    selected_timeslots = []

    if selected_doctor_id:
        selected_doctor = Doctor.objects.filter(doctor_id=selected_doctor_id).first()
        if selected_doctor:
            if selected_date:
                selected_timeslots = TimeSlot.objects.filter(doctor=selected_doctor, date=selected_date)
            else:
                available_dates = TimeSlot.objects.filter(doctor=selected_doctor).values_list('date', flat=True).distinct()
                selected_timeslots = available_dates

    if request.method == 'POST':
        user_id = request.session.get('user_id', None)
        doctor_id = request.POST.get('doctor_id')
        date = request.POST.get('date')
        time = request.POST.get('time')
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        if not all([doctor_id, date, time, name, phone]):
            messages.error(request, "All fields are required.")
            return redirect('patient_dashboard')

        existing_appointment = Appointment.objects.filter(
                doctor_id=doctor_id,
                date=date,
                time=time
            ).exists()

        if existing_appointment:
            messages.error(request, "The doctor is already booked for this time. Please select another time.")
            return redirect('book_appointment_patient')

        Appointment.objects.create(
            user_id=user_id,
            doctor_id=doctor_id,
            date=date,
            time=time,
            patient_name=name,
            patient_phone=phone
        )
        messages.success(request, "Your appointment has been booked successfully!")
        return redirect('display_appointments')

    return render(request, 'book_appointment.html', {
        'doctors': doctors,
        'selected_doctor_id': selected_doctor_id,
        'selected_timeslots': selected_timeslots,
        'selected_date': selected_date
    })

def display_appointments(request):
    if request.method == 'GET':
        user_id = request.session.get('user_id', None)

        if not user_id:
            messages.error(request, "User not found.")
            return redirect('home')

        try:
            user = UserProfile.objects.get(user_id=user_id)
        except UserProfile.DoesNotExist:
            messages.error(request, "User not found.")
            return redirect('patient_dashboard')

        appointments = Appointment.objects.filter(user=user)

        # if not appointments:
        #     messages.warning(request, "No appointments found.")
        return render(request, 'display_appointments.html', {'appointments': appointments})

    elif request.method == 'POST':
        appointment_id_to_delete = request.POST.get('appointment_id')

        if appointment_id_to_delete:
            try:
                appointment_to_delete = Appointment.objects.get(appointment_id=appointment_id_to_delete)
                appointment_to_delete.delete()
                messages.success(request, "Appointment deleted successfully.")
            except Appointment.DoesNotExist:
                messages.error(request, "Appointment not found.")

        return redirect('display_appointments')

    else:
        messages.error(request, "Invalid request method.")
        return redirect('patient_dashboard')