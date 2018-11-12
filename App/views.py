

# Create your views here.
import hashlib
import uuid

from django.shortcuts import render, redirect

from App.models import User, Wheel, Goods


# 首页
def index(request):
    goods = Goods.objects.all()
    wheel = Wheel.objects.all()

    token = request.session.get('token')
    print(token,'**********8')
    if not token:
        name = None
    else:
        user = User.objects.filter(token=token).first()
        name = user.phone

    data = {
        'name':name,
        'wheel':wheel,
        'goods': goods

    }
    return render(request,'index.html',context=data)


def goodinfo(request):
    return render(request,'goodinfo.html')


def goodlist(request):
    goods = Goods.objects.all()
    wheel = Wheel.objects.all()

    data = {
        'wheel': wheel,
        'goods': goods

    }

    return render(request,'goodlist.html',context=data)


def goodsinfo(request):
    wheel = Wheel.objects.all()

    data = {
        'wheel': wheel,

    }
    return render(request,'goodsinfo.html',context=data)

# 登录
def login(request):
    wheel = Wheel.objects.all()

    data = {
        'wheel': wheel,

    }

    if request.method == 'GET':
        return render(request,'login.html',context=data)
    elif request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password = secret(password)
        try:
            users = User.objects.filter(phone=phone).filter(password=password)
            print(users)
            user = users.first()
            user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
            user.save()
            request.session['token'] = user.token
            return redirect('dr:index')
        except:
            return redirect('dr:login')

# 注册
def register(request):
    wheel = Wheel.objects.all()

    data = {
        'wheel': wheel,

    }


    if request.method == 'GET':
        return render(request,'register.html',context=data)
    elif request.method == "POST":
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        password = secret(password)
        user = User()
        user.phone = phone
        user.password = password
        user.token = str(uuid.uuid5(uuid.uuid4(),'register'))
        user.save()
        request.session['token'] = user.token
        return redirect('dr:index')


def shopcar(request):
    return render(request,'shopcar.html')


# md5加密
def secret(password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    return md5.hexdigest()


# 退出
def logout(request):
    request.session.flush()
    return redirect('dr:index')