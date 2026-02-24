"""Tests for course_mgmt models."""
import pytest
from django.utils import timezone

from course_mgmt.models import Course


@pytest.mark.django_db
class TestCourse:
    """Course model tests."""

    def test_create(self, course):
        """Test Course creation."""
        assert course.pk is not None
        assert course.is_deleted is False

    def test_str(self, course):
        """Test string representation."""
        assert str(course) is not None
        assert len(str(course)) > 0

    def test_soft_delete(self, course):
        """Test soft delete."""
        pk = course.pk
        course.is_deleted = True
        course.deleted_at = timezone.now()
        course.save()
        assert not Course.objects.filter(pk=pk).exists()
        assert Course.all_objects.filter(pk=pk).exists()

    def test_queryset_excludes_deleted(self, hub_id, course):
        """Test default queryset excludes deleted."""
        course.is_deleted = True
        course.deleted_at = timezone.now()
        course.save()
        assert Course.objects.filter(hub_id=hub_id).count() == 0

    def test_toggle_active(self, course):
        """Test toggling is_active."""
        original = course.is_active
        course.is_active = not original
        course.save()
        course.refresh_from_db()
        assert course.is_active != original


