from django.db import models

class Lead(models.Model):
    company_name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    application = models.CharField(max_length=100)

    capacity = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        help_text="Raw capacity input exactly as entered by the user"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.company_name} - {self.capacity}"


    