from django.shortcuts import render


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

