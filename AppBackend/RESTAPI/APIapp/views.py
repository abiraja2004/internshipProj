from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import CommitsSetupforFusion
import GithubGo
import starsSetupforFusion
import StarsHistoryForFusion
import nltkclfpickle




# Create your views here.

def home(request):
    return render(request, 'home.html')

class commitData(APIView):

    # send data back as JSON

    def get(self, request):

        data = {'data': 'someData'}


        print data

        return Response(data)

    # to access data:       request.data[key]

    def post(self, request):
        print "Post called"
        data = request.data
        fusionData = {}
        repo = GithubGo.searchRepos(query=data['company'], sort='stars')
        fusionData['stars'] = starsSetupforFusion.convertData(repo)
        fusionData['starshistory'] = StarsHistoryForFusion.convertData(repo)
        return Response(fusionData)

class tweetclf(APIView):
    def get(self,request):
        pass

    def post(self, request):
        data = request.data
        headline = data['headline']
        prob, label = nltkclfpickle.hamorspam(headline)
        json = {}
        json['prob'] = prob
        json['label'] = label
        return Response(json)





