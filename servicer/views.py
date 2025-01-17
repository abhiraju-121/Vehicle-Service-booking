from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from . models import Customer,Staff,Vehicle,Booking,Cars
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def base(request):
    return render(request,'base.html')

def index(request):
    return render(request,'index.html')

def staff_index(request):
    return render(request,'staff_index.html')

def dashboard(request):
    return render(request,'staff_dashboard.html')

def customer_reg(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request,'customer_register.html',{'error':'Username Already exist !!'})
        
        if password!=password2:
            return render(request,'customer_register.html',{'error':'password mismatch !!'})
        
        user=User.objects.create_user(username=username,password=password)

        Customer.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email
        )
        return redirect('customer_log')
    return render(request,'customer_register.html')

def customer_log(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid username or password!')
            return redirect('customer_log')
    return render (request,'customer_log.html')

@login_required
def customer_logout(request):
    logout(request)
    return redirect('base')

def staff_register(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm_password')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')

        if User.objects.filter(username=username).exists():
            return render(request,'staff_register.html',{'error':'Username Already exist !!'})
        if password!=confirm_password:
            return render(request,'staff_register.html',{'error':'password is not matching'})
        
        user=User.objects.create_user(username=username,password=password)

        Staff.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        return redirect('staff_log')
    return render(request,'staff_register.html')

def staff_log(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('staff_index')
        else:
            messages.error(request,'Invalid username or password !!')
            return redirect('staff_log')
    return render(request,'staff_login.html')

@login_required
def staff_logout(request):
    logout(request)
    return redirect('base')

def vehicle(request):
    if request.method=="POST":
        name=request.POST.get('name')
        price=request.POST.get('price')
        brand=request.POST.get('brand')
        is_available=request.POST.get('is_available')=='on'
        description=request.POST.get('description')

        customer=Customer.objects.get(user=request.user)
        items=Vehicle.objects.create(
            name=name,
            price=price,
            brand=brand,
            is_available=is_available,
            description=description,
            owner=customer,
        )
        items.save()
        return redirect('vehicle_list')
    return render (request,'vehicle.html')

def vehicle_list(request):
    items=Vehicle.objects.all()
    return render(request,'vehicle_list.html',{'items':items})

def vehicle_detail(request,item_id):
    detail=get_object_or_404(Vehicle,id=item_id)
    return render(request,'vehicle_detail.html',{'details':detail})

def car(request):
    cars=Cars.objects.all()
    return render(request,'car.html',{"cars":cars})

def car_detail(request,car_id):
    item=get_object_or_404(Cars,id=car_id)
    return render(request,'car.html',{'item':item})

@login_required
def book_service(request):
    customer=Customer.objects.get(user=request.user)
    customer_vehicles = customer.vehicles.all()

    if request.method == "POST":
        service_date = request.POST['service_date']
        service_time = request.POST['service_time']
        comment = request.POST['comment']
        vehicle_id=request.POST.get('vehicle_id')

        vehicle=get_object_or_404(Vehicle,id=vehicle_id)

        book = Booking.objects.create(
            vehicle=vehicle,
            customer=customer,
            service_date=service_date,
            service_time=service_time,
            comment=comment,
        )
        book.save()
        return redirect('booking_history')
    return render(request, 'book_service.html',{'customer_vehicles':customer_vehicles})

@login_required
def approve_booking(request, book_id):
    if not request.user.staff:
        return redirect('staff_index')
    booking = Booking.objects.get(id=book_id)
    booking.status = 'Approved'
    booking.save()
    return redirect('dashboard')

@login_required
def reject_booking(request, book_id):
    if not request.user.staff:
        return redirect('staff_index')
    booking = Booking.objects.get(id=book_id)
    booking.status = 'Rejected'
    booking.save()
    return redirect('approve_booking_list')

@login_required
def approve_booking_list(request):
    if not request.user.staff:
        return redirect('staff_index')
    bookings = Booking.objects.filter(status='Pending')
    return render(request, 'approve_booking.html', {'bookings': bookings})


@login_required
def booking_history(request):
    customer = Customer.objects.get(user=request.user)
    bookings = Booking.objects.filter(customer=customer).order_by('-service_date')
    return render(request, 'booking_history.html', {'bookings': bookings})

