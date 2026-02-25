# Course & Class Management Module

Course catalog, class scheduling and instructor management.

## Features

- Create and manage a course catalog with codes, descriptions, and pricing
- Define course duration in hours and maximum student capacity
- Schedule class sessions linked to courses with start/end times
- Assign instructors to class sessions
- Specify session locations
- Track enrolled student count per session
- Activate or deactivate courses
- Dashboard overview of courses and upcoming sessions

## Installation

This module is installed automatically via the ERPlora Marketplace.

## Configuration

Access settings via: **Menu > Course & Class Management > Settings**

## Usage

Access via: **Menu > Course & Class Management**

### Views

| View | URL | Description |
|------|-----|-------------|
| Dashboard | `/m/course_mgmt/dashboard/` | Overview of courses and class metrics |
| Courses | `/m/course_mgmt/courses/` | List, create and manage courses |
| Classes | `/m/course_mgmt/classes/` | Schedule and manage class sessions |
| Settings | `/m/course_mgmt/settings/` | Module configuration |

## Models

| Model | Description |
|-------|-------------|
| `Course` | A course with name, code, description, duration (hours), price, max students, and active flag |
| `ClassSession` | A scheduled class session linked to a course, with instructor, start/end times, location, and enrolled count |

## Permissions

| Permission | Description |
|------------|-------------|
| `course_mgmt.view_course` | View courses |
| `course_mgmt.add_course` | Create new courses |
| `course_mgmt.change_course` | Edit existing courses |
| `course_mgmt.delete_course` | Delete courses |
| `course_mgmt.view_classsession` | View class sessions |
| `course_mgmt.add_classsession` | Create new class sessions |
| `course_mgmt.change_classsession` | Edit existing class sessions |
| `course_mgmt.manage_settings` | Manage module settings |

## License

MIT

## Author

ERPlora Team - support@erplora.com
