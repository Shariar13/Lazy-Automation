from importlib.resources import path
from django.shortcuts import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import UpdateView
from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def home(request):
    return render (request, "index.html")

def virtual_assistant (request):
    return render (request, "virtual_assistant.html")

def search_youtube (request):
    if request.method == "POST":
        video = request.POST ['search']
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.youtube.com/results?search_query={}'.format(str(video)))
    return render (request, "virtual_assistant.html")



    

    # # play the video
    # wait.until(visible((By.ID, "video-title")))
    # driver.find_element_by_id("video-title").click()