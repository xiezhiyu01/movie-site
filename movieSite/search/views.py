from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from search.models import *
from django.core.paginator import Paginator
from datetime import datetime
import xlrd


book_m = xlrd.open_workbook(r"C:\Users\XieZhiyu\PycharmProjects\movieSite\影片信息.xls")
sheet_m = book_m.sheet_by_name("影片信息")
book_c = xlrd.open_workbook(r"C:\Users\XieZhiyu\PycharmProjects\movieSite\演员信息.xls")
sheet_c = book_c.sheet_by_name("演员信息")


def exploremovie(request):
    paginator = Paginator(Movie.objects.all(), 16)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 2) + 1)
    return render(request, 'exploremovie.html', {'posts': page, 'page_range': page_range,
                                                 'pagecnt': paginator.num_pages,
                                                 'pagecntminus': paginator.num_pages-1})


def explorecelebrity(request):
    paginator = Paginator(Celebrity.objects.all(), 16)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 2) + 1)
    return render(request, 'explorecelebrity.html', {'posts': page, 'page_range': page_range,
                                                 'pagecnt': paginator.num_pages,
                                                 'pagecntminus': paginator.num_pages-1})


def movie(request, movieid):
    actorsID = eval(sheet_m.cell(movieid-1, 5).value)
    actors = {}
    for i in range(len(actorsID)):
        actors[actorsID[i]+1] = Celebrity.objects.get(id=actorsID[i]+1)
    imgSrc = '<img src="{% static "images/celebritypic/celebrity'+str(0) + '" %}'
    return render(request, 'movie.html', {'id': movieid,
                                          'movie': Movie.objects.get(id=movieid),
                                          'actors': actors,
                                          'imgSrc': imgSrc} )


def celebrity(request, celebrityid):
    moviesID = eval(sheet_c.cell(celebrityid-1, 8).value)
    coopID = eval(sheet_c.cell(celebrityid-1, 4).value)
    coopCnt = eval(sheet_c.cell(celebrityid-1, 5).value)
    movies = {}
    coop = {}
    for i in range(len(moviesID)):
        movies[moviesID[i]+1] = Movie.objects.get(id=moviesID[i]+1)
    for i in range(len(coopID)):
        coop[coopID[i]+1] = []
        coop[coopID[i]+1].append(Celebrity.objects.get(id=coopID[i]+1))
        coop[coopID[i]+1].append(coopCnt[i])
    return render(request, 'celebrity.html', {'id':celebrityid,
                                              'celebrity': Celebrity.objects.get(id=celebrityid),
                                              'movies': movies,
                                              'coop': coop})


def search(request):
    def get_brief(movie):
        res = []
        if movie['comment1'].find(keyword) != -1:
            pos = movie['comment1'].find(keyword)
            if pos < 5:
                res.append( movie['comment1'][:72] + ('……' if 72 < len(movie['comment1']) else ''))
            else:
                res.append( '……' + movie['comment1'][pos - 5: pos + 67] + ('……' if pos + 67 < len(movie['comment1']) else ''))
        if movie['comment2'].find(keyword) != -1:
            pos = movie['comment2'].find(keyword)
            if pos < 5:
                res.append( movie['comment2'][:72] + ('……' if 72 < len(movie['comment2']) else ''))
            else:
                res.append( '……' + movie['comment2'][pos - 5: pos + 67] + ('……' if pos + 67 < len(movie['comment2']) else ''))
        if movie['comment3'].find(keyword) != -1:
            pos = movie['comment3'].find(keyword)
            if pos < 5:
                res.append( movie['comment3'][:72] + ('……' if 72 < len(movie['comment3']) else ''))
            else:
                res.append( '……' + movie['comment3'][pos - 5: pos + 67] + ('……' if pos + 67 < len(movie['comment3']) else ''))
        if movie['comment4'].find(keyword) != -1:
            pos = movie['comment4'].find(keyword)
            if pos < 5:
                res.append( movie['comment4'][:72] + ('……' if 72 < len(movie['comment4']) else ''))
            else:
                res.append( '……' + movie['comment4'][pos - 5: pos + 67] + ('……' if pos + 67 < len(movie['comment4']) else ''))
        if movie['comment5'].find(keyword) != -1:
            pos = movie['comment5'].find(keyword)
            if pos < 5:
                res.append( movie['comment5'][:72] + ('……' if 72 < len(movie['comment5']) else ''))
            else:
                res.append( '……' + movie['comment5'][pos - 5: pos + 67] + ('……' if pos + 67 < len(movie['comment5']) else ''))
        return res
    response = request.GET
    keyword = response.get('keyword')
    option = response.get('option')
    begin = datetime.now()
    if option == 'movie':
        data = Movie.objects.filter(Q(title__contains=keyword) | Q(actors__contains=keyword)).order_by('id').values()
    elif option == 'celebrity':
        data = Celebrity.objects.filter(Q(name__contains=keyword) | Q(movies__contains=keyword)).order_by('id').values()
    else:
        data = Movie.objects.filter(Q(comment1__contains=keyword) |
                                    Q(comment2__contains=keyword) |
                                    Q(comment3__contains=keyword) |
                                    Q(comment4__contains=keyword) |
                                    Q(comment5__contains=keyword) ).order_by('id').values()
    total = len(data)
    paginator = Paginator(data, 12)
    page_number = int(request.GET.get('page', 1))
    page = paginator.get_page(page_number)
    end = datetime.now()
    cost = (end - begin).total_seconds()
    page_range = range(max(1, page_number - 2), min(paginator.num_pages, page_number + 2) + 1)
    if option == 'movie':
        return render(request, 'searchmovie.html',
                      {'posts': page, 'keyword': keyword, 'cost': cost, 'page_range': page_range,
                       'total': total, 'pagecnt': paginator.num_pages, 'pagecntminus': paginator.num_pages-1})
    elif option == 'celebrity':
        return render(request, 'searchcelebrity.html',
                      {'posts': page, 'keyword': keyword, 'cost': cost, 'page_range': page_range,
                       'total': total, 'pagecnt': paginator.num_pages, 'pagecntminus': paginator.num_pages-1})
    else:
        for each in page:
            each['brief'] = get_brief(each)
        end = datetime.now()
        cost = (end - begin).total_seconds()
        return render(request, 'searchcomment.html',
                      {'posts': page, 'keyword': keyword, 'cost': cost, 'page_range': page_range,
                       'total': total, 'pagecnt': paginator.num_pages, 'pagecntminus': paginator.num_pages-1})
