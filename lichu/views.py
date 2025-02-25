from django.shortcuts import render
from django.templatetags.static import static

def lichu_list(request):
    lichus = [
        {"name": "বোম্বাই লিচু", "description": "বড় আকারের মিষ্টি লিচু।", "image": 'bombay_lichu.jpeg'},
        {"name": "চায়না-৩ লিচু", "description": "গোলাপি রঙের সুস্বাদু লিচু।", "image": "china3_lichu.jpeg"},
        {"name": "মাদ্রাজি লিচু", "description": "খুবই রসালো এবং জনপ্রিয়।", "image": "madrazi_lichu.jpeg"},
    ]
    return render(request, 'lichu/index.html', {"lichus": lichus})
