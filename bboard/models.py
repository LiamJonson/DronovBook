from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50)  # допустимая 50 симвл
    content = models.TextField(null=True, blank=True)  # можно не заполнять,неогран.длинны
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now_add=True, db_index=True) # текущ.дат.и врем. и идекс
