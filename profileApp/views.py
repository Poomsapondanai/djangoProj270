from django.shortcuts import render, redirect

from profileApp.forms import ProductForm
from profileApp.models import *

# Create your views here.
def profile(request):
    return render(request, 'profile.html')

def education(request):
    return render(request, 'education.html')


def insteres(request):
    return render(request, 'insteres.html')


def idol(request):
    return render(request, 'idol.html')


def sale(request):
    return render(request, 'sale.html')


def ShowMyData(request):
    IdCard = "1104300400307"
    Name = "สพลดนัย เจาะจง"
    Address = "ขอนเเก่น"
    Domicile = "ร้อยเอ็ด"
    Gender = "ชาย"
    Weight = "107"
    Height = "194"
    Favoritecolor = "สีม่วง"
    FavoriteFood = "เเหนมเนือง"
    Work = "student"
    products = [
        ['Bike001','/static/images/panigale.png' ,'Ducati Panigale 899', 759000.00],
        ['Bike002', '/static/images/mt09.png','Yamaha MT09 ', 420000.00],
        ['Bike003', '/static/images/xsr.png','Yamaha Xsr900 ', 459000.00],
        ['Bike004', '/static/images/tmax.png','Yamaha Tmax', 550000.00],
        ['Bike005', '/static/images/r1.png','Yamaha R1', 890000.00],
        ['Bike006', '/static/images/1100.png','Ducati Scrambler 1100', 890000.00],
        ['Bike007', '/static/images/cbr1000rr.png', 'Honda CBR1000RR', 1190000.00],
        ['Bike008', '/static/images/xadv.png', 'Honda XADV750 ', 445000.00],
        ['Bike009', '/static/images/zx10r.png', 'Kawasaki Zx10r', 990000.00],
        ['Bike0010', '/static/images/z1000.png', 'Kawasaki Z900', 429000.00],
    ]
    context = {'idcard': IdCard, 'name': Name, 'address': Address, 'domicile': Domicile, 'gender': Gender,'weight':Weight , 'height': Height,
               'favoritecolor': Favoritecolor, 'favoritefood':FavoriteFood, 'work':Work, 'product':products,}
    return render(request, 'ShowData.html',context)
lstOurProduct = []
def listProduct(request):
    context = {'product':lstOurProduct}
    return render(request, 'listProduct.html',context)

def inputProduct(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            id = form.get('id')
            model = form.get('model')
            scale = form.get('scale')
            toybrand = form.get('toybrand')
            type = form.get('type')
            year = form.get('year')
            colortype = form.get('colortype')

            if model == 'Toyota Supra':
                pModel = 1200
            elif model == 'SUBARU IMPREZA WRC':
                pModel = 1900
            elif model == 'XANAVI NISMO GTR R35':
                pModel = 2000
            elif model == 'MUH-60L BLACK HAWK':
                pModel = 1200
            elif model == 'USS Missouri BB 63':
                pModel = 1300
            elif model == 'SUH-60L BLACK HAWK':
                pModel = 1300
            elif model == 'USS Missouri BB 63':
                pModel = 1300
            else:  # CADEMY 12568 USAF F-15E D-DAY 75th
                pModel = 1200


            if scale == '1/20':
                pScale = 0
            elif scale == '1/24':
                pScale = 0
            elif scale == '1/12':
                pScale = 500
            elif scale == '1/18':
                pScale = 0
            elif scale == '1/32':
                pScale = 0
            elif scale == '1/72':
                pScale = 0
            else:  # 144
                pScale = 500


            if toybrand == 'Tamiya' or 'ACADEMY PLASTIC KITS':
                pToybrand = 0
            else:  # ACADEMY PLASTIC KITS
                pToybrand = 0

            if type == ' CARS':
                pType = 1200
            elif type == ' Motorcycle':
                pType = 900
            elif type == ' boat':
                pType = 1500
            elif type == ' tank':
                pType = 2500
            else:  # plane
                pType = 4500


            if year == '2023':
                pYear = 0
            elif year == '2020':
                pYear = 0
            else:  # 2018
                pYear = 0

            if colortype == 'Sticker':
                pColortype = 300
            else:  # color'
                pColortype = 500

            pSum = pModel + \
                   pScale + \
                   pToybrand + \
                   pType + \
                   pYear + \
                   pColortype

            if pSum < 2000:
                pDiscount = pSum * 5 / 100
            elif pSum < 3000:
                pDiscount = pSum * 15 / 100
            else:
                pDiscount = pSum * 10 / 100

            pTotal = pSum - pDiscount

            ProductList = Product(id,model,scale,toybrand,type,year,colortype)
            lstOurProduct.append(ProductList)
            return redirect('listProduct')
        else:
            form = ProductForm(form)
    else:
        form = ProductForm()
        context = {'form':form}
        return render(request,'inputProduct.html',context)
