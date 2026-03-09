# Course & Class Management

## Overview

| Property | Value |
|----------|-------|
| **Module ID** | `course_mgmt` |
| **Version** | `1.0.0` |
| **Icon** | `book-outline` |
| **Dependencies** | None |

## Models

### `Course`

Course(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, name, code, description, duration_hours, price, max_students, is_active)

| Field | Type | Details |
|-------|------|---------|
| `name` | CharField | max_length=255 |
| `code` | CharField | max_length=20, optional |
| `description` | TextField | optional |
| `duration_hours` | PositiveIntegerField |  |
| `price` | DecimalField |  |
| `max_students` | PositiveIntegerField |  |
| `is_active` | BooleanField |  |

### `ClassSession`

ClassSession(id, hub_id, created_at, updated_at, created_by, updated_by, is_deleted, deleted_at, course, title, instructor_id, instructor_name, start_time, end_time, location, enrolled_count)

| Field | Type | Details |
|-------|------|---------|
| `course` | ForeignKey | → `course_mgmt.Course`, on_delete=CASCADE |
| `title` | CharField | max_length=255, optional |
| `instructor_id` | UUIDField | max_length=32, optional |
| `instructor_name` | CharField | max_length=255, optional |
| `start_time` | DateTimeField |  |
| `end_time` | DateTimeField |  |
| `location` | CharField | max_length=255, optional |
| `enrolled_count` | PositiveIntegerField |  |

## Cross-Module Relationships

| From | Field | To | on_delete | Nullable |
|------|-------|----|-----------|----------|
| `ClassSession` | `course` | `course_mgmt.Course` | CASCADE | No |

## URL Endpoints

Base path: `/m/course_mgmt/`

| Path | Name | Method |
|------|------|--------|
| `(root)` | `dashboard` | GET |
| `classes/` | `classes` | GET |
| `courses/` | `courses_list` | GET |
| `courses/add/` | `course_add` | GET/POST |
| `courses/<uuid:pk>/edit/` | `course_edit` | GET |
| `courses/<uuid:pk>/delete/` | `course_delete` | GET/POST |
| `courses/<uuid:pk>/toggle/` | `course_toggle_status` | GET |
| `courses/bulk/` | `courses_bulk_action` | GET/POST |
| `settings/` | `settings` | GET |

## Permissions

| Permission | Description |
|------------|-------------|
| `course_mgmt.view_course` | View Course |
| `course_mgmt.add_course` | Add Course |
| `course_mgmt.change_course` | Change Course |
| `course_mgmt.delete_course` | Delete Course |
| `course_mgmt.view_classsession` | View Classsession |
| `course_mgmt.add_classsession` | Add Classsession |
| `course_mgmt.change_classsession` | Change Classsession |
| `course_mgmt.manage_settings` | Manage Settings |

**Role assignments:**

- **admin**: All permissions
- **manager**: `add_classsession`, `add_course`, `change_classsession`, `change_course`, `view_classsession`, `view_course`
- **employee**: `add_course`, `view_classsession`, `view_course`

## Navigation

| View | Icon | ID | Fullpage |
|------|------|----|----------|
| Dashboard | `speedometer-outline` | `dashboard` | No |
| Courses | `book-outline` | `courses` | No |
| Classes | `calendar-outline` | `classes` | No |
| Settings | `settings-outline` | `settings` | No |

## AI Tools

Tools available for the AI assistant:

### `list_courses`

List courses.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `is_active` | boolean | No |  |

### `create_course`

Create a course.

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `name` | string | Yes |  |
| `code` | string | No |  |
| `description` | string | No |  |
| `duration_hours` | integer | No |  |
| `price` | string | No |  |
| `max_students` | integer | No |  |

## File Structure

```
README.md
__init__.py
admin.py
ai_tools.py
apps.py
forms.py
locale/
  en/
    LC_MESSAGES/
      django.po
  es/
    LC_MESSAGES/
      django.po
migrations/
  0001_initial.py
  __init__.py
models.py
module.py
static/
  course_mgmt/
    css/
    js/
  icons/
    icon.svg
templates/
  course_mgmt/
    pages/
      classes.html
      course_add.html
      course_edit.html
      courses.html
      dashboard.html
      index.html
      settings.html
    partials/
      classes_content.html
      course_add_content.html
      course_edit_content.html
      courses_content.html
      courses_list.html
      dashboard_content.html
      panel_course_add.html
      panel_course_edit.html
      settings_content.html
tests/
  __init__.py
  conftest.py
  test_models.py
  test_views.py
urls.py
views.py
```
