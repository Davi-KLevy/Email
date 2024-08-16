from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')  # Removendo 'is_staff' e 'is_superuser'
    search_fields = ('email',)
    list_filter = ('is_active',)  # Removendo 'is_staff' e 'is_superuser'

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    ordering = ('email',)

admin.site.register(User, UserAdmin)
