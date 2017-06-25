import GithubGo
import datetime


def convertData(repo):

    # repo = GithubGo.searchRepos('tensorflow', sort='stars')

    data = GithubGo.getCommitActivity(repo)
    if data == []:
        data = GithubGo.getCommitActivity(repo)

    fusiondata = {'data': []}
    for weekdata in data:
        week = datetime.datetime.fromtimestamp(int(weekdata['week'])).strftime('%m-%Y')
        commits = weekdata['total']
        print "Week: {}".format(week)
        print "Commits: {}".format(commits)
        fusiondata['data'].append({"label": week, "value": commits})

        # print fusiondata

        fusiondata['chart'] = {
            "caption": "{} commit activity".format(repo),
            "subCaption": "Last year",
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
            "showAlternateHGridColor": "0"
        }
        # fusiondata['trendlines'] = [
        #     {
        #         "line": [
        #             {
        #                 "startvalue": "18500",
        #                 "color": "#1aaf5d",
        #                 "displayvalue": "Average{br}weekly{br}footfall",
        #                 "valueOnRight": "1",
        #                 "thickness": "2"
        #             }
        #         ]
        #     }
        # ]

    return fusiondata





