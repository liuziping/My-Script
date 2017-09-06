from django.contrib import admin

from .models import *

class QuestionAdmin(admin.ModelAdmin):
      search_fields = ('question_text',)
      list_display = ('question_text', 'pub_date')
      list_filter = ['pub_date','question_text']
admin.site.register(Question,QuestionAdmin)

