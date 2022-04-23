from django.db.models import *
from django.contrib.auth.models import User

class Paint(Model):
    title = CharField(max_length=64)
    image = ImageField(upload_to='images', blank=True, null=True)
    is_active = BooleanField(default=True)
    content = TextField()
    related_user = ForeignKey(User, on_delete=CASCADE, default=1)

    def __str__(self):
        return self.title