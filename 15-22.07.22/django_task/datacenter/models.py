from django.db import models
import django
import datetime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(
                f'leaved at {self.leaved_at}'
                if self.leaved_at else 'not leaved'
            )
        )

    def format_duration(self):
        seconds = int(self.total_seconds())
        return str(datetime.timedelta(seconds=seconds))

    def get_duration(self):
        delta = django.utils.timezone.localtime() - self.entered_at
        return Visit.format_duration(delta)

    def is_visit_long(self, minutes=60):
        if self.leaved_at:
            delta = self.leaved_at - self.entered_at
            seconds = int(delta.total_seconds())
            return seconds > minutes*60
        else:
            return False
