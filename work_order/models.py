from django.db import models

class LeadTech(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class ServiceType(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Payment(models.Model):
    payment_type = models.CharField(max_length = 100)

    def __str__(self):
        return self.payment_type

class Techs(models.Model):
    techs = models.IntegerField()
    lbr_rate = models.IntegerField()
    
class ServiceRequest(models.Model):
    wo = models.CharField(max_length=100, unique=True)
    district = models.CharField(max_length=100)
    lead_tech = models.ForeignKey(LeadTech, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    rush = models.BooleanField(null=True)
    req_date = models.DateField()
    work_date = models.DateField()
    techs = models.IntegerField()
    wty_lbr = models.BooleanField(null=True)
    wty_parts = models.BooleanField(null=True)
    lbr_hrs = models.FloatField(null=True)
    parts_cost = models.FloatField()
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    @property
    def lbr_rate(self):
        #get lbr_rate from Techs table based on techs field
        pass

    @property
    def work_day(self):
        #get working day based on work_date
        pass
    






