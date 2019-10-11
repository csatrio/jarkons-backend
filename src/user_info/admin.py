from django.contrib import admin
from django import forms
from user_info.models import Profesi, Klasifikasi, Kualifikasi, Keahlian


class ProfesiForm(forms.ModelForm):
    model = Profesi


class KualifikasiInline(admin.StackedInline):
    model = Kualifikasi
    extra = 0


class KlasifikasiInline(admin.StackedInline):
    model = Klasifikasi
    extra = 0


class KeahlianInline(admin.StackedInline):
    model = Keahlian
    extra = 0


class ProfesiAdmin(admin.ModelAdmin):
    form = ProfesiForm
    inlines = [KualifikasiInline, KlasifikasiInline, KeahlianInline]


admin.site.register(Profesi, ProfesiAdmin)
