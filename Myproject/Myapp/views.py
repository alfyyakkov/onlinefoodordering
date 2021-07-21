from django.shortcuts import render,HttpResponse,redirect
from Myapp.forms import *
from Myapp.models import *
# Create your views here.
def Welcome(request):
    return render(request,'hi.html')
def Foodapp(request):
    if request.method=='POST':
        frmUp=Signup(request.POST)
        if frmUp.is_valid():
            Name=frmUp.cleaned_data['name']
            Email=frmUp.cleaned_data['email']
            PassWord=frmUp.cleaned_data['password']
            User=Newuser(name=Name,email=Email,password=PassWord)
            User.save()
            return redirect(Login)
        else:
            return HttpResponse("Registration failed...")
    else:return render(request,'Reg.html')
def Login(request):
    if request.method=='POST':
        frmIn=LogIn(request.POST)
        if frmIn.is_valid():
            Email=frmIn.cleaned_data['email']
            PassWord=frmIn.cleaned_data['password']
            a=Newuser.objects.all()
            for i in a:
                if i.email==Email:
                    if i.password==PassWord:
                        return redirect(Items)
                    else:
                        return HttpResponse('Incorrect Password')
            else:
                return redirect(Foodapp)
        else:
            return HttpResponse("Login failed")
    else:
        return render(request,'Log.html')
def Newitem(request):
    if request.method=='POST':
        frmup=FileUp(request.POST,request.FILES)
        if frmup.is_valid():
            Name=frmup.cleaned_data['Item_name']
            Price=frmup.cleaned_data['Item_price']
            Image=frmup.cleaned_data['Item_image']
            Item=NewItem(Item_name=Name,Item_price=Price,Item_image=Image)
            Item.save()
            return HttpResponse('Item added successfully...')
        else:
            return HttpResponse("Failed to add item...")
    else:
        return render(request,'fileup.html')
def ItemDisplay(request):
    x=NewItem.objects.all()
    Li=[]
    Ni=[]
    for i in x:
        path=i.Item_image
        Li.append(str(path).split('/')[2])
        Ni.append(i.Item_name)
    return render(request,'Itempage.html',{'Image':zip(Li,Ni)})
def Items(request):
    x=NewItem.objects.all()
    ItemName=[]
    ItemPrice=[]
    ItemImage=[]
    for i in x:
        path=i.Item_image
        ItemImage.append(str(path).split('/')[2])
        ItemName.append(i.Item_name)
        ItemPrice.append(i.Item_price)
    return render(request,'redir.html',{'Name':zip(ItemName,ItemPrice,ItemImage)})
def HomePage(request):
    return render(request,'ItemView.html')
def Ordering(request,val):
    x=NewItem.objects.all()
    for i in x:
        if i.Item_name==val:
            path=i.Item_image
            return render(request,'Order.html',{'Url': (str(path).split('/')[2]),'Name':i.Item_name,'Price':i.Item_price})
def testingorder(request):
    return render(request,'Order.html')
def BillAmount(request):
    if request.method=='POST':
        frm=Billamount(request.POST)
        if frm.is_valid():
            Name=frm.cleaned_data['Name']
            Price=frm.cleaned_data['Price']
            Quatity=frm.cleaned_data['Quatity']
            Total=Price*Quatity
            Bill(Name=Name,Price=Price,Quatity=Quatity,Total=Total).save()
            # return HttpResponse('success')
            return render(request,'bill.html',{'Name':Name,'Price':Price,'Quatity':Quatity,'Total':Total})
        else:
            HttpResponse('Order failed')
    else:return render(request,'Order.html')
def ViewOrders(request):
    B=Bill.objects.all()
    Name=[]
    Price=[]
    Quantity=[]
    Total=[]
    count=0
    for i in B:
        Name.append(i.Name)
        Price.append(i.Price)
        Quantity.append(i.Quatity)
        Total.append(i.Total)
        count+=1
    return render(request,'Orders.html',{'Orders':zip(Name,Price,Quantity,Total)})