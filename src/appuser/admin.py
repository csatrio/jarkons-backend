from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import UserChangeForm as BaseUserChangeForm, UserCreationForm as BaseUserCreationForm, \
    ReadOnlyPasswordHashField

from django import forms
from .models import User
from user_info.models import UserInfo
from django.utils.translation import gettext_lazy as _

_labels = {
    'user_permissions': _('Hak Akses'),
    'last_login': _('Login Terakhir'),
    'date_joined': _('Tanggal Gabung'),
    'first_name': _('Nama Depan'),
    'last_name': _('Nama Belakang'),
    'email': _('Email'),
    'is_staff': _('Staff'),
    'is_superuser': _('Superuser'),
    'is_verified': _('Sudah verifikasi'),
}

_help_texts = {
    'username': _('Wajib. 150 karakter atau kurang. Huruf, angka dan @/./+/-/_ saja.'),
    'is_active': _('Apakah user ini aktif?'),
    'is_staff': _('Apakah user ini staff?'),
    'is_superuser': _('Apakah user ini superuser?'),
    'groups': _(
        'Grup tempat pengguna ini. Seorang pengguna akan mendapatkan semua izin yang diberikan untuk masing-masing grup pengguna.'),
    'user_permissions': _('Hak akses / ijin yang diberikan kepada pengguna.'),
}

_error_messages = {
    'username': {
        'max_length': _("This writer's name is too long."),
    },
}


class UserCreationForm(BaseUserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        help_texts = _help_texts
        labels = _labels
        error_messages = _error_messages


class UserChangeForm(BaseUserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')
        help_texts = _help_texts
        labels = _labels
        error_messages = _error_messages

    password = ReadOnlyPasswordHashField(
        label=_("Password"),
        help_text=_(
            "Kata sandi mentah tidak disimpan, jadi tidak ada cara untuk melihat kata sandi pengguna ini, "
            "tetapi Anda dapat mengubah kata sandi menggunakan: "
            "<a href=\"{}\">formulir ini</a>."
        ),
    )


class UserInfoForm(forms.ModelForm):
    model = UserInfo


# Define a new User admin
class UserInfoInline(admin.StackedInline):
    model = UserInfo
    extra = 0


class UserInfoAdmin(admin.ModelAdmin):
    form = UserInfoForm


class UserAdmin(BaseUserAdmin):

    def __init__(self, model, admin_site):
        super(UserAdmin, self).__init__(model, admin_site)
        model.email.verbose_name = 'Email'

    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    inlines = [UserInfoInline, ]
    list_display = ['username', 'email', 'is_verified']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Informasi Pribadi'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Hak Akses'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                     'groups', 'user_permissions')}),
        (_('Tanggal Penting'), {'fields': ('last_login', 'date_joined')}),
        ('Membership Dan Verifikasi', {'fields': ('is_verified',)}),
    )
    pass


# register UserAdmin
admin.site.register(User, UserAdmin)