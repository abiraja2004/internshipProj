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
import TextSummaryEngine
import GithubScrapeTrending
import GetLogo
import LogoFromDatabase
import os







# Create your views here.

def home(request):
    return render(request, 'home.html')

class topContribFollowerData(APIView):

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

class summarizerEngine(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        company = data["url"]

        print data
        returnData = {}
        text = TextSummaryEngine.getTextFromURL(company)
        wCloud = TextSummaryEngine.convertToWordCloud(text)
        # print wCloud
        returnData['wCloud'] = wCloud
        returnData['summaries'] = []
        returnData['summaries'].append({'sumySummary': TextSummaryEngine.sumySummarize(url)})
        returnData['summaries'].append({'algortithmiaSummary': TextSummaryEngine.algorithmiaSummarizer(text)})
        returnData['summaries'].append({'nltkSummary': TextSummaryEngine.nltkSummarize(text)})



        return Response(returnData)

class ghubTrending(APIView):
    def get(self, request):
        trending = GithubScrapeTrending.scrapeTrending()
        returnData = {}
        returnData['trending'] = GithubScrapeTrending.setupTrendingDict()
        return Response(returnData)



    def post(self, request):
        pass


class getMarketMap(APIView):
    def get(self, request):
        pass

    def post(self, request):
        data = request.data
        company = data['companyName']
        mmap = LogoFromDatabase.getMapFromLogo(company)
        data = {'mmap': mmap}
        return Response(data)




