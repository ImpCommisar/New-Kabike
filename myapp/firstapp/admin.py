from django.contrib import admin
from .models import TodoItem, subject, IndexCard

class IndexCardInline(admin.TabularInline):
    model = IndexCard

class subjectAdmin(admin.ModelAdmin):
    model = subject

    # Use the subject name and the teacher's name to search through all instances
    search_fields = ('name', 'teacher_name',)
    # Display just the teacher name and the subject name in the list
    list_display = ('name', 'teacher_name',)
    # Enable filtering via the teacher's name and the number of units
    list_filter = ('teacher_name', 'units',)

    inlines = [IndexCardInline,]

    fieldsets = [
        ('Class Data', {
            'fields': [
                ('name', 'units'), 'teacher_name'
            ]
        })
    ]
    
class IndexCardAdmin(admin.ModelAdmin):
    model = IndexCard


# Register your models here.
admin.site.register(subject, subjectAdmin)
admin.site.register(IndexCard, IndexCardAdmin)
admin.site.register(TodoItem)