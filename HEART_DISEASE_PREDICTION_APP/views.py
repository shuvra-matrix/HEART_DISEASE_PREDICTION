import joblib
from django.shortcuts import render
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Create your views here.
def index(request):
    
    project = joblib.load("heart_model.sav")
    list = [57,0,0,140,241,0,1,123,1,0.2,1,0,3]
    ans = project.predict([list])
    print(ans)
    return render(request, "index.html")