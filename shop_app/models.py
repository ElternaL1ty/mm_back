from django.db import models, migrations
from django.conf import settings
from django.core.validators import MinValueValidator
from django.contrib.postgres.fields import ArrayField
# Create your models here.
def get_default():
    return [None]

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=False)
    parent = models.ForeignKey('Category', on_delete=models.RESTRICT, blank=True, null=True)

    def __str__(self):
        if self.parent is not None:
            return str(self.parent) + " > "  + self.name
        else:
            return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=False)
    varcode = models.CharField(max_length=8, blank=False)
    categories = models.ManyToManyField(Category)
    desc = models.TextField(default="Нет описания")
    price = models.IntegerField(validators=[MinValueValidator(1)], blank=False)
    amount = models.IntegerField(default=1)
    image1 = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100, default='media/default.png')
    image2 = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,
                              default='media/default.png')
    image3 = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,
                              default='media/default.png')
    image4 = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,
                              default='media/default.png')
    image5 = models.ImageField(upload_to='media/', height_field=None, width_field=None, max_length=100,
                              default='media/default.png')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class Order(models.Model):

    STATUSES = (
        ('DONE', 'Done'),
        ('IN WORK', 'In work'),
        ('CANCELED', 'Canceled'),
        ('CREATED', 'Created'),
    )
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, blank=False)
    products = models.JSONField()
    status = models.CharField(max_length=50, choices=STATUSES, default='Created')
    create_date = models.DateTimeField(auto_now=True)
    complete_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.id)