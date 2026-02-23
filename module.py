from django.utils.translation import gettext_lazy as _

MODULE_ID = 'course_mgmt'
MODULE_NAME = _('Course & Class Management')
MODULE_VERSION = '1.0.0'
MODULE_ICON = 'book-outline'
MODULE_DESCRIPTION = _('Course catalog, class scheduling and instructor management')
MODULE_AUTHOR = 'ERPlora'
MODULE_CATEGORY = 'specialized'

MENU = {
    'label': _('Course & Class Management'),
    'icon': 'book-outline',
    'order': 93,
}

NAVIGATION = [
    {'label': _('Dashboard'), 'icon': 'speedometer-outline', 'id': 'dashboard'},
{'label': _('Courses'), 'icon': 'book-outline', 'id': 'courses'},
{'label': _('Classes'), 'icon': 'calendar-outline', 'id': 'classes'},
{'label': _('Settings'), 'icon': 'settings-outline', 'id': 'settings'},
]

DEPENDENCIES = []

PERMISSIONS = [
    'course_mgmt.view_course',
'course_mgmt.add_course',
'course_mgmt.change_course',
'course_mgmt.delete_course',
'course_mgmt.view_classsession',
'course_mgmt.add_classsession',
'course_mgmt.change_classsession',
'course_mgmt.manage_settings',
]
