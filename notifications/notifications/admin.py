from django.contrib import admin
from .models import Notification

# Customize the admin interface for the Notification model
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'notification_type', 'status', 'timestamp')
    list_filter = ('status', 'notification_type')
    search_fields = ('user__username', 'message')
    ordering = ('-timestamp',)
