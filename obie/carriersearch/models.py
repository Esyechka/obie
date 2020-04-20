from django.db import models

# Create your models here.


class State(models.Model):
    ''' 
    I am not making states an object because there might be attributes which 
    will need to be assigned to states in the future. As well as ease of REST and
    bi-directional relationships.
    '''
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Carrier(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Policy(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Offering(models.Model):
    policy = models.ForeignKey(Policy, blank=True, on_delete=models.CASCADE)
    carrier = models.ForeignKey(Carrier, blank=True, on_delete=models.CASCADE)
    state = models.ForeignKey(State, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        # f-strings are the best thing to happen since python
        return f"{self.policy} {self.carrier} {self.state}"
