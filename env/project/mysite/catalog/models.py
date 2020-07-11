from django.db import models
import uuid

class Genre(models.Model):
    """ model representating book genre """

    name = models.CharField(max_length=200, help_text="Enter Book Genre..")

    def __str__(self):
        return self.name


class Book(models.Model):
    """ model representating book """

    title = models.CharField(max_length=200)

    """ book can only have one author """
    author = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=1000, help_text="Enter The Summary Of The Book..")
    isBn = models.CharField('ISBN',max_length=13,help_text="Search In Google To Find More About It..")

    """ genre can have many books and books can have many genre """
    genre = models.ManyToManyField(Genre,help_text="Select Genre For This Book..")


    def __str__(self):
        return self.title


    # def get_absolute_url(self):
    #     """ return the url to access the detail record for this book """
    #     return reverse('book-detail',arg=[str(self.id)])


class BookInstance(models.Model):
    """ model representating specific copy of book eg.specific book can be borrowed and not available for a moment. """

    id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey('Book', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    LOAN_STATUS = (
        ('m','Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )
    status = models.CharField(max_length=1,choices=LOAN_STATUS, blank=True, default='m', help_text="Book Availability")

    class Meta:
        ordering = ['due_back']


    def __str__(self):
        return f'{self.id} ({self.book.title})'



class Author(models.Model):
    """ models representating an author. """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
