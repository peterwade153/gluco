import uuid
from django.db import models


class GlucoseLevel(models.Model):
    user_id = models.UUIDField(default=uuid.uuid4)
    seriennummer = models.CharField(max_length=255)
    gerätezeitstempel = models.DateTimeField(auto_now_add=True)
    aufzeichnungstyp = models.IntegerField()
    glukosewert_verlauf = models.IntegerField(help_text='mg/dL')
    glukose_scan = models.IntegerField(help_text='mg/dL')
