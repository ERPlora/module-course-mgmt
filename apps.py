from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CourseMgmtConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'course_mgmt'
    label = 'course_mgmt'
    verbose_name = _('Course & Class Management')

    def ready(self):
        pass
