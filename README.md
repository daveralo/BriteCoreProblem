# Product Development Hiring Project

As part for a Product Development Hiring Project for [BriteCore](https://www.britecore.com/) in [this](https://github.com/IntuitiveWebSolutions/ProductDevelopmentProject) repository, this is a solution for the problem where the data model is pretty rigid. This solution is focus to insurers can define their own custom data model for their risk.

## Backend

For Backend I used [Django](https://www.djangoproject.com/) and [Django REST framework](https://www.django-rest-framework.org/) with two models:

```
class Risk(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name


class Field(models.Model):
    TYPE_CHOICES = (
        ('text', 'Text'),
        ('date', 'Date'),
        ('number', 'Number'),
    )
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES,
                            default='text')
    label = models.CharField(max_length=100)
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
```

## Data

### Entity relationship diagram 

![alt text](https://github.com/daveralo/BriteCoreProblem/blob/master/er-risk.png)

### Creating risks and fields

```
from risk.models import Risk, Field

Risk.objects.create(
    name='automobile', 
    description='Risk for automobile insurance')

automobile = Risk.objects.create(
    name='automobile',
    description='Risk for automobile insurance')

Field.objects.create(
    name='chassis',
    type='text',
    label='Chassis',
    risk=automobile)    

Field.objects.create(
    name='color',
    type='text',
    label='Color',
    risk=automobile)    

Field.objects.create(
    name='purchase_date',
    type='date',
    label='Purchase date',
    risk=automobile)            

Field.objects.create(
    name='commercial_value',
    type='number',
    label='Commercial value',
    risk=automobile)    

person = Risk.objects.create(
    name='person',
    description='Risk for life insurance')

Field.objects.create(
    name='first_name',
    type='text',
    label='First name',
    risk=person) 

Field.objects.create(
    name='last_name',
    type='text',
    label='Last name',
    risk=person) 

Field.objects.create(
    name='birth_date',
    type='date',
    label='Birth date',
    risk=person)     
```

## Frontend

description

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [Django](https://www.djangoproject.com/) - python Web framework
* [Django REST framework](https://www.django-rest-framework.org/) - powerful and flexible toolkit for building Web APIs
* [PostgreSQL](https://www.postgresql.org/) -  open source relational database

