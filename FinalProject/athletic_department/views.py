from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Team, Employee , Athlete, Equipment, Event
from django.views.generic import CreateView, UpdateView, DeleteView, ListView , DetailView
from .forms import TeamForm, EmployeeForm, AthleteForm, EquipmentForm, EventForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def homepage(request):
    return render(request, 'athletic_department/Homepage.html')


class AthleteListView(ListView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_list.html'
    success_url = '/athletes/'

class AthleteCreateView(CreateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_create.html'
    success_url = '/athletes/'

class AthleteUpdateView(UpdateView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_update.html'
    success_url = '/athletes/'

class AthleteDetailView(DetailView):
    model = Athlete
    form_class = AthleteForm
    template_name = 'athletic_department/athlete_detail.html'
    success_url = '/athletes/'

# class AthleteDeleteView(DeleteView):
#    model = Athlete
#    form_class = AthleteForm
#    template_name = 'athletic_department/athlete_delete.html'
#    success_url = '/athletes/'

class AthleteDeleteView(DeleteView):
    model = Athlete
    template_name = 'athletic_department/confirm_ath_delete.html'
    success_url = reverse_lazy('athlete_list')

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        return obj

class EmployeeListView(ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'athletic_department/employees/employee_list.html'
    success_url = '/employees/'    

#def employee_login(request):
   # return render(request, 'athletic_department/employee_login.html')

def employee_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Check if the user is a superuser
            if user.is_superuser:
                return HttpResponseRedirect(reverse('admin:index'))  # Redirect to Django admin
            elif user.is_staff:
                return redirect('employee_dashboard')  # Redirect to the staff dashboard
            else:
                # Optionally handle non-staff users differently
                return redirect('some_general_page')
        else:
            # Return an error message if login fails
            return render(request, 'athletic_department/employee_login.html', {'error': 'Invalid username or password'})
    # If not a POST request, show the login form
    return render(request, 'athletic_department/employee_login.html')

def employee_dashboard(request):
    return render(request, 'athletic_department/employee_dashboard.html')

def athlete_list(request):
    athletes = Athlete.objects.all()  # Retrieves all athletes from the database
    return render(request, 'athletic_department/athlete_list.html', {'athletes': athletes})

def athlete_detail(request, athleteid):
    # Retrieve an athlete by their 'athleteid'
    athlete = get_object_or_404(Athlete, athleteid=athleteid)
    return render(request, 'athletic_department/athlete_detail.html', {'athlete': athlete})

def athlete_delete(request, athleteid):
    athlete = get_object_or_404(Athlete, athleteid=athleteid)
    if request.method == 'POST':
        athlete.delete()
        return redirect('athletic_department:athlete_list')  # Redirect to the athlete list view after deletion
    else:
        return render(request, 'athletic_department/confirm_ath_delete.html', {'athlete': athlete})

# End Athlete Records
# Begin Employee Records

#added 4141045am
class EmployeeCreateView(CreateView):
    model = Employee
    #fields = ['teamid', 'name', 'sport_type', 'ranking', 'email', 'established_date', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    form_class = EmployeeForm
    template_name = 'athletic_department/employee_create.html'
    success_url = reverse_lazy('employee_list')

class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['employeeid', 'firstname', 'lastname', 'email', 'start_date']
    template_name = 'athletic_department/employee_form.html'
    success_url = reverse_lazy('employee_list')  # Ensure you have a URL named 'team_list' 

class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'athletic_department/employee_delete.html'
    success_url = reverse_lazy('employee_list')      

class EmployeeDetailView(DetailView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'athletic_department/employee_detail.html'
    success_url = '/employees/'

def employee_list(request):
    employees = Employee.objects.all()  # Retrieves all athletes from the database
    return render(request, 'athletic_department/employee_list.html', {'employees': employees})

def employee_create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('athletic_department:employee_list')  # Redirect after POST
        else:
            # Re-render the form with validation errors
            return render(request, 'athletic_department/employee_create.html', {'form': form})
    else:
        form = EmployeeForm()  # An unbound form
        return render(request, 'athletic_department/employee_create.html', {'form': form})

def employee_detail(request, employeeid):
    employee = get_object_or_404(Employee, employeeid=employeeid)
    return render(request, 'athletic_department/employee_detail.html', {'employee': employee})

def employee_delete(request, employeeid):
    employee = get_object_or_404(Employee, employeeid=employeeid)
    if request.method == 'POST':
        employee.delete()
        return redirect('athletic_department:employee_list')  # Redirect to the employee list view after deletion
    else:
        return render(request, 'athletic_department/confirm_emp_delete.html', {'employee': employee})

# End Employee Resources
# Begin Team Resources

#class TeamCreateView(CreateView):
    #model = Team
    #template_name = 'athletic_department/team_details.html'
    #fields = ['name', 'sport_type', 'email', 'established_date', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    #success_url = '/teams/'  # Redirect after successful creation

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})

class TeamCreateView(CreateView):
    model = Team
    fields = ['teamid', 'name', 'sport_type', 'ranking', 'email', 'established_date', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    template_name = 'athletic_department/team_create.html'
    success_url = reverse_lazy('team_list')

class TeamUpdateView(UpdateView):
    model = Team
    fields = ['teamid', 'name', 'sport_type', 'ranking', 'email', 'established_date', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    template_name = 'athletic_department/team_form.html'
    success_url = reverse_lazy('team_list')  # Ensure you have a URL named 'team_list'

class TeamDeleteView(DeleteView):
    model = Team
    template_name = 'athletic_department/team_delete.html'
    success_url = reverse_lazy('team_list')  # adjust this to where you want to redirect after deletion  

class TeamDetailView(DetailView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_detail.html'
    success_url = '/teams/'   

class TeamListView(ListView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_list.html'
    success_url = '/teams/'    

def team_delete(request, teamid):
    team = get_object_or_404(Team, teamid=teamid)
    if request.method == 'POST':
        team.delete()
        return redirect('athletic_department:team_list')  # Redirect to the team list view after deletion
    else:
        return render(request, 'athletic_department/confirm_team_delete.html', {'team': team})
    
def team_detail(request, teamid):
    team = get_object_or_404(Team, teamid=teamid)
    return render(request, 'athletic_department/team_detail.html', {'team': team})

def employee_detail(request, employeeid):
    employee = get_object_or_404(Employee, employeeid=employeeid)
    return render(request, 'athletic_department/employee_detail.html', {'employee': employee})

def team_create(request, teamid):
    team = get_object_or_404(Team, teamid=teamid)
    return render(request, 'athletic_department/team_create.html', {'team': team})

# Begin Equipment Resources

class EquipmentCreateView(CreateView):
    model = Equipment
    #fields = ['teamid', 'name', 'sport_type', 'ranking', 'email', 'established_date', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    form_class = EquipmentForm
    template_name = 'athletic_department/equipment_create.html'
    success_url = reverse_lazy('equipment_list')

class EquipmentUpdateView(UpdateView):
    model = Equipment
    fields = ['equipmenteid', 'annual_cost', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    template_name = 'athletic_department/equipment_form.html'
    success_url = reverse_lazy('equipment_list')  # Ensure you have a URL named 'team_list' 

class EquipmentDeleteView(DeleteView):
    model = Equipment
    template_name = 'athletic_department/equipment_delete.html'
    success_url = reverse_lazy('equipment_list')      

class EquipmentDetailView(DetailView):
    model = Equipment
    form_class = EquipmentForm
    template_name = 'athletic_department/equipment_detail.html'
    success_url = '/equipments/'

def equipment_detail(request, equipmentid):
    equipment = get_object_or_404(Equipment, equipmentid=equipmentid)
    return render(request, 'athletic_department/equipment_detail.html', {'equipment': equipment})

def equipment_list(request):
    equipments = Equipment.objects.all()
    return render(request, 'athletic_department/equipment_list.html', {'equipments': equipments})

def equipment_delete(request, equipmentid):
    equipment = get_object_or_404(Equipment, equipmentid=equipmentid)
    if request.method == 'POST':
        equipment.delete()
        return redirect('athletic_department:equipment_list')  # Redirect to the team list view after deletion
    else:
        return render(request, 'athletic_department/confirm_equ_delete.html', {'equipment': equipment})
    
# Begin Event Resources

class EventCreateView(CreateView):
    model = Event
    #fields = ['teamid', 'name', 'sport_type', 'ranking', 'email', 'established_date', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    form_class = EventForm
    template_name = 'athletic_department/event_create.html'
    success_url = reverse_lazy('event_list')

class EventUpdateView(UpdateView):
    model = Event
    fields = ['eventeid', 'annual_cost', 'incomeS1', 'costS1', 'incomeS2', 'costS2']
    template_name = 'athletic_department/event_form.html'
    success_url = reverse_lazy('event_list')  # Ensure you have a URL named 'team_list' 

class EventDeleteView(DeleteView):
    model = Event
    template_name = 'athletic_department/event_delete.html'
    success_url = reverse_lazy('event_list')      

class EventDetailView(DetailView):
    model = Event
    form_class = EventForm
    template_name = 'athletic_department/event_detail.html'
    success_url = '/events/'

def event_detail(request, eventid):
    event = get_object_or_404(Event, eventid=eventid)
    return render(request, 'athletic_department/event_detail.html', {'event': event})

def event_list(request):
    events = Event.objects.all()
    return render(request, 'athletic_department/event_list.html', {'events': events})

def event_delete(request, eventid):
    event = get_object_or_404(Event, eventid=eventid)
    if request.method == 'POST':
        event.delete()
        return redirect('athletic_department:event_list')  # Redirect to the team list view after deletion
    else:
        return render(request, 'athletic_department/confirm_evt_delete.html', {'event': event})    

def event_create(request, eventid):
    event = get_object_or_404(Event, eventid=eventid)
    return render(request, 'athletic_department/event_create.html', {'event': event})    
    
# Begin Admin Reports Resources

