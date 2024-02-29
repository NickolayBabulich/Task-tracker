from django.db import models


class Performer(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    removed_tasks_count = models.PositiveIntegerField(default=0, verbose_name='Количество удаленных задач')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    tasks = models.ManyToManyField('Task', related_name='projects', verbose_name='Задачи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Task(models.Model):
    priority_values = [
        (1, 'Высокий'),
        (2, 'Средний'),
        (3, 'Низкий'),
    ]
    created_date = models.DateTimeField(verbose_name='Дата создания')
    deadline = models.DateTimeField(verbose_name='Дата окончания')
    performer = models.ForeignKey(Performer, on_delete=models.SET_NULL, related_name='tasks', null=True,
                                  verbose_name='Исполнитель')
    priority = models.PositiveSmallIntegerField(choices=priority_values, verbose_name='Приоритет')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    comment = models.TextField(blank=True, verbose_name='Комментарий')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
