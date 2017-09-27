from django.shortcuts import render
from django.views.generic import View


class Home(View):

    def get(self, request, *args, ** kwargs):
        home_template = 'index.html'
        return render(request, home_template)
