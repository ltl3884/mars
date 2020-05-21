from django.http import HttpResponse
from django.shortcuts import render
import logging
import time

from .models import User
from .dy import get_awemes

logger = logging.getLogger("django")


def index(request):
    users = User.objects.order_by('-follower_count')[:5]
    return render(request, 'video/index.html', {'users': users})


def awemes(request):
    return render(request, 'video/awemes.html', {'awemes': []})


def fetch_awemes(request, user_id):
    aweme_list = []
    max_cursor = "0"
    has_more = True
    while has_more:
        result = get_awemes(user_id, max_cursor)
        aweme_list.append(result.get("aweme_list"))
        max_cursor = result.get("max_cursor")
        has_more = result.get("has_more")
        logger.info("aweme_list size:{}, max_cursor:{}, has_more:{}".format(len(result.get("aweme_list")), max_cursor, has_more))
        time.sleep(5)
    return HttpResponse("OK")
