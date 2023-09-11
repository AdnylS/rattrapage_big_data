from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd

def index(request):
    dataset = "adnyls/resto-avis"
    connect_kaggle(dataset)
    return HttpResponse("Hello, world. You're at the frontend index.")


def connect_kaggle(dataset_string):
    kaggle_api = KaggleApi()
    kaggle_api.authenticate()
    kaggle_api.dataset_download_files(dataset_string)

    #load data from resto-avis.zip and save in database
    data = pd.read_csv("resto-avis.zip")
    print(data.head())
    #save data in database



def getdataresto(request):
    #load data from database
    #return data in json format
    pass

def connect_dataset():

    pass