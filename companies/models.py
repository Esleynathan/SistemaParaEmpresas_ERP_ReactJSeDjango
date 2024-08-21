from django.db import models


class Enterprise(models.Model):
    nome = models.CharField(max_length=150)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

class Employee(models.Model):
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    entreprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)