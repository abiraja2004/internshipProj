import GithubGo
import datetime


# Benchmarks

mongoDB = {"trendlines":[{"line":[{"color":"#1aaf5d","displayvalue":"MongoDB Average 68","startvalue":"68","valueOnRight":"1","thickness":"2"}]}],"data":[{"value":129,"label":"07-2016"},{"value":108,"label":"07-2016"},{"value":106,"label":"07-2016"},{"value":103,"label":"07-2016"},{"value":106,"label":"08-2016"},{"value":104,"label":"08-2016"},{"value":89,"label":"08-2016"},{"value":99,"label":"08-2016"},{"value":90,"label":"09-2016"},{"value":98,"label":"09-2016"},{"value":107,"label":"09-2016"},{"value":82,"label":"09-2016"},{"value":65,"label":"10-2016"},{"value":59,"label":"10-2016"},{"value":55,"label":"10-2016"},{"value":62,"label":"10-2016"},{"value":54,"label":"10-2016"},{"value":73,"label":"11-2016"},{"value":51,"label":"11-2016"},{"value":27,"label":"11-2016"},{"value":54,"label":"11-2016"},{"value":81,"label":"12-2016"},{"value":65,"label":"12-2016"},{"value":34,"label":"12-2016"},{"value":20,"label":"12-2016"},{"value":33,"label":"01-2017"},{"value":50,"label":"01-2017"},{"value":44,"label":"01-2017"},{"value":56,"label":"01-2017"},{"value":38,"label":"01-2017"},{"value":33,"label":"02-2017"},{"value":44,"label":"02-2017"},{"value":40,"label":"02-2017"},{"value":58,"label":"02-2017"},{"value":69,"label":"03-2017"},{"value":42,"label":"03-2017"},{"value":59,"label":"03-2017"},{"value":89,"label":"03-2017"},{"value":79,"label":"04-2017"},{"value":57,"label":"04-2017"},{"value":82,"label":"04-2017"},{"value":74,"label":"04-2017"},{"value":69,"label":"04-2017"},{"value":27,"label":"05-2017"},{"value":79,"label":"05-2017"},{"value":81,"label":"05-2017"},{"value":54,"label":"05-2017"},{"value":100,"label":"06-2017"},{"value":86,"label":"06-2017"},{"value":109,"label":"06-2017"},{"value":64,"label":"06-2017"},{"value":9,"label":"07-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"Last year","baseFontColor":"#333333","showXAxisLine":"1","labelBinSize":"1","showAlternateHGridColor":"0","showValues":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"mongodb/mongo commit activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}
angular = {"trendlines":[{"line":[{"color":"#1aaf5d","displayvalue":"Angular Average Commits 10","startvalue":"10","valueOnRight":"1","thickness":"2"}]}],"data":[{"value":22,"label":"07-2016"},{"value":18,"label":"07-2016"},{"value":16,"label":"07-2016"},{"value":9,"label":"07-2016"},{"value":17,"label":"08-2016"},{"value":5,"label":"08-2016"},{"value":4,"label":"08-2016"},{"value":7,"label":"08-2016"},{"value":22,"label":"09-2016"},{"value":13,"label":"09-2016"},{"value":18,"label":"09-2016"},{"value":9,"label":"09-2016"},{"value":19,"label":"10-2016"},{"value":20,"label":"10-2016"},{"value":18,"label":"10-2016"},{"value":12,"label":"10-2016"},{"value":21,"label":"10-2016"},{"value":10,"label":"11-2016"},{"value":16,"label":"11-2016"},{"value":26,"label":"11-2016"},{"value":22,"label":"11-2016"},{"value":19,"label":"12-2016"},{"value":13,"label":"12-2016"},{"value":9,"label":"12-2016"},{"value":3,"label":"12-2016"},{"value":9,"label":"01-2017"},{"value":10,"label":"01-2017"},{"value":8,"label":"01-2017"},{"value":9,"label":"01-2017"},{"value":14,"label":"01-2017"},{"value":11,"label":"02-2017"},{"value":7,"label":"02-2017"},{"value":12,"label":"02-2017"},{"value":6,"label":"02-2017"},{"value":6,"label":"03-2017"},{"value":12,"label":"03-2017"},{"value":14,"label":"03-2017"},{"value":6,"label":"03-2017"},{"value":7,"label":"04-2017"},{"value":7,"label":"04-2017"},{"value":5,"label":"04-2017"},{"value":7,"label":"04-2017"},{"value":3,"label":"04-2017"},{"value":11,"label":"05-2017"},{"value":7,"label":"05-2017"},{"value":7,"label":"05-2017"},{"value":1,"label":"05-2017"},{"value":5,"label":"06-2017"},{"value":4,"label":"06-2017"},{"value":3,"label":"06-2017"},{"value":3,"label":"06-2017"},{"value":4,"label":"07-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"Last year","baseFontColor":"#333333","showXAxisLine":"1","labelBinSize":"1","showAlternateHGridColor":"0","showValues":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"angular/angular.js commit activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}
wordpress = {"trendlines":[{"line":[{"color":"#1aaf5d","displayvalue":"Wordpress Average Commits 41","startvalue":"41","valueOnRight":"1","thickness":"2"}]}],"data":[{"value":44,"label":"07-2016"},{"value":76,"label":"07-2016"},{"value":23,"label":"07-2016"},{"value":23,"label":"07-2016"},{"value":28,"label":"08-2016"},{"value":26,"label":"08-2016"},{"value":113,"label":"08-2016"},{"value":92,"label":"08-2016"},{"value":26,"label":"09-2016"},{"value":31,"label":"09-2016"},{"value":30,"label":"09-2016"},{"value":51,"label":"09-2016"},{"value":61,"label":"10-2016"},{"value":36,"label":"10-2016"},{"value":71,"label":"10-2016"},{"value":137,"label":"10-2016"},{"value":139,"label":"10-2016"},{"value":58,"label":"11-2016"},{"value":114,"label":"11-2016"},{"value":36,"label":"11-2016"},{"value":64,"label":"11-2016"},{"value":63,"label":"12-2016"},{"value":32,"label":"12-2016"},{"value":10,"label":"12-2016"},{"value":12,"label":"12-2016"},{"value":47,"label":"01-2017"},{"value":33,"label":"01-2017"},{"value":39,"label":"01-2017"},{"value":26,"label":"01-2017"},{"value":15,"label":"01-2017"},{"value":15,"label":"02-2017"},{"value":19,"label":"02-2017"},{"value":20,"label":"02-2017"},{"value":15,"label":"02-2017"},{"value":31,"label":"03-2017"},{"value":14,"label":"03-2017"},{"value":23,"label":"03-2017"},{"value":23,"label":"03-2017"},{"value":20,"label":"04-2017"},{"value":20,"label":"04-2017"},{"value":35,"label":"04-2017"},{"value":17,"label":"04-2017"},{"value":17,"label":"04-2017"},{"value":77,"label":"05-2017"},{"value":61,"label":"05-2017"},{"value":31,"label":"05-2017"},{"value":17,"label":"05-2017"},{"value":10,"label":"06-2017"},{"value":21,"label":"06-2017"},{"value":13,"label":"06-2017"},{"value":64,"label":"06-2017"},{"value":14,"label":"07-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"Last year","baseFontColor":"#333333","showXAxisLine":"1","labelBinSize":"1","showAlternateHGridColor":"0","showValues":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"WordPress/WordPress commit activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}
dockercompose = {"trendlines":[{"line":[{"color":"#1aaf5d","displayvalue":"Docker/compose Average Commits 8","startvalue":"8","valueOnRight":"1","thickness":"2"}]}],"data":[{"value":4,"label":"07-2016"},{"value":10,"label":"07-2016"},{"value":30,"label":"07-2016"},{"value":7,"label":"07-2016"},{"value":3,"label":"08-2016"},{"value":1,"label":"08-2016"},{"value":2,"label":"08-2016"},{"value":0,"label":"08-2016"},{"value":6,"label":"09-2016"},{"value":10,"label":"09-2016"},{"value":5,"label":"09-2016"},{"value":9,"label":"09-2016"},{"value":6,"label":"10-2016"},{"value":6,"label":"10-2016"},{"value":6,"label":"10-2016"},{"value":16,"label":"10-2016"},{"value":10,"label":"10-2016"},{"value":9,"label":"11-2016"},{"value":7,"label":"11-2016"},{"value":6,"label":"11-2016"},{"value":2,"label":"11-2016"},{"value":6,"label":"12-2016"},{"value":4,"label":"12-2016"},{"value":3,"label":"12-2016"},{"value":3,"label":"12-2016"},{"value":17,"label":"01-2017"},{"value":12,"label":"01-2017"},{"value":16,"label":"01-2017"},{"value":8,"label":"01-2017"},{"value":13,"label":"01-2017"},{"value":14,"label":"02-2017"},{"value":15,"label":"02-2017"},{"value":11,"label":"02-2017"},{"value":10,"label":"02-2017"},{"value":11,"label":"03-2017"},{"value":13,"label":"03-2017"},{"value":23,"label":"03-2017"},{"value":9,"label":"03-2017"},{"value":10,"label":"04-2017"},{"value":9,"label":"04-2017"},{"value":7,"label":"04-2017"},{"value":14,"label":"04-2017"},{"value":8,"label":"04-2017"},{"value":4,"label":"05-2017"},{"value":9,"label":"05-2017"},{"value":9,"label":"05-2017"},{"value":2,"label":"05-2017"},{"value":11,"label":"06-2017"},{"value":2,"label":"06-2017"},{"value":6,"label":"06-2017"},{"value":2,"label":"06-2017"},{"value":0,"label":"07-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"Last year","baseFontColor":"#333333","showXAxisLine":"1","labelBinSize":"1","showAlternateHGridColor":"0","showValues":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"docker/compose commit activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}
bms = ['mongodb/mongo', 'wordpress/wordpress']

def getBMtrendlines(repo):
    repo = GithubGo.searchRepos(repo, sort='stars')
    commitact = GithubGo.getCommitActivity(repo)
    total = 0
    for x in commitact:
        total += x['total']

    average = total / 52
    return repo['items'][0]['full_name'], average

def convertData(repo):
    # bmName, bmAverage = getBMtrendlines('angular/angular.js')
    # repo = GithubGo.searchRepos('tensorflow', sort='stars')

    data = GithubGo.getCommitActivity(repo)
    # print data
    if data == []:
        data = GithubGo.getCommitActivity(repo)
    count = 0
    fusiondata = {'data': []}
    for weekdata in data:
        week = datetime.datetime.fromtimestamp(int(weekdata['week'])).strftime('%m-%Y')
        commits = weekdata['total']
        count += commits
        print "Week: {}".format(week)
        print "Commits: {}".format(commits)
        fusiondata['data'].append({"label": week, "value": commits})

        # print fusiondata


    fusiondata['chart'] = {
            "caption": "Last Year Commit Activity",
            "subCaption": "%s" % repo['items'][0]['full_name'],
            "xAxisName": "Week",
            "yAxisName": "# of commits",
            "lineThickness": "2",
            "paletteColors": "#0075c2",
            "baseFontColor": "#333333",
            "baseFont": "Helvetica Neue,Arial",
            "captionFontSize": "14",
            "subcaptionFontSize": "14",
            "subcaptionFontBold": "0",
            "showBorder": "0",
            "bgColor": "#ffffff",
            "showShadow": "0",
            "canvasBgColor": "#ffffff",
            "canvasBorderAlpha": "0",
            "divlineAlpha": "100",
            "divlineColor": "#999999",
            "divlineThickness": "1",
            "divLineIsDashed": "1",
            "divLineDashLen": "1",
            "divLineGapLen": "1",
            "showXAxisLine": "1",
            "xAxisLineThickness": "1",
            "xAxisLineColor": "#999999",
            "showAlternateHGridColor": "0",
            "showValues": "0",
            "labelBinSize": "1"
        }
    fusiondata['trendlines'] = [
        {
            "line": [
                {
                    "startvalue": str(count/52),
                    "color": "#0075c2",
                    "displayvalue": "%s {br} Average {br} %s" %(repo['items'][0]['full_name'], str(count/52)),
                    "valueOnRight": "1",
                    "thickness": "2"
                }
            ]
        }
    ]
    for bm in bms:
        bmName, bmAverage = getBMtrendlines(bm)
        fusiondata['trendlines'].append({
            "line": [
                {
                    "startvalue": bmAverage,
                    "color": "#1aaf5d",
                    "displayvalue": "%s {br} Average {br} %s" % (bmName, bmAverage),
                    "valueOnRight": "1",
                    "thickness": "2"
                }
            ]
        })
    return fusiondata


