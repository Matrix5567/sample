from django.db import models



class Category(models.Model):
    language = models.CharField(max_length=50)
    def __str__(self):
        return self.language




class Item(models.Model):
    category = models.CharField(max_length=255)
    subcatgeory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    language = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str:
        return self.name