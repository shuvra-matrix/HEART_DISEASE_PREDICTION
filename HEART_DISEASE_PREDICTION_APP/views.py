import joblib
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create your views here.
def index(request):
    
    return render(request, "index.html")


def heart_disease(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        sex = int(request.POST.get("sex"))
        cp = int(request.POST.get("cp"))
        bp = int(request.POST.get("bp"))
        chol = int(request.POST.get("chol"))
        fbs = int(request.POST.get("fbs"))
        rer = int(request.POST.get("rer"))
        heart_rate = int(request.POST.get("heart_rate"))
        agina = int(request.POST.get("agina"))
        oldpeak = float(request.POST.get("oldpeak"))
        slope = int(request.POST.get("slope"))
        ca = float(request.POST.get("ca"))
        thal = int(request.POST.get("thal"))
        request.session['list'] = []
        list = request.session.get("list")
        list.append(age)
        list.append(sex)
        list.append(cp)
        list.append(bp)
        list.append(chol)
        if fbs > 120 :
            list.append(1)
        else:
            list.append(0)
        list.append(rer)
        list.append(heart_rate)
        list.append(agina)
        list.append(oldpeak)
        list.append(slope)
        list.append(ca)
        list.append(thal)
        project = joblib.load("heart_model.sav")
        ans = project.predict([list])
        if ans == 1 :
            message = "Report Positive"
        elif ans == 0 :
            message = "Report Negative"
        my_dict ={
            "message" : message,
        }
        del request.session['list']
        return render(request, "heart_desease_prediction.html",context=my_dict)
    
    return render(request, "heart_desease_prediction.html")
