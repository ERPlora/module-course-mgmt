"""
Course & Class Management Module Views
"""
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from apps.accounts.decorators import login_required
from apps.core.htmx import htmx_view
from apps.modules_runtime.navigation import with_module_nav


@login_required
@with_module_nav('course_mgmt', 'dashboard')
@htmx_view('course_mgmt/pages/dashboard.html', 'course_mgmt/partials/dashboard_content.html')
def dashboard(request):
    """Dashboard view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('course_mgmt', 'courses')
@htmx_view('course_mgmt/pages/courses.html', 'course_mgmt/partials/courses_content.html')
def courses(request):
    """Courses view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('course_mgmt', 'classes')
@htmx_view('course_mgmt/pages/classes.html', 'course_mgmt/partials/classes_content.html')
def classes(request):
    """Classes view."""
    hub_id = request.session.get('hub_id')
    return {}


@login_required
@with_module_nav('course_mgmt', 'settings')
@htmx_view('course_mgmt/pages/settings.html', 'course_mgmt/partials/settings_content.html')
def settings(request):
    """Settings view."""
    hub_id = request.session.get('hub_id')
    return {}

