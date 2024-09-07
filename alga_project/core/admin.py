from django.contrib import admin
from django.contrib import admin
from .models import ALGA_Department, Professor, Student, Course, Office, Schedule, CourseRegistration
from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

@admin.register(ALGA_Department)
class ALGA_Department(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Course)
class Course(TranslationAdmin):

    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



admin.site.register(Professor)
admin.site.register(Student)

admin.site.register(Office)
admin.site.register(Schedule)
admin.site.register(CourseRegistration)

