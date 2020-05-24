from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello, World! </h1>")
    return render(request, "pages/home.html", context={}, status=200)

def tweet_list_view(request, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    """
    REST API VIEW
    Consume by JavaScript or Swift/Java/iOS/Android
    return json data
    """
    data = {
        "id": tweet_id
    }
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data["content"] = obj.content
        status = 200
    except:
        data["message"] = "not found"
        status = 404
    return JsonResponse(data, status=status)  # json.dumps content_type='application/json'

