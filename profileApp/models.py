from django.db import models

class Product(models.Model):
    id = models.CharField(max_length=6, default='',primary_key=True)
    model = models.CharField(max_length=100, default='')
    scale = models.CharField(max_length=100, default='')
    toybrand = models.CharField(max_length=100, default='')
    type = models.CharField(max_length=100, default='')
    year = models.CharField(max_length=100, default='')
    colortype = models.CharField(max_length=100, default='')

    def pModel(self):
        if self.model == 'Toyota Supra':
            pModel = 1200
        elif self.model == 'SUBARU IMPREZA WRC':
            pModel = 1900
        elif self.model == 'XANAVI NISMO GTR R35':
            pModel = 2000
        elif self.model == 'MAZDA RX-7 R1':
            pModel = 1200
        elif self.model == 'SOPWITH CAMAL WW1':
            pModel = 1300
        elif self.model == 'SUH-60L BLACK HAWK':
            pModel = 1300
        elif self.model == 'USS Missouri BB 63':
            pModel = 1300
        else:#CADEMY 12568 USAF F-15E D-DAY 75th
            pModel = 1200
        return pModel

    def pScale(self):
        if self.scale == '1/20':
            pScale = 0
        elif self.scale == '1/24':
            pScale = 0
        elif self.scale == '1/12':
            pScale = 500
        elif self.scale == '1/18':
            pScale = 0
        elif self.scale == '1/32':
            pScale = 0
        elif self.scale == '1/72':
            pScale = 0
        else:#144
            pScale = 500
        return pScale

    def pToybrand(self):
        if self.toybrand == 'Tamiya' or 'ACADEMY PLASTIC KITS':
            pToybrand = 0
        else:#ACADEMY PLASTIC KITS
            pToybrand = 0
        return pToybrand

    def pType(self):
        if self.type == ' CARS':
            pType = 1200
        elif self.type == ' Motorcycle':
            pType = 900
        elif self.type == ' boat':
            pType = 1500
        elif self.type == ' tank':
            pType = 2500
        else:#plane
            pType = 4500
        return pType

    def pYear(self):
        if self.year == '2023':
            pYear = 0
        elif self.year == '2020':
            pYear = 0
        else:#2018
            pYear = 0
        return pYear

    def pColortype(self):
        if self.colortype == 'Sticker':
            pColortype = 300
        else:#color'
            pColortype = 500
        return pColortype

    def pSum(self):
        pSum = self.pModel()+ \
               self.pScale()+ \
               self.pToybrand()+ \
               self.pType()+ \
               self.pYear()+ \
               self.pColortype()
        return pSum

    def pDiscount(self):
        if self.pSum() <2000:
            pDiscount = self.pSum()*5/100
        elif self.pSum() <4000:
            pDiscount = self.pSum()*10/100
        else:
            pDiscount = self.pSum()*15/100
        return pDiscount

    def pTotal(self):
        pTotal = self.pSum() - self.pDiscount()
        return pTotal

    def __str__(self):
        text = str(self.id) + ' : ' \
               + str(self.model) + ',' \
               + str(self.scale) + ',' \
               + str(self.toybrand) + ',' \
               + str(self.type) + ',' \
               + str(self.year) + ',' \
               + str(self.colortype) + ',' \
               + str(self.pTotal())
        return text