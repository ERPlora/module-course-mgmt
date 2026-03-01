"""AI tools for the Course Management module."""
from assistant.tools import AssistantTool, register_tool


@register_tool
class ListCourses(AssistantTool):
    name = "list_courses"
    description = "List courses."
    module_id = "course_mgmt"
    required_permission = "course_mgmt.view_course"
    parameters = {"type": "object", "properties": {"is_active": {"type": "boolean"}}, "required": [], "additionalProperties": False}

    def execute(self, args, request):
        from course_mgmt.models import Course
        qs = Course.objects.all()
        if 'is_active' in args:
            qs = qs.filter(is_active=args['is_active'])
        return {"courses": [{"id": str(c.id), "name": c.name, "code": c.code, "duration_hours": c.duration_hours, "price": str(c.price), "max_students": c.max_students, "is_active": c.is_active} for c in qs]}


@register_tool
class CreateCourse(AssistantTool):
    name = "create_course"
    description = "Create a course."
    module_id = "course_mgmt"
    required_permission = "course_mgmt.add_course"
    requires_confirmation = True
    parameters = {
        "type": "object",
        "properties": {
            "name": {"type": "string"}, "code": {"type": "string"}, "description": {"type": "string"},
            "duration_hours": {"type": "integer"}, "price": {"type": "string"}, "max_students": {"type": "integer"},
        },
        "required": ["name"],
        "additionalProperties": False,
    }

    def execute(self, args, request):
        from decimal import Decimal
        from course_mgmt.models import Course
        c = Course.objects.create(name=args['name'], code=args.get('code', ''), description=args.get('description', ''), duration_hours=args.get('duration_hours', 0), price=Decimal(args['price']) if args.get('price') else None, max_students=args.get('max_students', 0))
        return {"id": str(c.id), "name": c.name, "created": True}
