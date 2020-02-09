from django.contrib import admin
from .models import Post, Event, Member, Value

# Models are registered here
admin.site.register(Post)
admin.site.register(Event)
admin.site.register(Member)
admin.site.register(Value)