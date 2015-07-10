from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Date of birth')
    birthplace = models.CharField(max_length=100)
    country = models.ForeignKey(Country)


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)
    pub_date = models.DateField('Publication date')
