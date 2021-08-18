from django.db import models


class Sti(models.Model):
    name = models.CharField(max_length=256, unique=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Office(models.Model):
    sti = models.ForeignKey(Sti, on_delete=models.CASCADE)
    name = models.CharField(max_length=256, unique=True)

    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.name


class Address(models.Model):
    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=32, null=True)
    fax = models.CharField(max_length=32, null=True)
    address1 = models.CharField(max_length=256)
    address2 = models.CharField(max_length=256)
    zipcode = models.CharField(max_length=32)
    city = models.CharField(max_length=32)
    province = models.CharField(max_length=64, null=True)
    latitude = models.CharField(max_length=16, null=True)
    longitude = models.CharField(max_length=16, null=True)
    pub_date = models.DateTimeField('date published')


class Router(models.Model):
    GOLD = 'GOLD'
    SILVER = 'SILVER'
    CHOICES = (
        (GOLD, 'GOLD'),
        (SILVER, 'SILVER'),
    )

    office = models.ForeignKey(Office, on_delete=models.CASCADE)
    sid = models.CharField('S I D', max_length=32, unique=True)
    type = models.CharField(max_length=16, choices=CHOICES, default=SILVER)
    brand = models.CharField(max_length=256)
    model = models.CharField(max_length=256)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.sid + ' | ' + self.office.name


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
    sid = models.CharField(max_length=32, unique=True)
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
    serial_number = models.CharField(max_length=64, null=True)
    employee_name = models.CharField(max_length=64, null=True)
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
