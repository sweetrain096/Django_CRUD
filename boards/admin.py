from django.contrib import admin
# admin.py에서 Board 클래스를 쓰려면 반드시 import 해야한다.
# 명시적 상대 (.models : 현재디렉토리에 있는 models.py)
from .models import Board
# Register your models here.
class BoardAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at',]
admin.site.register(Board, BoardAdmin)
