from django.db import models


class Bb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Товар')  # допустимая 50 симвл
    content = models.TextField(null=True, blank=True, verbose_name='Описание')  # можно не заполнять,неогран.длинны
    price = models.FloatField(null=True, blank=True, verbose_name='Цена')
    published = models.DateTimeField(auto_now_add=True, db_index=True,
                                     verbose_name='Опубликовано')  # текущ.дат.и врем. и идекс
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
                               verbose_name='Рубрика')  # поле внешн.ключа->передать конструтор первичный класс

    class Meta:
        verbose_name_plural = 'Обьявления'  # множ.числ
        verbose_name = 'Обьявление'  # ед.ч
        ordering = ['-published']  # сортировка


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
