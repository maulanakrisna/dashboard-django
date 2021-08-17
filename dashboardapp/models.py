from django.db import models


class Sti(models.Model):
    name = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Office(models.Model):
    sti = models.ForeignKey(Sti, on_delete=models.CASCADE)
    name = models.CharField(max_length=256)
    email = models.EmailField()
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Address(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    pub_date = models.DateTimeField('date published')


class Router(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    sid = models.CharField(max_length=32)
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sid


class Network(models.Model):
    IPVPN = 'IPVPN'
    VSAT = 'VSAT'
    INTERNET = 'INTERNET'
    METRONET = 'METRONET'

    CHOICES = (
        (IPVPN, "IPVPN"),
        (VSAT, "VSAT"),
        (INTERNET, "INTERNET"),
        (METRONET, "METRONET"),
    )

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    sid = models.CharField(max_length=32)
    type = models.CharField(max_length=32, choices=CHOICES, default=IPVPN)
    bandwidth = models.CharField(max_length=32)
    ip_address = models.CharField(max_length=64)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sid


class Computer(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    sid = models.CharField(max_length=32)
    monitor = models.CharField(max_length=64)
    processor = models.CharField(max_length=64)
    memory = models.CharField(max_length=64)
    storage = models.CharField(max_length=64)
    serial_number = models.CharField(max_length=64)
    employee_name = models.CharField(max_length=64)
    pub_date = models.DateTimeField('date published')


class Itsupport(models.Model):
    Analyst = 'Analyst'
    FieldEngineer = 'Field Engineer'
    FieldSupport = 'Field Support'

    CHOICES = (
            (Analyst, 'Analyst'),
            (FieldEngineer, 'Field Engineer'),
            (FieldSupport, 'Field Support'),
    )

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    sid = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    jobdescription = models.CharField(
        max_length=32, choices=CHOICES, default=FieldSupport)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name
