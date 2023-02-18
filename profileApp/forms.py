from django import forms
from profileApp.models import *

model_choice = [('TAMIYA', 'Toyota Supra'),
                ('SUBARU IMPREZA WRC', 'SUBARU IMPREZA WRC'),
                ('XANAVI NISMO GTR R35','XANAVI NISMO GTR R35'),
                ('MAZDA RX-7 R1', 'MAZDA RX-7 R1'),
                ('SUH-60L BLACK HAWK', 'SUH-60L BLACK HAWK'),
                ('USS Missouri BB 63', 'USS Missouri BB 63'),
                ('SOPWITH CAMAL WW1', 'SOPWITH CAMAL WW1')]

scale_Choice = [('1/24', '1/24'),
                ('1/48', '1/48'),
                ('1/72', '1/72'),
                ('1/144', '1/144')]

toybrand_Choice = [('TAMIYA', 'TAMIYA'),
                   ('ACADEMY PLASTIC KITS', 'ACADEMY PLASTIC KITS')]

type_Choice = [(' Tank', 'Tank'),
               (' helicopter', 'helicopter'),
               (' boat', ' boat'),
               (' Motorcycle', ' Motorcycle'),
               (' CARS', ' CARS')]

year_Choice = [('2023', '2023'),
               ('2020', '2020'),
               ('2018', '2018'),]

colortype_Choice = [('color', 'color'),
                    ('sticker', 'sticker')
                    ]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('id','model', 'scale', 'toybrand', 'type', 'year', 'colortype')
        widgets = {
            'id': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=model_choice),
            'scale': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=scale_Choice),
            'toybrand': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=toybrand_Choice),
            'type': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=type_Choice),
            'year': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=year_Choice),
            'colortype': forms.RadioSelect(attrs={'class': 'form-inline'}, choices=colortype_Choice),
        }
        labels = {
            'id': 'ID',
            'model': 'Model',
            'scale': 'Scale',
            'toybrand': 'Toybrand',
            'type': 'Type',
            'year': 'Year',
            'colortype': 'Colortype',
        }