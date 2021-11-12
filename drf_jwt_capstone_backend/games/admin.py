from django.contrib import admin
from .models import Game
from .models import Comment
from .models import Reply

# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(Reply)
