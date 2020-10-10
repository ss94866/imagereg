from django.shortcuts import render
from clarifai.rest import ClarifaiApp


# Create your views here.
def index(request):
       
    if request.method == "POST":
        app = ClarifaiApp(api_key='de3647cf27144dcf80ef4e1a76e382cd')
        model = app.public_models.general_model
        url = request.POST['url']
        response = model.predict_by_url(url)
        print(type(response))
        mylist=response['outputs'][0]['data']['concepts']
        name = []
        for i in mylist:
            name.append(i['name'])

    
        return render(request,'index.html',{
        "response":name,"url":url
    })
    return render(request,"index.html")