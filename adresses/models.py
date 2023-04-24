from django.db import models


class Adress(models.Model):
    street = models.CharField(max_length=127)
    number = models.IntegerField()

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
        #   null=True
    )

    # models.PROTECT
    # models.SET_NULL

    def __repr__(self) -> str:
        return f"<Adress ({self.id}) - {self.street}>"
