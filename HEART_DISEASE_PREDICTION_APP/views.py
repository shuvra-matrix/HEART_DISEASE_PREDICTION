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
            message = "Positive"
        elif ans == 0 :
            message = "Negative"
        my_dict ={
            "message" : message,
        }
        del request.session['list']
        return render(request, "heart_desease_prediction.html",context=my_dict)
    
    return render(request, "heart_desease_prediction.html")


def heart_prediction_2(request):
    if request.method == "POST":
        age = int(request.POST.get("age"))
        gender = int(request.POST.get("gender"))
        height = int(request.POST.get("height"))
        weight = int(request.POST.get("weight"))
        bp_hi = int(request.POST.get("bp_hi"))
        bp_lo = int(request.POST.get("bp_lo"))
        cholestrol = int(request.POST.get("cholesterol"))
        gluc = int(request.POST.get("gluc"))
        smoke = int(request.POST.get("smoke"))
        alcohol = int(request.POST.get("alcohol"))
        activity = int(request.POST.get("activity"))
        request.session['list1'] = []
        list1 = request.session.get("list1")
        list1.append(age)
        list1.append(gender)
        list1.append(height)
        list1.append(weight)
        list1.append(bp_hi)
        list1.append(bp_lo)
        list1.append(cholestrol)
        list1.append(gluc)
        list1.append(smoke)
        list1.append(alcohol)
        list1.append(activity)
        project = joblib.load("heart_model_2.sav")
        ans = project.predict([list1])
        if ans == 1:
            message = "Positive"
        elif ans == 0:
            message = "Negative"
        my_dict = {
            "message": message,
        }
        del request.session['list1']
        return render(request, "heart_desease_prediction_2.html",context=my_dict)
        
    return render(request, "heart_desease_prediction_2.html")



def about_heart(request):
    
    return render(request, "about_heart.html")


def about1(request):
    return render(request, "about1.html")


def about2(request):
    return render(request, "about2.html")


def about3(request):
    return render(request, "about3.html")


def ins(request):
    return render(request, "ins.html")


def about4(request):
    return render(request, "about4.html")
