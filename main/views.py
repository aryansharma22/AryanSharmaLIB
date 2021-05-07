from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Books, Item
from .forms import AddNewBook

# Create your views here.

def index(response, id):
    ls = Books.objects.get(id=id)

    if ls in response.user.books.all():

        if response.method =="POST":
            print(response.POST)
            if response.POST.get("save"):
                for item in ls.item_set.all():
                    if response.POST.get("c"+str(item.id)) == "clicked":
                        item.complete = True
                    else:
                        item.complete =  False

                    item.save()

            elif response.POST.get("Addmore"):
                txt = response.POST.get("new")

                if len(txt) > 2:
                    ls.item_set.create(text=txt, complete=False)
                else:
                    print("invalid")                    


        return render(response, "main/list.html", {"ls":ls})
    return ender(response, "main/view.html", {"ls":ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        form = AddNewBook(response.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = Books(name=n)
            t.save()
            response.user.Books.add(t)

        return HttpResponseRedirect("/%i" %t.id)    
    else:    
        form = AddNewBook()
        
    return render(response, "main/create.html", {"form":form})    

def view(response):
    return render(response, "main/view.html", {})

  

def studentclick_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'templates/main/studentclick.html')

def afterlogin_view(request):
    if is_admin(request.user):
        return render(request,'templates/adminafterlogin.html')
    else:
        return render(request,'templates/studentafterlogin.html')
        



