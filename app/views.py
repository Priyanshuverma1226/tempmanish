import csv
from django.shortcuts import render, redirect,HttpResponse
from django.contrib import messages
import requests
from .models import myip, ticket_info
# Create your views here.
def index(request):
    return render(request, 'index.html')


def get_ip_details(ip_address):
    response = requests.get(f"http://ipinfo.io/{ip_address}/json")
    data = response.json()

    if response.status_code != 200:
        return f"Error fetching details for IP: {ip_address}"
    
    return data

def upload_csv(request):
    if request.method == 'POST':
        file =request.FILES['file']
        

        decoded_file = file.read().decode('utf-8').splitlines()
        reader = csv.DictReader(decoded_file)
        form1=ticket_info()
        form1.save()
        for i in reader:
            print(i['ip'])
            server_ip=i['ip']
            # Optional: Save data to the database
            details = get_ip_details(server_ip)
            print(details)
            form2=myip(my_ticket=form1,ip=details['ip'],city=details['city'],region=details['region'],country=details['country'],loc=details['loc'],org=details['org'],postal=details['postal'])
            form2.save()
            

        print(reader)
            
           
        return redirect(f'http://127.0.0.1:8000/my_ticket?ticket={form1.id}')
    else:
       
        return HttpResponse("upload_csv")
    

def my_ticket(request):
    ticket=request.GET['ticket']
    print(f"ticket{ticket}")
    obj=myip.objects.filter(my_ticket=ticket)

    print(obj)
    return render(request, 'ip_details.html',{'obj':obj})

def ticket(request):
    return render(request, 'ticket.html')