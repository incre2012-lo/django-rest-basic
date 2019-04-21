from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader, Context

# from .models import Person


from rest_framework import generics
from .models import Songs
from .serializers import SongsSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer


class ListSongsByArtistView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    # queryset = Entry.objects.get(pk=1)
    queryset = Songs.objects.get(artist='Rintu')
    serialized = SongsSerializer('json', queryset)
    # serializer_class = SongsSerializer

    # qs = SomeModel.objects.all()
    # qs_json = serializers.serialize('json', qs)
    # return HttpResponse(qs_json, content_type='application/json')


# def index(request):
#     return HttpResponse("This is music page.")

# def index(request):
#     personList = Person.objects.all()
#
#     context = {
#         'personList': personList,
#     }
#
#     return render(request, 'index2.html', context)




# def index1(request):
#     return HttpResponse("This is polls 2nd view.")
#
#
# def index2(request):
#     # getting our template
#     template = loader.get_template('index2.html')
#
#     # rendering the template in HttpResponse
#     return HttpResponse(template.render(({'name': 'Rintu'})))
#
#
# def index3(request):
#     # getting our template
#     template = loader.get_template('index3.html')
#
#     # rendering the template in HttpResponse
#     return HttpResponse(template.render())

