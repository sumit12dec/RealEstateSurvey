from django.contrib import admin

# Register your models here.

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
	list_display = Question._meta.get_all_field_names()
	class Meta:
		model = Question

admin.site.register(Question, QuestionAdmin)
