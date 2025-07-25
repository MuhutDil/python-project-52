import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from task_manager.labels.models import Label
from task_manager.statuses.models import Status
from task_manager.users.models import CustomUser

from .models import Task


class TaskFilter(django_filters.FilterSet):
    status = django_filters.ModelChoiceFilter(queryset=Status.objects.all())
    executor = django_filters.ModelChoiceFilter(
        queryset=CustomUser.objects.all()
    )
    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(), 
        label=_("Label"),
    )
    author = django_filters.BooleanFilter(
        widget=forms.CheckboxInput,
        method="check_author",
        label=_("Only your tasks"),
    )

    class Meta:
        model = Task
        fields = ["status", "executor", "labels"]

    def check_author(self, queryset, _, check):
        if check:
            user = self.request.user
            return queryset.filter(author=user)
        return queryset