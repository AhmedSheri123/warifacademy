import re
from django.shortcuts import render, redirect
from users.forms import usersForm , passwordForm
from users.models import Users, Password
from django.contrib import messages
from .models import Figures, FiguresChoosed, Question, pointsText
# Create your views here.

def index(request):
    form = usersForm
    passForm = passwordForm
    if request.method == "POST":
        form = form(request.POST)
        passForm = passForm(request.POST)
        
        if form.is_valid() and passForm.is_valid():
            password = passForm.cleaned_data["password"]
            passOBJ = Password.objects.filter(password=password)
            if passOBJ.exists():
                user_id = form.save().pk
                figures = Figures.objects.all()
                request.session["user_id"] = user_id
                return render(request, 'pages/figures.html', {"figures": figures})
            else:
                messages.error(request, "كلمة المرور خاطئة")
            
        else:
            messages.error(request, "هناك خطاء في المدخلات")
    return render(request, "pages/index.html", {"form":form , 'passForm':passForm})

def choose2(request):
    if request.method == "POST":
        figures_id = request.POST.getlist('figure')
        user_id = request.session["user_id"]
        print(user_id)
        user = Users.objects.filter(id=user_id)
        if user.exists():
            if len(figures_id) == 7:
                print(figures_id)
                def getFiguresObj(id):
                    return Figures.objects.get(id=id)
                choosed_add = FiguresChoosed.objects.create(figures_1=getFiguresObj(figures_id[0]), figures_2=getFiguresObj(figures_id[1]), figures_3=getFiguresObj(figures_id[2]), figures_4=getFiguresObj(figures_id[3]), figures_5=getFiguresObj(figures_id[4]), figures_6=getFiguresObj(figures_id[5]), figures_7=getFiguresObj(figures_id[6]), user=Users.objects.get(id=user_id))
                choosed_add.save()
                
                return redirect('questions')
        else:
            return redirect('index')
        figures = Figures.objects.filter(id__in=figures_id)

        return render(request, 'pages/choose2.html',{'user_id': user_id, "figures": figures})
    
    
def question(request):
    user_id = request.session["user_id"]
    user = Users.objects.get(id=user_id)
    figuresChoosed = FiguresChoosed.objects.filter(user=user)[0]
    questions = Question.objects.all()
    values = {}
    values["questions"] = questions
    
    if request.method == "POST":
        points = 0
        print(questions)
        figure_value = request.POST['figure_value']
        for ques in questions:
           questionPoint = request.POST[str(ques.id)]
           points += int(questionPoint)
           user.save()
           
           
        if figure_value == '1':
            figuresChoosed.is_finshed_1 = True
            figuresChoosed.figures_1_points = points
            
        if figure_value == '2':
            figuresChoosed.is_finshed_2 = True
            figuresChoosed.figures_2_points = points
            
        if figure_value == '3':
            figuresChoosed.is_finshed_3 = True
            figuresChoosed.figures_3_points = points
            
        if figure_value == '4':
            figuresChoosed.is_finshed_4 = True
            figuresChoosed.figures_4_points = points
            
        if figure_value == '5':
            figuresChoosed.is_finshed_5 = True
            figuresChoosed.figures_5_points = points
            
        if figure_value == '6':
            figuresChoosed.is_finshed_6 = True
            figuresChoosed.figures_6_points = points
            
        if figure_value == '7':
            figuresChoosed.is_finshed_7 = True
            figuresChoosed.figures_7_points = points
            
        figuresChoosed.save()
        return redirect("questions")

    if not figuresChoosed.is_finshed_1:
        values['figure_value'] = 1
        values['figure'] = figuresChoosed.figures_1
        
        
    elif not figuresChoosed.is_finshed_2:
        values['figure_value'] = 2
        values['figure'] = figuresChoosed.figures_2
        
    elif not figuresChoosed.is_finshed_3:
        values['figure_value'] = 3
        values['figure'] = figuresChoosed.figures_3
        
    elif not figuresChoosed.is_finshed_4:
        values['figure_value'] = 4
        values['figure'] = figuresChoosed.figures_4

    elif not figuresChoosed.is_finshed_5:
        values['figure_value'] = 5
        values['figure'] = figuresChoosed.figures_5
        
    elif not figuresChoosed.is_finshed_6:
        values['figure_value'] = 6
        values['figure'] = figuresChoosed.figures_6
        
    elif not figuresChoosed.is_finshed_7:
        values['figure_value'] = 7
        values['figure'] = figuresChoosed.figures_7
    else:
        return redirect('viewPoints')
    
    return render(request, 'pages/questions.html', values)


def viewPoints(request):
    user_id = request.session["user_id"]
    user = Users.objects.filter(id=user_id)

    if user.exists():
        figuresChoosed = FiguresChoosed.objects.filter(user=user[0])
        if figuresChoosed.exists():
            figuresChoosed = figuresChoosed[0]
            if figuresChoosed.is_finshed_1 and figuresChoosed.is_finshed_2 and figuresChoosed.is_finshed_3 and figuresChoosed.is_finshed_4 and figuresChoosed.is_finshed_5 and figuresChoosed.is_finshed_6 and figuresChoosed.is_finshed_7:
                
                valuse = {
                    "figure":figuresChoosed,
                    "figures_1_points" : "غير معروف",
                    "figures_2_points" : "غير معروف",
                    "figures_3_points" : "غير معروف",
                    "figures_4_points" : "غير معروف",
                    "figures_5_points" : "غير معروف",
                    "figures_6_points" : "غير معروف",
                    "figures_7_points" : "غير معروف",
                          }
                
                pointsTextOBJs = pointsText.objects.all()
                
                for pointsTextOBJ in pointsTextOBJs:
                    pointsRange = []
                    
                    for num in range(pointsTextOBJ._from, pointsTextOBJ._to + 1):
                        pointsRange.append(num)
                        
                    if figuresChoosed.figures_1_points in pointsRange:
                        valuse["figures_1_points"] = pointsTextOBJ.text
                    
                    if figuresChoosed.figures_2_points in pointsRange:
                        valuse["figures_2_points"] = pointsTextOBJ.text
                    
                    if figuresChoosed.figures_3_points in pointsRange:
                        valuse["figures_3_points"] = pointsTextOBJ.text
                    
                    if figuresChoosed.figures_4_points in pointsRange:
                        valuse["figures_4_points"] = pointsTextOBJ.text
                    
                    if figuresChoosed.figures_5_points in pointsRange:
                        valuse["figures_5_points"] = pointsTextOBJ.text
                    
                    if figuresChoosed.figures_6_points in pointsRange:
                        valuse["figures_6_points"] = pointsTextOBJ.text
                    
                    if figuresChoosed.figures_7_points in pointsRange:
                        valuse["figures_7_points"] = pointsTextOBJ.text
                    
                return render(request, "pages/showPoint.html", valuse)

            else:
                return redirect("questions")
        else:
            return redirect("index")
    else:
        return redirect("index")
    



#XnhPW95Q