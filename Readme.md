# ios
iPhone App

APPBACKEND - Holds the Django API framework
======================================================================================

  url routes located in [RESTAPI/RESTAPI/urls.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/RESTAPI/urls.py)

  views are located in [RESTAPI/APIapp/views.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/views.py)




clearbit analysis view (tab1)
----------------------------
Nothing is hooked up here yet since there is no clearbit account but the code for this is located in [/KnowledgeVC/competition](https://github.com/Knowledgevc-org/ios/tree/master/competition/competition)


Github analysis view (tab2)
----------------------------
* [APIapp/GithubGo.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/GithubGo.py) - this is main file that contains functions for github api calls (search repos, get stars, commmits, followers)


* On startup: shows a trending repository feed that is scraped using beautifulSoup;
    script is located in [APIapp/GithubScrapeTrending.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/GithubScrapeTrending.py)


### CHARTS



Clicking on one of trending repo or searching for repo displays 4 charts:


///// ALL CHARTS ARE MADE USING FUSIONCHARTS.JS for angular /////////

[Angular Fusion Charts](Documentation]http://www.fusioncharts.com/angularjs-charts/)

#### 52 week Commit activity line graph

* route = "api/commmitData"

* view = [views.py/commit52](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/views.py)

* created using github api "statistics"
[Documentation](https://developer.github.com/v3/repos/statistics/#get-the-last-year-of-commit-activity-data)

* Data is then parsed to format usable by fusion charts using [CommitsSetupforFusion.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/CommitsSetupforFusion.py)

#### Top 5 contributors follower count bar chart

* route = "api/topContribFollowers/"

* view = [views.py/topContribFollowerData](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/views.py)

* created using github api "statistics"
[Documentation](https://developer.github.com/v3/repos/statistics/#get-contributors-list-with-additions-deletions-and-commit-counts)

* Data is parsed, sorted using pandas, and set up for fusioncharts in the script called [topContribsFollowersforFusion.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/topContribsFollowersforFusion.py)

#### Total Stars bar chart

* route = "api/totalStars/"

* view = [views.py/totalStars](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/views.py)

* created using github api "search/repositories"
[Documentation](https://developer.github.com/v3/search/#search-repositories)

* json returned provides star count and is set up for fusioncharts using [totalStarsSetupforFusion.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/totalStarsSetupforFusion.py)

#### Initial two year star growth multiline chart

* route = "api/starGrowth/"

* view = [views.py/starGrowth](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/views.py)

* created using github api "list-stargazers"
[Documentation](https://developer.github.com/v3/activity/starring/#list-stargazers)

* Most complicated chart so I will add additional documentation to the [starHistoryforFusionmultiline.py](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/starHistoryforFusionmultiline.py)
to explain how data is obtained and parsed for fusionCharts



Summary Engine view (tab4)
--------------------------

* route = "api/summarizerEngine/"

* view = [views.py/summarizerEngine](https://github.com/Knowledgevc-org/ios/blob/master/AppBackend/RESTAPI/APIapp/views.py)

* View sends data to TextSummaryEngine.py which will return 3 different summaries and word cloud data:

* url's text are scraped using beautifulSoup except for nltk which has its own html parser

### Sumy (the best one imo):

* python github project located [here](https://github.com/miso-belica/sumy)


### nltk:

* code found [here](http://glowingpython.blogspot.com/2014/09/text-summarization-with-nltk.html)


### algorithmia:

* docs [here](https://algorithmia.com/algorithms/nlp/Summarizer)

### Word Cloud

* uses google cloud nlp to come up with most common phrases/words and its importance (salience)

code example:

    def analyzeText(text):
        client = language.Client()
        document = client.document_from_text(text)
        sent_analysis = document.analyze_sentiment()
        sentiment = sent_analysis.sentiment
        ent_analysis = document.analyze_entities()
        entities = ent_analysis.entities
        return sentiment, entities


    def convertToWordCloud(text):
        wordCloudList = []
        sent, ent = analyzeText(text)
        for e in ent:
            wordCloudList.append([e.name, e.salience*1500])
        return wordCloudList


wordCloudList is then returned to front end for word cloud rendering




PhoneGapHeloWorld - Holds the front end work
======================================================================================

Only directory that matters is [/www/](https://github.com/Knowledgevc-org/ios/tree/master/PhoneGapHeloWorld/www)
Here you'll find all the html, css and javascript files, as well as any dependencies

Note on js for phonegap:
Each js file contains var "app" object that sets up the phonegap app and needs to be initialized.  JS will work
in development mode but will not work in a mobile app without this initialization

All api calls are made through XMLHttpRequest() because angular.post would not work with the django back end




Index.html = clearbit analysis view
-----------------------------------



ghub.html = github analysis view
--------------------------------

css: [css/ghub.css](https://github.com/Knowledgevc-org/ios/blob/master/PhoneGapHeloWorld/www/css/ghub.css)

js: [js/ghub.js](https://github.com/Knowledgevc-org/ios/blob/master/PhoneGapHeloWorld/www/js/ghub.js)
* dependencies:
    - fusioncharts for angular - [docs](http://www.fusioncharts.com/angularjs-charts/#/demos/ex1)
    - located in js/bower_components




Headline.html = test page for Oscar's Ham/spam
----------------------------------------------
css: [headline.css](https://github.com/Knowledgevc-org/ios/blob/master/PhoneGapHeloWorld/www/css/headline.css)

js: [js/headline.js](https://github.com/Knowledgevc-org/ios/blob/master/PhoneGapHeloWorld/www/js/headline.js)
* dependencies:
    - None yet


SummaryEngine.html = Company main page summarizer
-------------------------------------------------
css: [css/SummaryEngine.css](https://github.com/Knowledgevc-org/ios/blob/master/PhoneGapHeloWorld/www/css/summaryEngine.css)

js: [js/summaryEngine.js](https://github.com/Knowledgevc-org/ios/blob/master/PhoneGapHeloWorld/www/js/summaryEngine.js)
* dependencies:
    - wordCloud2.js - [docs at github](https://github.com/timdream/wordcloud2.js/)
    - located in js/











