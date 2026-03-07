"""
Course & Class Management Module Views
"""
from django.core.paginator import Paginator
from django.db.models import Q, Count
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import get_object_or_404, render as django_render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.views.decorators.http import require_POST

from apps.accounts.decorators import login_required, permission_required
from apps.core.htmx import htmx_view
from apps.core.services import export_to_csv, export_to_excel
from apps.modules_runtime.navigation import with_module_nav

from .models import Course, ClassSession

PER_PAGE_CHOICES = [10, 25, 50, 100]


# ======================================================================
# Dashboard
# ======================================================================

@login_required
@with_module_nav('course_mgmt', 'dashboard')
@htmx_view('course_mgmt/pages/index.html', 'course_mgmt/partials/dashboard_content.html')
def dashboard(request):
    hub_id = request.session.get('hub_id')
    return {
        'total_courses': Course.objects.filter(hub_id=hub_id, is_deleted=False).count(),
    }


# ======================================================================
# Course
# ======================================================================

COURSE_SORT_FIELDS = {
    'code': 'code',
    'name': 'name',
    'is_active': 'is_active',
    'max_students': 'max_students',
    'price': 'price',
    'duration_hours': 'duration_hours',
    'created_at': 'created_at',
}

def _build_courses_context(hub_id, per_page=10):
    qs = Course.objects.filter(hub_id=hub_id, is_deleted=False).order_by('code')
    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(1)
    return {
        'courses': page_obj,
        'page_obj': page_obj,
        'search_query': '',
        'sort_field': 'code',
        'sort_dir': 'asc',
        'current_view': 'table',
        'per_page': per_page,
    }

def _render_courses_list(request, hub_id, per_page=10):
    ctx = _build_courses_context(hub_id, per_page)
    return django_render(request, 'course_mgmt/partials/courses_list.html', ctx)

@login_required
@with_module_nav('course_mgmt', 'courses')
@htmx_view('course_mgmt/pages/courses.html', 'course_mgmt/partials/courses_content.html')
def courses_list(request):
    hub_id = request.session.get('hub_id')
    search_query = request.GET.get('q', '').strip()
    sort_field = request.GET.get('sort', 'code')
    sort_dir = request.GET.get('dir', 'asc')
    page_number = request.GET.get('page', 1)
    current_view = request.GET.get('view', 'table')
    per_page = int(request.GET.get('per_page', 10))
    if per_page not in PER_PAGE_CHOICES:
        per_page = 10

    qs = Course.objects.filter(hub_id=hub_id, is_deleted=False)

    if search_query:
        qs = qs.filter(Q(name__icontains=search_query) | Q(code__icontains=search_query) | Q(description__icontains=search_query))

    order_by = COURSE_SORT_FIELDS.get(sort_field, 'code')
    if sort_dir == 'desc':
        order_by = f'-{order_by}'
    qs = qs.order_by(order_by)

    export_format = request.GET.get('export')
    if export_format in ('csv', 'excel'):
        fields = ['code', 'name', 'is_active', 'max_students', 'price', 'duration_hours']
        headers = ['Code', 'Name', 'Is Active', 'Max Students', 'Price', 'Duration Hours']
        if export_format == 'csv':
            return export_to_csv(qs, fields=fields, headers=headers, filename='courses.csv')
        return export_to_excel(qs, fields=fields, headers=headers, filename='courses.xlsx')

    paginator = Paginator(qs, per_page)
    page_obj = paginator.get_page(page_number)

    if request.htmx and request.htmx.target == 'datatable-body':
        return django_render(request, 'course_mgmt/partials/courses_list.html', {
            'courses': page_obj, 'page_obj': page_obj,
            'search_query': search_query, 'sort_field': sort_field,
            'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
        })

    return {
        'courses': page_obj, 'page_obj': page_obj,
        'search_query': search_query, 'sort_field': sort_field,
        'sort_dir': sort_dir, 'current_view': current_view, 'per_page': per_page,
    }

@login_required
@htmx_view('course_mgmt/pages/course_add.html', 'course_mgmt/partials/course_add_content.html')
def course_add(request):
    hub_id = request.session.get('hub_id')
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        code = request.POST.get('code', '').strip()
        description = request.POST.get('description', '').strip()
        duration_hours = int(request.POST.get('duration_hours', 0) or 0)
        price = request.POST.get('price', '0') or '0'
        max_students = int(request.POST.get('max_students', 0) or 0)
        is_active = request.POST.get('is_active') == 'on'
        obj = Course(hub_id=hub_id)
        obj.name = name
        obj.code = code
        obj.description = description
        obj.duration_hours = duration_hours
        obj.price = price
        obj.max_students = max_students
        obj.is_active = is_active
        obj.save()
        response = HttpResponse(status=204)
        response['HX-Redirect'] = reverse('course_mgmt:courses_list')
        return response
    return {}

@login_required
@htmx_view('course_mgmt/pages/course_edit.html', 'course_mgmt/partials/course_edit_content.html')
def course_edit(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Course, pk=pk, hub_id=hub_id, is_deleted=False)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '').strip()
        obj.code = request.POST.get('code', '').strip()
        obj.description = request.POST.get('description', '').strip()
        obj.duration_hours = int(request.POST.get('duration_hours', 0) or 0)
        obj.price = request.POST.get('price', '0') or '0'
        obj.max_students = int(request.POST.get('max_students', 0) or 0)
        obj.is_active = request.POST.get('is_active') == 'on'
        obj.save()
        return _render_courses_list(request, hub_id)
    return {'obj': obj}

@login_required
@require_POST
def course_delete(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Course, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_deleted = True
    obj.deleted_at = timezone.now()
    obj.save(update_fields=['is_deleted', 'deleted_at', 'updated_at'])
    return _render_courses_list(request, hub_id)

@login_required
@require_POST
def course_toggle_status(request, pk):
    hub_id = request.session.get('hub_id')
    obj = get_object_or_404(Course, pk=pk, hub_id=hub_id, is_deleted=False)
    obj.is_active = not obj.is_active
    obj.save(update_fields=['is_active', 'updated_at'])
    return _render_courses_list(request, hub_id)

@login_required
@require_POST
def courses_bulk_action(request):
    hub_id = request.session.get('hub_id')
    ids = [i.strip() for i in request.POST.get('ids', '').split(',') if i.strip()]
    action = request.POST.get('action', '')
    qs = Course.objects.filter(hub_id=hub_id, is_deleted=False, id__in=ids)
    if action == 'activate':
        qs.update(is_active=True)
    elif action == 'deactivate':
        qs.update(is_active=False)
    elif action == 'delete':
        qs.update(is_deleted=True, deleted_at=timezone.now())
    return _render_courses_list(request, hub_id)


@login_required
@permission_required('course_mgmt.manage_settings')
@with_module_nav('course_mgmt', 'settings')
@htmx_view('course_mgmt/pages/settings.html', 'course_mgmt/partials/settings_content.html')
def settings_view(request):
    return {}

