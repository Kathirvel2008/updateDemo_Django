from django.shortcuts import render , redirect
from django.http import HttpResponse
from updateApp.models import Details

# Create your views here.

def login_page(request):
    return render(request , 'login.html')

def details_page(request):
    if request.method == 'POST':
        Name = request.POST.get('name_details')
        print(Name)

        Age = request.POST.get('age_details')
        print(Age)
        
        DOB = request.POST.get('dob_details')
        print(DOB)
        
        Id = request.POST.get('id_details')
        print(Id)
        
        City = request.POST.get('city_details')
        print(City)
        
        Country = request.POST.get('country_details')
        print(Country)

        DB = Details(
        user_name = Name,
        user_age = Age,
        user_dob = DOB,
        user_id = Id,
        user_city = City,
        user_country = Country
        )

        DB.save()

        return redirect('List')
        
    return render(request , 'details.html')

def list_page(request):
    list_details = Details.objects.all()
    return render(request , 'list.html' , {'details_of_list' : list_details})

def delete_page(request , id):
    delete_details = Details.objects.get(id = id)
    delete_details.delete()
    return redirect('List')

def update_page(request , id):
    update_details = Details.objects.get(id = id)
    if request.method == 'POST':
        update_details.user_name = request.POST.get('name')
        update_details.user_age = request.POST.get('age')
        update_details.user_dob = request.POST.get('dob')
        update_details.user_id = request.POST.get('id')
        update_details.user_city = request.POST.get('city')
        update_details.user_country = request.POST.get('country')
       
        update_details.save()
        return redirect('List')

    return render(request , 'update.html' , {'details_of_update' : update_details})
