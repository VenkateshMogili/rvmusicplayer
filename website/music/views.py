from django.http import HttpResponse
from django.template import loader
from .models import Album, Song

def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albums': all_albums,
    }
    return HttpResponse(template.render(context, request))
    # text="<html><head><title>Hello</title></head>"
    # text+="<style>table{width:100%;border-collapse:collapse;padding:10px;color:white;} td,th{text-align:left;padding:10px;border-bottom:1px solid lightgray}</style>"
    # text+="<body style='font-family:arial'>"
    # text+="<div style='margin-top:80px;background-color:tomato;color:white;padding:5px;border-bottom:3px solid tomato;'>"
    # text+="<h1>RV Music Player</h1></div>"
    # text+="<div style='padding:10px;color:white;background:linear-gradient(lightgray,black)'>"
    # text+="<img src='' style='border-radius:10px;float:left;margin-left:5%'><h1>Geetha Govindam</h1><p>Music By Gopi Sundar</p>"
    # text+="<table style='border-collapse:collapse'><tr><th>S.No</th><th>Title</th><th>Artist</th><th>Duration</th></tr>"
    # for album in all_albums:
    #     url =str(album.id) + '/'
    #     text += "<tr><td>"+str(album.id)+"</td><td><a href='"+url +"' style='text-decoration:none;color:white'>"+album.album_title+"</a></td><td>"+album.artist+"</td><td>04:19</td></tr>"
    # text+="</table></div>"
    # text+="<div style='padding:10px;background-color:tomato'>"
    # text+="<audio style='width:100%' controls autoplay='true' src='http://sensongsmp3.co.in/mp3/2018/Geetha%20Govindam%20(2018)/01%20-%20Inkem%20Inkem%20Inkem%20Kaavaale%20-%20SenSongsMp3.Co.mp3' type='audio/mp3'></audio>"
    # text+="</div></body></html>"


def detail(request, album_id):
    all_albumss = Song.objects.filter(id=album_id).all()
    template = loader.get_template('music/index.html')
    context = {
        'all_albumss': all_albumss,
    }
    return HttpResponse(template.render(context, request))