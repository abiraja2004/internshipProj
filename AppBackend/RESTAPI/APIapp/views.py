from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import CommitsSetupforFusion
import GithubGo
import totalStarsSetupforFusion
import StarsHistoryForFusion
import nltkclfpickle
import starhistorybenchmarks
import starHistoryforFusionmultiline
import topContribsFollowersforFusion







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
        # print repo
        # fusionData['totalstars'] = totalStarsSetupforFusion.convertData(repo)
        # fusionData['commit52'] = CommitsSetupforFusion.convertData(repo)
        # fusionData['starshistory'] = StarsHistoryForFusion.convertData(repo)
        # fusionData['starshistory'] = starHistoryforFusionmultiline.convertData(repo)
        fusionData['benchmarks'] = starhistorybenchmarks.getStarHistoryBenchmarks()
        fusionData['topContribFollowers'] = topContribsFollowersforFusion.convertData(repo)

        return Response(fusionData)

class tweetclf(APIView):
    def get(self,request):
        pass

    def post(self, request):
        data = request.data
        headline = data['headline']
        json = nltkclfpickle.hamorspam(headline)
        return Response(json)


class commit52(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        fusionData = {}
        repo = GithubGo.searchRepos(query=data['company'], sort='stars')
        fusionData['commit52'] = CommitsSetupforFusion.convertData(repo)
        return Response(fusionData)

class starGrowth(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        fusionData = {}
        repo = GithubGo.searchRepos(query=data['company'], sort='stars')
        fusionData['starshistory'] = starHistoryforFusionmultiline.convertData(repo)
        return Response(fusionData)

class totalStars(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        fusionData = {}
        repo = GithubGo.searchRepos(query=data['company'], sort='stars')
        fusionData['totalStars'] = totalStarsSetupforFusion.convertData(repo)
        return Response(fusionData)

