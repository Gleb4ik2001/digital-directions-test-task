from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import logging

# переменная для инициализации функции логирования
logger = logging.getLogger(__name__)

STATUS_CHOICES = (
    ('new', 'New'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
)

class Task(models.Model):
    user = models.ForeignKey(
        verbose_name='пользователь',
        to=User,
        on_delete=models.CASCADE,
        related_name='tasks'
    )
    title = models.CharField(
        verbose_name='название',
        max_length=255
    )
    description = models.TextField(
        verbose_name='описание задачи',
        blank=True
    )
    status = models.CharField(
        verbose_name='статус',
        max_length=20, 
        choices=STATUS_CHOICES, 
        default='new'
    )
    due_date = models.DateTimeField(
        verbose_name='срок задачи',
        blank=True,
        null=True
    )
    tags = models.JSONField(
        verbose_name='теги',
        blank=True, 
        null=True
    )
    datetime_created = models.DateTimeField(
        verbose_name='дата создания задачи',
        auto_now=True,
        null=True,
        blank=True
    )
    datetime_updated = models.DateTimeField(
        verbose_name='дата обновления задачи',
        auto_now_add=True,
        blank=True,
        null=True
    )

    @property
    def is_overdue(self):
        now = timezone.now()
        if self.status != 'done' and self.due_date < now:
            logger.warning(f'⚠️ Задача "{self.title}" (ID: {self.id}) просрочена!')
            return True
        return False

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
        ordering = ('id',)
