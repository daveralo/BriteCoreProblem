# BriteCore Problem

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Entity relationship diagram 

![alt text](https://github.com/daveralo/BriteCoreProblem/blob/master/er-risk.png)

### Data

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

### Prerequisites

What things you need to install the software and how to install them

```
https://github.com/daveralo/BriteCoreProblem.git
```

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

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

