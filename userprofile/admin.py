from django.contrib import admin

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import UserProfile, Review


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin configuration for UserProfile model.
    """
    list_display = ('company_name', 'user_contact_number')
    search_fields = ['company_name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    """
    Admin configuration for Review model.
    """
    list_display = ('comment', 'stars')
    search_fields = ['profile_reviewed', 'reviewed_from']


class UserProfileInline(admin.StackedInline):
    """
    Inline admin configuration for UserProfile model.
    """
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'company_name'


class UserAdmin(BaseUserAdmin):
    """
    Admin configuration for the User model with UserProfile inline.
    """
    inlines = (UserProfileInline, )


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
