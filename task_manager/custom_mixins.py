from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

user_anonymous_message = _("You are not logged in! Please log in.")


class CustomLoginRequiredMixin(LoginRequiredMixin):
    """Extends LoginRequiredMixin to
    provide user feedback when login is required.
    
    This mixin enhances the default behavior by showing
    an error message when an anonymous user tries to access
    a protected view before redirecting to the login page.
    
    Attributes:
        Inherits all attributes from LoginRequiredMixin.
    """
    def handle_no_permission(self):
        messages.error(self.request, user_anonymous_message)
        return redirect(reverse_lazy("login"))


class CustomUserPassesTestMixin(UserPassesTestMixin):
    """Extended UserPassesTestMixin with 
    customizable permission messages.
    
    Provides different feedback for anonymous users and
    authenticated users who fail permission checks.
    
    Attributes:
        error_anonymous_message (str): Message for anonymous users
            (default: login message).
        error_permission_message (str): Message for failed permission checks.
        error_redirect (str): URL name to redirect failed permission checks
            (default: "home").
    """
    error_anonymous_message = user_anonymous_message
    error_permission_message = ''
    error_redirect = reverse_lazy("home")

    def handle_no_permission(self):
        if self.request.user.is_anonymous:
            messages.error(
                self.request, self.error_anonymous_message
            )
            return redirect(reverse_lazy("login"))
        messages.error(
            self.request, self.error_permission_message
        )
        return redirect(self.error_redirect)


class PlaceholderMixin:
    '''
    Automatically adds placeholder attributes 
    to form fields matching their labels.

    When applied to a form class, this mixin will
    set the placeholder attribute of each field's widget
    to match the field's label during form initialization.
    '''
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if hasattr(field.widget, 'attrs'):
                field.widget.attrs.update({'placeholder': field.label})