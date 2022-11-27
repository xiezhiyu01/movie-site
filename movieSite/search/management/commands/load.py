from pathlib import Path
from json import load

from django.core.management.base import BaseCommand
from django.db import transaction
import xlrd

from search.models import Movie
from search.models import Celebrity


class Command(BaseCommand):

    help = 'load movies from excel'

    def handle(self, *args, **options):
        book_m = xlrd.open_workbook(r"C:\Users\XieZhiyu\PycharmProjects\movieSite\影片信息.xls")
        sheet_m = book_m.sheet_by_name("影片信息")
        book_c = xlrd.open_workbook(r"C:\Users\XieZhiyu\PycharmProjects\movieSite\演员信息.xls")
        sheet_c = book_c.sheet_by_name("演员信息")
        print(sheet_m.cell(0, 0).value)

        for i in range(4332):
            celebrity = Celebrity(name=sheet_c.cell(i, 0).value,
                                  intro=sheet_c.cell(i, 1).value,
                                  imgSrc='images/celebritypic/celebrity' + str(i) + '.jpg',
                                  gender=sheet_c.cell(i, 3).value,
                                  id=i+1,
                                  movies=str(sheet_c.cell(i, 10).value))
            celebrity.save()

        for i in range(1046):
            comments = sheet_m.cell(i, 7).value
            comments = eval(comments)
            movie = Movie(title=sheet_m.cell(i, 0).value,
                          rating=sheet_m.cell(i, 1).value,
                          summary=sheet_m.cell(i, 2).value,
                          imgSrc='images/moviepic/movie' + str(i) + '.jpg',
                          comment1=comments[0],
                          comment2=comments[1],
                          comment3=comments[2],
                          comment4=comments[3],
                          comment5=comments[4],
                          id=i+1,
                          actors=str(sheet_m.cell(i, 4).value)
                          )
            movie.save()



