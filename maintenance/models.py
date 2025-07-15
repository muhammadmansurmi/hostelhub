from django.db import models

class MaintenanceRequest(models.Model):
    room_number = models.CharField(max_length=10)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Room {self.room_number} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
