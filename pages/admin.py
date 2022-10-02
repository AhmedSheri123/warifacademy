from django.contrib import admin
from .models import Figures, Question, FiguresChoosed, pointsText, FiguresInfo
# Register your models here.

admin.site.register(Figures)
admin.site.register(Question)
admin.site.register(FiguresChoosed)
admin.site.register(pointsText)
admin.site.register(FiguresInfo)