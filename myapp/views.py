from django.http import HttpResponse
from django.shortcuts import render
import logging

# Create your views here.

logger = logging.getLogger(__name__)
log_format = "%(asctime)s - %(message)s"
logging.basicConfig(
    format=log_format,
    level=logging.INFO,
    handlers=[logging.FileHandler("django.log", mode="w+")],
)

def index(request):
    logger.info("visiting 'main page'")
    html = """
    <html>
    <head>
        <title>Главная страница</title>
    </head>
    <body>
        <h1>Добро пожаловать!</h1>
        <p>Это гланая страница первого задания по "Django".</p>
    </body>
    </html>
    """
    return HttpResponse(html)


def about(request):
    logger.info('visiting the site "About us"')
    html = """
    <html>
    <head>
        <title>О себе</title>
    </head>
    <body>
        <h1>О себе</h1>
        <p>1994 года рождения высшее образование по направлению электроэнергетика и электротехника профиль Электропривод и Автоматика.На данный момент студент Geekbrains мечтающий отучиться и найти себе новую интересную работу.</p>
    </body>
    </html>
    """
    return HttpResponse(html)
