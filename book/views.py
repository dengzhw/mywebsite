from django.shortcuts import render
from django.db.models import Max, F, Q
from .models import BookInfo


def index(request):
    # list = BookInfoookInfo.books2.aggregate(Max('bpub_date'))
    # list = BookInfo.books1.filter(bread__gte=F('bcomment')*0)
    # list = BookInfo.books1.filter(pk__lt=3)
    list = BookInfo.books1.filter(Q(pk__lt=3) | Q(bread__gt=2))

    context = {'list': list}
    return render(request, 'book/index.html', context)
