from io import BytesIO

import qrcode
from django.core.files import File
from django.db import models

# Create your models here.
# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_start_date = models.DateField()
    event_end_date = models.DateField()
    event_start_time = models.TimeField()
    event_end_time = models.TimeField()
    event_location = models.CharField(max_length=255)

    def __str__(self):
        return self.event_name


class Registration(models.Model):
    class TshirtSize(models.TextChoices):
        S = "S", "Small"
        M = "M", "Medium"
        L = "L", "Large"
        XL = "XL", "Extra Large"
        XXL = "XXL", "Extra Extra Large"

    id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    batch_year = models.IntegerField(null=True, blank=True)
    mobile_no = models.CharField(max_length=15, null=True, blank=True)
    tshirt_size = models.CharField(max_length=3, null=True, choices=TshirtSize.choices)
    # events = models.ManyToManyField(Event, blank=True)  # Adding the ManyToManyField

    registration = models.BooleanField(default=False, null=True, blank=True)
    kit = models.BooleanField(default=False)
    tshirt = models.BooleanField(default=False)
    cap = models.BooleanField(default=False)
    lapel_pin = models.BooleanField(default=False)
    barcode = models.ImageField(upload_to="images", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def _str_(self):
        return self.name

    def save(self, *args, **kwargs):
        if self._state.adding is True:
            code = qrcode.make(str(self.pk))
            blob = BytesIO()
            code.save(blob, format="PNG")
            blob.seek(0)
            self.barcode.save(f"{self.pk}.png", File(blob), save=False)

        return super().save(*args, **kwargs)


class EventRegistration(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
    )
    registration = models.ForeignKey(
        Registration, on_delete=models.CASCADE, related_name="events"
    )
    present = models.BooleanField(default=False)
    can_attend_multiple = models.BooleanField(default=False)
    attend_event_count = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.event}-{self.registration}"

    class Meta:
        unique_together = ("event", "registration")
