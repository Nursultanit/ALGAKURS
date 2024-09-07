from modeltranslation.translator import register, TranslationOptions
from .models import ALGA_Department, Professor, Course

@register(ALGA_Department)
class ALGA_DepartmentTranslationOptions(TranslationOptions):
    fields = ('name', 'description')  

@register(Professor)
class ProfessorTranslationOptions(TranslationOptions):
    fields = ('title', 'bio')

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
