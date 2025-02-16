from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from django.views.generic import UpdateView, ListView, DeleteView, DetailView, CreateView
from audioop import reverse

from django.db import models
from django.utils import timezone

from django.urls import reverse, reverse_lazy
from .models import Yangiliklar,Bizhaqimizda_rasm,SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMI,FuterManzil
from blog.forms import royxatForm, CommentForm


def AsosiyPage(request):
    form = royxatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    news = Yangiliklar.objects.all()
    n = SONGI_YILLARDA_BAJARILGAN_ISHLAR_XAJMI.objects.all()
    q = FuterManzil.objects.all()
    context = {
        'news': news,
        'xabar': n,
        "manzil" : q
    }
    return render(request,"AsosiyPage.html",context=context)


def yangiliklar(request):
    form = royxatForm(request.POST or None)
    news = Yangiliklar.objects.all()
    if request.method == "POST" and form.is_valid():
        form.save()
    context = {
        "news":news
    }
    return render(request,"Yangiliklar.html",context=context)
def Biz_haqimizda_rahbariyat(request):
    form = royxatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request,"Biz haqimizda-rahbariyat.html",context={})
def Biz_haqimizda(request):
    form = royxatForm(request.POST or None)
    rasm = Bizhaqimizda_rasm.objects.all()
    if request.method == "POST" and form.is_valid():
        form.save()
    context = {
        "rasm": rasm
    }
    return render(request,"Biz-haqimizda.html",context=context)
def Foter(request):
    form = royxatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request,"Foter.html",context={})
def hamkor(request):
    form = royxatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request,"hamkor.html",context={})
def ishla(request):
    form = royxatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request,"Hizmatlar.html",context={})
def Hujjatlar(request):
    form = royxatForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
    return render(request,"Hujjatlar.html",context={})
def Labaratoriya(request):
    form1 = royxatForm(request.POST or None)
    if request.method == "POST" and form1.is_valid():
        form1.save()
    return render(request,"Labaratoriya.html",context={})
# def news_detel(request,id):
#
#     d = get_object_or_404(Yangiliklar, id=id)
#     post = get_object_or_404(Yangiliklar, id=id)
#     if post:
#         post.views=post.views+1
#         post.save()
#     form1 = royxatForm(request.POST or None)
#     if request.method == "POST" and form1.is_valid():
#         form1.save()
#     detelqogani = Yangiliklar.objects.all()[:4]
#     n = get_object_or_404(Yangiliklar, id=id)
#     comments = n.comments.filter()
#     new_comment = None
#     if request.method == "POST":
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.Yangiliklar = n
#             new_comment.user = request.user
#             new_comment.save()
#             comment_form = CommentForm()
#     context = {
#         "detel":d,
#         "detel_qogani":detelqogani,
#         "news": n,
#         'comments': comments,
#         'new_comment': new_comment,
#         'comment_form': comment_form
#     }
#     return render(request,"tuproq_datel.html",context)
def detail(request, id):
    d = get_object_or_404(Yangiliklar, id=id)
    product = get_object_or_404(Yangiliklar, id=id)
    comments = product.comments.filter(active=True)
    comment_count = comments.count()
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.products = product
            new_comment.user = request.user
            new_comment.save()
            comment_form = CommentForm()
    else:
        comment_form = CommentForm()
    context = {
        'product': product,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form,
        'comment_count': comment_count,
        "detel": d,
    }
    return render(request, "tuproq_datel.html", context=context)
