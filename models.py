from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.models.base import HubBaseModel

class Course(HubBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('Name'))
    code = models.CharField(max_length=20, blank=True, verbose_name=_('Code'))
    description = models.TextField(blank=True, verbose_name=_('Description'))
    duration_hours = models.PositiveIntegerField(default=0, verbose_name=_('Duration Hours'))
    price = models.DecimalField(max_digits=10, decimal_places=2, default='0', verbose_name=_('Price'))
    max_students = models.PositiveIntegerField(default=20, verbose_name=_('Max Students'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active'))

    class Meta(HubBaseModel.Meta):
        db_table = 'course_mgmt_course'

    def __str__(self):
        return self.name


class ClassSession(HubBaseModel):
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=255, blank=True, verbose_name=_('Title'))
    instructor_id = models.UUIDField(null=True, blank=True, verbose_name=_('Instructor Id'))
    instructor_name = models.CharField(max_length=255, blank=True, verbose_name=_('Instructor Name'))
    start_time = models.DateTimeField(verbose_name=_('Start Time'))
    end_time = models.DateTimeField(verbose_name=_('End Time'))
    location = models.CharField(max_length=255, blank=True, verbose_name=_('Location'))
    enrolled_count = models.PositiveIntegerField(default=0, verbose_name=_('Enrolled Count'))

    class Meta(HubBaseModel.Meta):
        db_table = 'course_mgmt_classsession'

    def __str__(self):
        return self.title

