from django.contrib import admin
from .models import Game
from .models import Comment
from .models import ShoppingCart
from .models import User
from .models import Role


# Register your models here.
admin.site.register(Game)
admin.site.register(Comment)
admin.site.register(ShoppingCart)
admin.site.register(User)
admin.site.register(Role)

