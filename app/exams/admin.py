from django.contrib import admin

from .models import Exam, Room, Registration


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    pass


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    pass


class RegistrationInline(admin.TabularInline):
    model = Registration
    extra = 1


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    inlines = [RegistrationInline]
