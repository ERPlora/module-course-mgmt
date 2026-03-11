"""
AI context for the Course Management module.
Loaded into the assistant system prompt when this module's tools are active.
"""

CONTEXT = """
## Module Knowledge: Course Management

### Models

**Course** — a course or training program offered.
- `name` (str): course title
- `code` (str, max 20): short reference code (e.g. "PY101", "ENG-ADV")
- `description` (text)
- `duration_hours` (int, default 0): total course length in hours
- `price` (Decimal): enrollment price
- `max_students` (int, default 20): capacity cap per session
- `is_active` (bool, default True)

**ClassSession** — a scheduled session of a course.
- `course` (FK → Course): which course this session belongs to
- `title` (str): session title or topic (can be blank for generic sessions)
- `instructor_id` (UUID, nullable): UUID of the instructor (references accounts.LocalUser)
- `instructor_name` (str): name copy for display
- `start_time` (datetime): session start
- `end_time` (datetime): session end
- `location` (str): room, URL, or address
- `enrolled_count` (int, default 0): current enrollment count

### Key flows

1. **Create a course**: provide name, price, duration_hours, max_students.
2. **Schedule a session**: create ClassSession linked to a course with start_time, end_time, location, and instructor info.
3. **Enroll a student**: increment ClassSession.enrolled_count (check enrolled_count < course.max_students first).
4. **List upcoming sessions**: filter ClassSession by start_time__gte=now, ordered by start_time.
5. **Check availability**: compare enrolled_count to course.max_students.

### Relationships
- ClassSession.course → Course
- ClassSession.instructor_id → UUID reference to accounts.LocalUser (no FK)

### Notes
- Student enrollment records are typically stored in the student_mgmt module (Enrollment model), not here.
- enrolled_count is a denormalized counter — update it when enrollments are created/cancelled.
"""
