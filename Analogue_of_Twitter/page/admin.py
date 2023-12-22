from django.contrib import admin


from .models import Tag, Page, Subscription, BlockedPage, Request

admin.site.register(Tag),
admin.site.register(Page),
admin.site.register(Subscription),
admin.site.register(BlockedPage),
admin.site.register(Request)
