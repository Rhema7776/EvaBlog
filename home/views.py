from django.shortcuts import render, redirect

# Create your views here.
from home.models import Todo,Dev,Tag_level
from home.forms import TodoForm, DevForm
# from home.models import Todo,Taglag,Tag_level,Tagjob,Dev


def home(request):
    todolist = Todo.objects.all()
    dev = Dev.objects.all()

# def fulltime(request):
#     fulltime = Dev.objects.filter(Job__name="Fullname")
#     return render(request, 'fulltime.html')
    # print(todolist)

    # for i in todolist:
    #    print(i.name)
    #    print(i.des)
    context = {"todolist" : todolist, "dev":dev}
    return render(request, 'index.html', context)

def tododetails(request, pk):
    dev = Dev.objects.get(id=pk)
    # todo = Todo.objects.get(id=pk)
    context = {"dev": dev}
    # context = {"todo": todo}
    return render(request, 'details.html', context)

def CreateTodo(request):
    form =TodoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form':form}
    return render(request, 'create.html', context )

    
def update(request, id):
    todo = Todo.objects.get(id=id)
    form =TodoForm(request.POST or None, instance=todo)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form':form, "todo":todo}
    return render(request, 'uptade.html', context )

def todo_delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/')

def fulltime(request):
    fulltime = Dev.objects.filter(job__name="Fullname")

    context = {'fulltime': fulltime}
    return render(request, 'fulltime.html', context)

def internship(request):
    internship = Dev.objects.filter(job__name="Internship")

    context = {'internship': internship}
    return render(request, 'internship.html', context)
def freelance(request):
    freelance = Dev.objects.filter(job__name="Freelance")

    context = {'freelance': freelance}
    return render(request, 'freelance.html', context)
def remote(request):
    remote = Dev.objects.filter(job__name="Remote")

    context = {'remote': remote}
    return render(request, 'remote.html', context)
def parttime(request):
    parttime = Dev.objects.filter(job__name="Part-time")

    context = {'parttime': parttime}
    return render(request, 'parttime.html', context)
def midlevel(request):
    midlevel = Dev.objects.filter(job__name="Midlevel")

    context = {'midlevel': midlevel}
    return render(request, 'midlevel.html', context)
def junior(request):
    junior = Dev.objects.filter(job__name="Junior")

    context = {'junior': junior}
    return render(request, 'junior.html', context)
def beginner(request):
    beginner = Dev.objects.filter(job__name="Beginner")

    context = {'beginner': beginner}
    return render(request, 'beginner.html', context) 
def senior(request):
    senior = Dev.objects.filter(job__name="Senior")

    context = {'senior': senior}   
    return render(request, 'senior.html', context)    
def form(request):
    form =DevForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')

    context = {'form':form}

    return render(request, 'form.html', context)


  
# def CreateTodo(request):
#     form =TodoForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     context = {'form':form}
#     return render(request, 'create.html', context )