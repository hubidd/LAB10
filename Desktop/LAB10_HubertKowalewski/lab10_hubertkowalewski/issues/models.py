from django.db import models

class Problem(models.Model):
    MODULE_CHOICES = [
        ('offer_mng', 'Zarządzanie ofertą'),
        ('offer', 'Oferta publiczna'),
        ('auth', 'Logowanie/Rejestracja'),
        ('other', 'Inne'),
    ]

    data_zgloszenia = models.DateTimeField(auto_now_add=True)
    autor = models.CharField(max_length=150)
    temat = models.CharField(max_length=200)
    opis_problemu = models.TextField()
    modul = models.CharField(max_length=50, choices=MODULE_CHOICES)
    zalacznik = models.ImageField(upload_to='issues_attachments/', null=True, blank=True)

    def __str__(self):
        return f"{self.temat} ({self.autor})"