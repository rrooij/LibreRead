from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=50)
    country_code = models.CharField(max_length=5)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField('Date of birth')
    birthplace = models.CharField(max_length=100)
    country = models.ForeignKey(Country)

    def __str__(self):
        return '{0} {1} {2}'.format(self.first_name,
                                    self.middle_name, self.last_name)


class Book(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=200)
    pub_date = models.DateField('Publication date')

    def __str__(self):
        return self.title


class BookStatus(models.Model):
    status = models.ForeignKey(Status)
    book = models.ForeignKey(Book)
    book_reader = models.ForeignKey('BookReader')


class BookReader(models.Model):
    user = models.OneToOneField(User)
    friends = models.ManyToManyField('self', blank=True)


class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField()
    reviewer = models.ForeignKey(BookReader)
    book = models.ForeignKey(Book)
