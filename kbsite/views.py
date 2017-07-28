from django.shortcuts import render
from forms import KillForm
from models import Kill_PureText

# Create your views here.


def home(request, pagenum=0):
    pagenum = int(pagenum)
    step = 10
    total = Kill_PureText.objects.all().count()
    lower = min(pagenum*step, total)
    upper = min((pagenum+1)*step, total)
    kills = Kill_PureText.objects.all()[lower:upper]
    return render(request, "main.html", {"kills": kills, "page":pagenum})


def postkill(request):
    form = KillForm()
    if request.method == "GET":
        return render(request, "killform.html", {"formset": form})
    elif request.method == 'POST':
        form = KillForm(request.POST)
        form.save()
        return render(request, "killform.html", {"formset": form, "success": True})
    return render(request, "killform.html", {"formset": form, "success": False})
