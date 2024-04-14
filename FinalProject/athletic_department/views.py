from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Team, Employee , Athlete
from django.views.generic import CreateView, UpdateView, DeleteView, ListView , DetailView
from .forms import TeamForm, EmployeeForm, AthleteForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


def homepage(request):
    return render(request, 'athletic_department/Homepage.html')

def team_list(request):
    teams = Team.objects.all()
    return render(request, 'athletic_department/team_list.html', {'teams': teams})



class TeamCreateView(CreateView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_form.html'
    success_url = '/teams/'

class TeamUpdateView(UpdateView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_form.html'
    success_url = '/teams/'

class TeamDeleteView(DeleteView):
    model = Team
    form_class = TeamForm
    template_name = 'athletic_department/team_form.html'
    success_url = '/teams/'

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
    template_name = 'athletic_department/athlete_confirm_delete.html'
    success_url = reverse_lazy('athlete_list')

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

def athlete_delete(request, pk):
    athlete = get_object_or_404(Athlete, pk=pk)
    if request.method == 'POST':
        athlete.delete()
        return redirect('athlete_list')
    return render(request, 'athletic_department/athlete_confirm_delete.html', {'athlete': athlete})

# End Athlete Records
# Begin Employee Records

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