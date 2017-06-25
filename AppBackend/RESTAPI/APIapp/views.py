from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import CommitsSetupforFusion
import GithubGo
import starsSetupforFusion


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
        repo = GithubGo.searchRepos(query=data['company'], sort='stars')
        fusionData = starsSetupforFusion.convertData(repo)
        return Response(fusionData)


