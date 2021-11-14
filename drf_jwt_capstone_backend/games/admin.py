from django.contrib import admin
from .models import Game
from .models import Comment
from .models import ShoppingCart
from .models import Users
from .models import Roles


# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(ShoppingCart)
admin.site.register(Users)
admin.site.register(Roles)

