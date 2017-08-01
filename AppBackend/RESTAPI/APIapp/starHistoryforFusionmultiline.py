import GithubGo
import datetime
import pandas as pd
import starhistorybenchmarks
import pdb
import numpy as np

#
def convertData(repo):
    # get first repo name in returned repo list
    print repo['items'][0]['full_name']

    # initializers
    firstCreated = ''
    currentStars = 0
    dosYearsOfStars = []

    # api for list stargazers only returns one page,
    # page contains 100 items listed in chronological order
    # so I iterate through pages
    numberOfPages = iter(range(1, 300))

    for p in numberOfPages:
        # get stargazers for current page
        stars = GithubGo.getStargazers(repo, p)

        # Here I get top date (d1) on page and bottom date (d2) on page, and check if the difference between the dates
        # If d1 - d2 is less than 1 day than I skip 5 pages and add 500 stars to total count; 500 because 100 stargazers on each page
        # if d1 - d2 greater than 1 day but less than 5 then I skip 3 pages and add 300 stars to total count
        # if d1 - d2 greater than 5 than I i skip two pages and add 200 stars
        # this repeats until 2 years of stars have been gathered limiting the amount of api calls

        try:
            topdate = datetime.datetime.strptime(stars[0]['starred_at'], '%Y-%m-%dT%H:%M:%SZ')
            print topdate
        except:
            break
        botdate = datetime.datetime.strptime(stars[-1]['starred_at'], '%Y-%m-%dT%H:%M:%SZ')
        print botdate
        if p == 1:
            currentStars += 100
            firstCreated = topdate
        if (botdate - firstCreated).days >= 704:
            print "two years reached"
            break

        if (botdate - topdate).days < 1:
            dosYearsOfStars.append({'label': botdate.strftime('%m-%y'), 'value': currentStars})
            currentStars += 500
            print dosYearsOfStars
            next(numberOfPages)
            next(numberOfPages)
            next(numberOfPages)
            next(numberOfPages)
        elif (botdate - topdate).days >= 1 and (botdate - topdate).days <= 5:
            dosYearsOfStars.append({'label': botdate.strftime('%m-%y'), 'value': currentStars})
            currentStars += 300
            print dosYearsOfStars
            next(numberOfPages)
            next(numberOfPages)
        else:
            dosYearsOfStars.append({'label': botdate.strftime('%m-%y'), 'value': currentStars})
            currentStars += 200
            next(numberOfPages)

# Resulting dataset "dosyearsofstars" gives a dataset with varying dates and starcounts
# multiline charts for fusion require same units on the x axis so the following code converts varying dates into
# 0 to 24 months (2 years)

            # stars.to_csv('/Users/Hallshit/Documents/GithubAPITests/samplestargazers.csv')
    fusionChart = {}




    fusionChart['categories'] = [{'category': [{'label': 0}]}]
    for x in range(1,25):
        fusionChart['categories'][0]['category'].append({'label': x})
        print x

    # pdb.set_trace()


    # convert into pandas dataframe

    df = pd.DataFrame(data=dosYearsOfStars)

    # groups dataframe by same dates and only keeps the highest star count

    df = df.groupby(df['label']).max()

    df.index = pd.to_datetime(df.index, format='%m-%y')
    df = df.sort_index()


    df['label'] = df.index
    # pdb.set_trace()
    # subtracts each date from the first date to get the number of months between
    # this will be the label for x axis
    df['label'] = df['label'] - df['label'].iloc[0]
    df['label'] = df['label'].apply(lambda x: round(x.days/30))
    df = df.groupby(df['label']).max()
    df = df.sort_index()
    df['label'] = df.index
    print "Original df"
    print df
    last = int(df['label'].tail(1).values[0])

    # Example dataframe at this point looks like this
    # Month  stars
    #  1       10
    #  3       20
    #  4       35
    #  8       80
    #  ..      ..
    #  20      270

    # dataframe is missing certain months so they need to estimated using this bit of code

    for x in range(0, last):
        if (df.loc[df['label'] == float(x)]).empty:

            # previous month star value
            v0 = df['value'].iloc[x-1]
            # current month star value
            v2 = df['value'].iloc[x]
            # previous month
            m0 = df['label'].iloc[x-1]
            # current month
            m1 = x
            # next month
            m2 = df['label'].iloc[x]

            # equation for estimating in between values
            value = (v0*(m2-m1) + v2*(m1-m0))/(m2-m0)

            # add value to dataframe and sort values by month
            df = df.append(pd.DataFrame([[int(value), float(x)]], columns=['value', 'label']))
            df = df.sort_values('label')

            print df

        else:
            print x


    print df

    # the rest converts dataframe to a dictionary for fusion charts

    starhistory = df.to_dict(orient='records')
    # pdb.set_trace()
    values = df.to_dict('list')['value']
    data = [{'value': values[0]}]
    for x in values[1:]:
        data.append({'value': x})
    fusionChart['dataset'] = []

    fusionChart['dataset'].append({'seriesname': repo['items'][0]['full_name'],
                                   'data': data})

    # Here are the hardcoded benchmarks for this chart
    fusionChart['dataset'].append(starhistorybenchmarks.msangular)
    fusionChart['dataset'].append(starhistorybenchmarks.msmongodb)
    fusionChart['dataset'].append(starhistorybenchmarks.mswordpress)
    fusionChart['dataset'].append(starhistorybenchmarks.msdjango)


    print fusionChart['dataset']

    # This sets up the configuration for the chart (styling, captions, etc)
    fusionChart['chart'] = {
        "caption": "First Two Year Star Growth",
        "subCaption": "{}".format(repo['items'][0]['full_name']),
        "captionFontSize": "14",
        "subcaptionFontSize": "14",
        "subcaptionFontBold": "0",
        "paletteColors": "#0075c2,#1aaf5d,#ff0000,#ff6600,#42d7f4",
        "bgcolor": "#ffffff",
        "showBorder": "0",
        "showShadow": "0",
        "showCanvasBorder": "0",
        "usePlotGradientColor": "0",
        "legendBorderAlpha": "0",
        "legendShadow": "0",
        "showAxisLines": "1",
        "showAlternateHGridColor": "0",
        "divlineThickness": "1",
        "divLineIsDashed": "1",
        "divLineDashLen": "1",
        "divLineGapLen": "1",
        "xAxisName": "Time",
        "yAxisName": "Stars",
        "showValues": "0",

    }

    return fusionChart

