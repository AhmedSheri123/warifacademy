from django.db import models
from users.models import Users
# Create your models here.

class Figures(models.Model):
    text = models.CharField(verbose_name="النص", max_length=250)
    
    def __str__(self):
        return self.text
    
class Question(models.Model):
    text = models.CharField(verbose_name="النص", max_length=250)
    
    def __str__(self):
        return self.text
    
    
class FiguresChoosed(models.Model):
    user = models.ForeignKey(Users, verbose_name="المستحدم", on_delete=models.CASCADE)
    
    figures_1 = models.ForeignKey(Figures, related_name="figures_1", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_1 = models.BooleanField(default=False)
    figures_1_points = models.IntegerField(default=0)
    
    figures_2 = models.ForeignKey(Figures, related_name="figures_2", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_2 = models.BooleanField(default=False)
    figures_2_points = models.IntegerField(default=0)
    
    figures_3 = models.ForeignKey(Figures, related_name="figures_3", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_3 = models.BooleanField(default=False)
    figures_3_points = models.IntegerField(default=0)
    
    figures_4 = models.ForeignKey(Figures, related_name="figures_4", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_4 = models.BooleanField(default=False)
    figures_4_points = models.IntegerField(default=0)
    
    figures_5 = models.ForeignKey(Figures, related_name="figures_5", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_5 = models.BooleanField(default=False)
    figures_5_points = models.IntegerField(default=0)
    
    figures_6 = models.ForeignKey(Figures, related_name="figures_6", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_6 = models.BooleanField(default=False)
    figures_6_points = models.IntegerField(default=0)

    figures_7 = models.ForeignKey(Figures, related_name="figures_7", verbose_name="الشخصية", on_delete=models.CASCADE)
    is_finshed_7 = models.BooleanField(default=False)
    figures_7_points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    
    
class pointsText(models.Model):
    _from = models.IntegerField(default=0, verbose_name="من")
    _to = models.IntegerField(default=0, verbose_name="الى")
    text = models.TextField(verbose_name="النص الذي سوف يعرض للمستخدم")
    
    def __str__(self):
        return "من " + str(self._from) + " الى " + str(self._to)