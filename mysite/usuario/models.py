from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
    nome = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.id} - {self.nome}"

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.PROTECT, null=False) # Changed on_delete

    def __str__(self):
        return f"{self.id} - {self.user.username} ({self.role.nome})"
