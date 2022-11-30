from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class Business(models.Model):
    business_id = models.CharField(max_length=100)
    business_name = models.CharField(max_length=100)
    yelp_business_id = models.CharField(max_length=45, blank=True, null=True)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=15, blank=True, null=True)
    latitude = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    longitude = models.DecimalField(max_digits=100, decimal_places=2, blank=True, null=True)
    business_stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    business_review_count = models.IntegerField(blank=True, null=True)
    is_open = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'business'
        ordering = ['business_name', 'business_stars', 'is_open']
        verbose_name = 'Business Information'
        verbose_name_plural = "Business's Information"

    def __str__(self):
        return f"{self.business_id}, {self.business_name}, {self.yelp_business_id}, {self.phone},\
        {self.city}, {self.state}, {self.address}, {self.postal_code}, {self.latitude}, {self.longitude},\
        {self.business_stars}, {self.business_review_count}, {self.is_open}"

class Googlemodel(models.Model):
    Resname = models.CharField(max_length = 100)
    Address = models.CharField(max_length = 100)
    Lat = models.CharField(max_length = 100)
    Long = models.CharField(max_length = 100)

    class Meta:
        managed = True
        db_table = 'Googlemodel'

    def __str__(self):
        return f"{self.Resname}, {self.Address}, {self.Lat}, {self.Long}"

class GoogleInputmodel(models.Model):
    Foodinput=models.CharField(blank=True, null=False, max_length = 100)

    class Meta:
        managed = True
        db_table = 'GoogleInputmodel'

class Nutritionmodel(models.Model):
    item_id = models.CharField(max_length = 100)
    item_name = models.CharField(max_length = 100)
    resturaunt_name = models.CharField(max_length = 100)
    

    class Meta:
        managed = True
        db_table = 'Food_Items'

    def __str__(self):
        return f"{self.item_id}, {self.item_name}, {self.resturaunt_name}"



class NutritionInputmodel(models.Model):
    Nutritioninput=models.CharField(blank=True, null=False, max_length = 100)

    class Meta:
        managed = True
        db_table = 'NutritionInputmodel'

class Foodnutritionmodel(models.Model):
    qname = models.CharField(max_length = 100)
    qcalories = models.CharField(max_length = 100)
    qserving = models.CharField(max_length = 100)
    qfattotal = models.CharField(max_length = 100)
    qfatsat = models.CharField(max_length = 100)
    qprotein = models.CharField(max_length = 100)
    qsodium = models.CharField(max_length = 100)
    qpotassium = models.CharField(max_length = 100)
    qcholesterol = models.CharField(max_length = 100)
    qcarb = models.CharField(max_length = 100)
    qfibe = models.CharField(max_length = 100)
    qsugar = models.CharField(max_length = 100)
    

    class Meta:
        managed = True
        db_table = 'NutritionFix'

    def __str__(self):
        return f"{self.qname}, {self.qcalories}, {self.qserving}, {self.qfattotal}, {self.qfatsat}, {self.qprotein}, {self.qpotassium}, {self.qcholesterol}, {self.qcarb}, {self.qfibe}, {self.qsugar}"


class FoodnutritionInputmodel(models.Model):
    Macroinput=models.CharField(blank=True, null=False, max_length = 100)

    class Meta:
        managed = True
        db_table = 'FoodNutritionInputmodel'


class YelpInputModel(models.Model):
    term = models.CharField(blank=True, null=False, max_length=100)
    location = models.CharField(blank=True, null=False, max_length=100)

    class Meta:
        managed = True
        db_table = 'yelpinputmodel'

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    city_name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'city'
        ordering = ['city_name']
        verbose_name = 'Business city'
        verbose_name_plural = "Business's city"

    def __str__(self):
        return self.city_name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    business = models.ForeignKey('Business', models.PROTECT, blank=False, null=False)
    user = models.ForeignKey('User', models.PROTECT, blank=False, null=False)
    stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    date_created = models.DateField(blank=True, null=False)
    review_text = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'review'
        ordering = ['business', 'user', 'stars', 'date_created', 'review_text']
        verbose_name = 'Review made by user about a business'
        verbose_name_plural = "Reviews made by users about various businesses"

class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    state_abbrev = models.CharField(unique=True, max_length=10)

    class Meta:
        managed = False
        db_table = 'state'
        ordering = ['state_abbrev']
        verbose_name = 'State where the Business is located'
        verbose_name_plural = "State where the Business is located"

    def __str__(self):
        return self.state_abbrev

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=45, unique=True)
    email = models.EmailField(blank=False, null=False)
    review_count = models.IntegerField()
    yelper_since = models.DateField(blank=True, null=False)
    average_stars = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=False)
    yelp_user_id = models.CharField(max_length=45, blank=True, null=False)
    business = models.ManyToManyField(Business, through='Review')

    USERNAME_FIELD = 'username'

    class Meta:
        managed = False
        db_table = 'user'
        ordering = ['username', 'review_count', 'average_stars', 'yelper_since']
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    def get_absolute_url(self):
		# return reverse('site_detail', args=[str(self.id)])
        return reverse('user_detail', kwargs={'pk': self.pk})

    @property
    def business_names(self):

        businesses = self.business.order_by('business_name')

        names = []
        for business in businesses:
            name = business.business_name
            if name is None:
                continue
            if name not in names:
                names.append(name)
        return ', '.join(names)
