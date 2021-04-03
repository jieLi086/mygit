
from django.shortcuts import render
from searchbooks import models
from searchbooks.models import Infos, Users
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator



# Create your views here.
# 查询所有信息
def findAll(request):
    if request.method == 'GET':
       bookname = request.GET.get('title')
       if  request.COOKIES.get('isLogin'):
            if bookname is None:
                result = Infos.objects.all()
            else:
                result = Infos.objects.filter(name__contains=bookname)
            currpage = request.GET.get('currpage')

            if currpage is None:
                currpage = 1
            paginator = Paginator(list(result), 10)
            page = paginator.page(currpage)  # 页的page对象
            arr = []
            for i in page:
                txt = {'id': i.id, 'name': i.name, 'url': i.url}
                arr.append(txt)
            context = {'bookList': arr, 'count': len(result), 'currpage': currpage}
            if None != bookname:
                context["bookname"] = bookname
            #     fw = open('static/books_info.json', 'w', encoding ='utf - 8')
            #     dic_json = json.dump(txt, fw, ensure_ascii=False, indent=10)
            return render(request, 'guanli.html', context)
       return render(request, 'login.html')
    return render(request, 'guanli.html', )


# 登录页面
def loginpage(request):
    return render(request, 'login.html')


# 登录功能
def login(request):
    # 获取用户输入的name，password

    if request.method == 'POST':
        username = request.POST.get('name')
        password = request.POST.get('password')
        if username and password:  # 确保用户名和密码都不为空
            username = username.strip()
            try:
                user = models.Users.objects.get(name=username)
                if user.password == password:
                    rep = HttpResponseRedirect('../findAll/')#1
                    rep.set_cookie('isLogin',1)#2
                    return rep
                    # return HttpResponseRedirect('../findAll/')
                else:
                    # dct = {'1':"用户名或者密码不正确！"}
                    return render(request, 'login.html', {'data': '用户名或者密码不正确'})
            except:
                return render(request, 'login.html', {'data': '用户名或者密码不正确'})
        return render(request, 'login.html', {'data': '请输入用户名和密码'})
        # dct = {'1':"用户名或者密码不正确！"}
    return render(request, 'login.html', {'data': '请输入用户名和密码'})

# 检索
def jiansuo(request):
    if request.method == 'GET':
        bookname = request.GET.get('title')
        if request.COOKIES.get('isLogin'):
            if bookname is None:
                result = Infos.objects.all()
            else:
                result = Infos.objects.filter(name__contains=bookname)
            currpage = request.GET.get('currpage')
            if currpage is None:
                currpage = 1
            paginator = Paginator(list(result), 10)
            page = paginator.page(currpage)  # 页的page对象
            arr = []
            for i in page:
                txt = {'id': i.id, 'name': i.name, 'url': i.url}
                arr.append(txt)
            context = {'bookList': arr, 'count': len(result), 'currpage': currpage}
            if None != bookname:
                context["bookname"] = bookname
            #     fw = open('static/books_info.json', 'w', encoding ='utf - 8')
            #     dic_json = json.dump(txt, fw, ensure_ascii=False, indent=10)
            return render(request, 'jiansuo.html', context)
        return render(request,'login.html')
    return render(request, 'jiansuo.html', )


# 帮助
def help(request):
    if request.COOKIES.get('isLogin'):
        return render(request, 'help.html')
    return render(request,'login.html')

# 修改
def update(request):
    if request.COOKIES.get('isLogin'):
        if request.method == 'GET':
            bookid = int(request.GET.get('bookid'))
            name = request.GET.get('bookname')
            bookname = request.GET.get('title')
            url = request.GET.get('bookurl')
            curr = request.GET.get('curr')
            info = Infos.objects.get(id=bookid)
            info.name = name
            info.url = url
            info.save()
            if bookname is None:
                books = Infos.objects.all()
            else:
                books = Infos.objects.filter(name__contains=bookname)
            if curr is None:
                curr = 1
            paginator = Paginator(list(books), 10)
            page = paginator.page(curr)  # 页的page对象
            arr = []
            for i in page:
                txt = {'id': i.id, 'name': i.name, 'url': i.url}
                arr.append(txt)
            context = {'bookList': arr,'count': len(books),'currpage':curr}
            if None != bookname:
                context["bookname"] = bookname
            return render(request, 'guanli.html', context)
        else:
            sid = request.GET.get('bookid')
            book = Infos.objects.get(id=sid)
            book.name = request.POST.get('bookname')
            book.save()
            return HttpResponseRedirect('../findAll/')
    return render(request, 'login.html')


# 删除
def delete(request):
    if request.COOKIES.get('isLogin'):
        if request.method == 'GET':

            bookid = request.GET.get('bookid')
            bookname = request.GET.get('title')
            curr = request.GET.get('curr')
            book = Infos.objects.get(id=bookid)
            book.delete()
            if bookname is None :
                books = Infos.objects.all()
            else:
                books = Infos.objects.filter(name__contains=bookname)
            if curr is None:
                curr = 1
            paginator = Paginator(list(books), 10)
            page = paginator.page(curr)  # 页的page对象
            arr = []
            for i in page:
                txt = {'id': i.id, 'name': i.name, 'url': i.url}
                arr.append(txt)
            context = {'bookList': arr, 'count': len(books), 'currpage': curr}
            if None != bookname:
                context["bookname"] = bookname
            return render(request, 'guanli.html', context)
        else:
            sid = request.GET.get('bookid')
            book = Infos.objects.get(id=sid)
            book.name = request.POST.get('bookname')
            book.save()
            return HttpResponseRedirect('../findAll/')
    return render(request,'login.html')