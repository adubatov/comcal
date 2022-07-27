from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    fieldsets = (
        ('Персональные данные', {
            "fields": ('first_name', 'last_name', 'email',)
            }
        ),
        ('Данные Битрикс', {
            "fields": ('bitrix_user_id',)
            }
        )
    )

admin.site.register(CustomUser, CustomUserAdmin)
