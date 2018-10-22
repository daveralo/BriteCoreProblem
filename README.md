# Product Development Hiring Project

As part for a Product Development Hiring Project for [BriteCore](https://www.britecore.com/). This is a solution for the problem where the data model is pretty rigid. This solution is focus to insurers can define their own custom data model for their risk.

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

For Frontend I used [Vue.js](https://vuejs.org/) and [Boostrap](http://getbootstrap.com/) 

## Running the tests

You can run the unit tests using the following command

```
python manage.py test
```

## Deployment

For Frontend I used [Zappa](https://www.zappa.io/)

```

$ pip install zappa
$ zappa init
$ zappa deploy dev
Deploying..
Your application is now live at: https://itqbut4z6g.execute-api.us-east-1.amazonaws.com/dev/

```

Next you have to modify settings.py with credentials and host of AWS, then you can update your deploy:

```

$ zappa update dev

```


## Built With

* [Django](https://www.djangoproject.com/) - python Web framework
* [Django REST framework](https://www.django-rest-framework.org/) - powerful and flexible toolkit for building Web APIs
* [PostgreSQL](https://www.postgresql.org/) -  open source relational database
* [Vue.js](https://vuejs.org/) - JavaScript Framework
* [Boostrap](http://getbootstrap.com/) - open source toolkit for developing with HTML, CSS, and JS.


