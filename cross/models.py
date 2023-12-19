from django.db import models
from django.contrib.postgres.fields import ArrayField

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    img = models.TextField()  # Assuming img is stored as a text field

    def __str__(self):
        return self.name

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    lan = models.ForeignKey(Language, on_delete=models.CASCADE)
    location = models.CharField(max_length=255,default=None)
    def __str__(self):
        return self.name

class Terms(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    nav = models.JSONField()
    lan = models.ForeignKey(Language, on_delete=models.CASCADE)
    content = models.TextField(max_length=7000)
    button = models.TextField()

    def __str__(self):
        return self.title

class Price(models.Model):
    id = models.AutoField(primary_key=True)
    input = ArrayField(models.CharField(max_length=255))
    button = ArrayField(models.CharField(max_length=255))
    button_main = models.JSONField()
    sidebar_content_main =  models.JSONField()
    sidebar_content = ArrayField(models.CharField(max_length=255))
    sidebar_title = models.TextField()
    lan = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return f"Price ID: {self.id}, Language: {self.lan.name}"


class Price_Article(models.Model):
    id = models.AutoField(primary_key=True)
    articleno = models.IntegerField()
    product = models.CharField(max_length=255)
    inprice = models.IntegerField()
    price = models.IntegerField(default=None)
    unit = models.CharField(max_length=255)
    instock = models.IntegerField()
    description = models.TextField()
    lan = models.ForeignKey(Language, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Article ID: {self.id}, Product: {self.product}, User: {self.user.name} Language: {self.lan.name}"
