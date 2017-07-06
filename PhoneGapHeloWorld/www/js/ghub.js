/**
 * Created by Hallshit on 6/21/17.
 */

var app = {
    // Application Constructor
    initialize: function() {
        this.bindEvents();
    },
    // Bind Event Listeners
    //
    // Bind any events that are required on startup. Common events are:
    // 'load', 'deviceready', 'offline', and 'online'.
    bindEvents: function() {
        document.addEventListener('deviceready', this.onDeviceReady, false);
    },
    // deviceready Event Handler
    //
    // The scope of 'this' is the event. In order to call the 'receivedEvent'
    // function, we must explicitly call 'app.receivedEvent(...);'
    onDeviceReady: function() {
        app.receivedEvent('deviceready');
    },
    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }

};

var ghubApp = angular.module('ghubApp', ['ng-fusioncharts']);

ghubApp.controller('ghubCtrl', ['$scope', '$compile', function($scope, $compile) {

    $scope.submitSearch = function (){
        angular.element(document.querySelector( '#chartsdiv' )).html('');
        var company = $('#companyName').val();
        $('#companyName').blur();

         // Last year commit activity request
        var commitxhr = new XMLHttpRequest();
            commitxhr.onreadystatechange = function() {
                if (commitxhr.readyState == XMLHttpRequest.DONE) {
                    console.log(commitxhr.responseText)
                    $scope.commitChartData = JSON.parse(commitxhr.responseText);
                    var commitChartDirective = $compile('<div class="row mx-auto"><fusioncharts margin: auto  height="400" width="100%" type="line" datasource="{{commitChartData.commit52}}"></fusioncharts></div>')($scope);
                    angular.element(document.querySelector('#chartsdiv')).append(commitChartDirective);
                    $scope.$apply()
                }
            };
            commitxhr.open('POST', 'http://ff3e99ad.ngrok.io/api/commitData/', true);
            commitxhr.setRequestHeader("Content-Type", "application/json");
            commitxhr.send(JSON.stringify({'company': company}));

                        // console.log(commitxhr.responseText);

        // First two year Star growth request
        var stargxhr = new XMLHttpRequest();
            stargxhr.onreadystatechange = function() {
                if (stargxhr.readyState == XMLHttpRequest.DONE) {
                    console.log(JSON.parse(stargxhr.responseText));
                    $scope.starGChartData = JSON.parse(stargxhr.responseText);
                    var starGChartDirective = $compile('<div class="row mx-auto" width="100vw"><fusioncharts margin: auto  height="400" width="175%" type="msline" datasource="{{starGChartData.starshistory}}"></fusioncharts></div>')($scope);
                    angular.element(document.querySelector('#chartsdiv')).append(starGChartDirective);
                    $scope.$apply()
                }
            };
            stargxhr.open('POST', 'http://ff3e99ad.ngrok.io/api/starGrowth/', true);
            stargxhr.setRequestHeader("Content-Type", "application/json");
            stargxhr.send(JSON.stringify({'company': company}))

        //  Total Stars
        var totalStarsxhr = new XMLHttpRequest();
            totalStarsxhr.onreadystatechange = function() {
                if (totalStarsxhr.readyState == XMLHttpRequest.DONE) {
                    console.log(totalStarsxhr.responseText)
                    $scope.totalStarsChartData = JSON.parse(totalStarsxhr.responseText);
                    var totalStarsChartDirective = $compile('<div class="row mx-auto" width="100vw"><fusioncharts margin: auto  height="400" width="150%" type="column2d" datasource="{{totalStarsChartData.totalStars}}"></fusioncharts></div>')($scope);
                    angular.element(document.querySelector('#chartsdiv')).append(totalStarsChartDirective);
                    $scope.$apply()
                }
            };
            totalStarsxhr.open('POST', 'http://ff3e99ad.ngrok.io/api/totalStars/', true);
            totalStarsxhr.setRequestHeader("Content-Type", "application/json");
            totalStarsxhr.send(JSON.stringify({'company': company}));


        var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                    if (xhr.readyState == XMLHttpRequest.DONE) {

                        // console.log(xhr.responseText);

                        $scope.commitData = xhr.responseText;
                        $afterPostData = $scope.myDataSource
                        // console.log(xhr.responseText);
                        $scope.myDataSource = JSON.parse(xhr.responseText);
                        // var commitChartDirective = $compile( '<div class="row mx-auto" width="100vw"><div class="col"><fusioncharts margin: auto  height="400" width="125%" type="line" datasource="{{myDataSource.commit52}}"></fusioncharts></div></div>' )( $scope );
                        // var starGrowthChartDirective = $compile('<div class="row" width="100vw"><div class="col mx-auto"><fusioncharts class="p-5" margin=auto width="125%" height="400" type="msline" datasource="{{myDataSource.starshistory}}"></fusioncharts></div></div>' )( $scope );
                        // var TotalStarDirective = $compile('<div class="row" width="100vw"><div class="col"><fusioncharts class="p-5" margin=auto width="125%" height="400" type="column2d" datasource="{{myDataSource.totalstars}}"></fusioncharts></div></div>' )( $scope );
                        var TopContribFDirective = $compile('<div class="row" width="100vw"><fusioncharts class="p-5" margin=auto width="150%" height="400" type="column2d" datasource="{{myDataSource.topContribFollowers}}"></fusioncharts></div>' )( $scope );

                        // angular.element(document.querySelector( '#chartsdiv' )).append(commitChartDirective);
                        // angular.element(document.querySelector( '#chartsdiv' )).append(starGrowthChartDirective);
                        // angular.element(document.querySelector( '#chartsdiv' )).append(TotalStarDirective);
                        angular.element(document.querySelector( '#chartsdiv' )).append(TopContribFDirective);
                        $scope.$apply()

                        // $compile(commitChartDirective)($scope)


                    }
                };
                xhr.open('POST', 'http://ff3e99ad.ngrok.io/api/allData/', true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({'company': company}))
    }

    $scope.myDataSource = {"data":[{"value":100,"label":"06-2016"},{"value":100,"label":"07-2016"},{"value":100,"label":"07-2016"},{"value":176,"label":"07-2016"},{"value":170,"label":"07-2016"},{"value":182,"label":"07-2016"},{"value":216,"label":"08-2016"},{"value":197,"label":"08-2016"},{"value":281,"label":"08-2016"},{"value":194,"label":"08-2016"},{"value":197,"label":"09-2016"},{"value":257,"label":"09-2016"},{"value":283,"label":"09-2016"},{"value":271,"label":"09-2016"},{"value":221,"label":"10-2016"},{"value":331,"label":"10-2016"},{"value":352,"label":"10-2016"},{"value":353,"label":"10-2016"},{"value":341,"label":"10-2016"},{"value":251,"label":"11-2016"},{"value":286,"label":"11-2016"},{"value":192,"label":"11-2016"},{"value":311,"label":"11-2016"},{"value":338,"label":"12-2016"},{"value":281,"label":"12-2016"},{"value":193,"label":"12-2016"},{"value":82,"label":"12-2016"},{"value":168,"label":"01-2017"},{"value":231,"label":"01-2017"},{"value":275,"label":"01-2017"},{"value":255,"label":"01-2017"},{"value":330,"label":"01-2017"},{"value":306,"label":"02-2017"},{"value":253,"label":"02-2017"},{"value":179,"label":"02-2017"},{"value":239,"label":"02-2017"},{"value":192,"label":"03-2017"},{"value":263,"label":"03-2017"},{"value":240,"label":"03-2017"},{"value":255,"label":"03-2017"},{"value":192,"label":"04-2017"},{"value":190,"label":"04-2017"},{"value":198,"label":"04-2017"},{"value":207,"label":"04-2017"},{"value":245,"label":"04-2017"},{"value":243,"label":"05-2017"},{"value":288,"label":"05-2017"},{"value":260,"label":"05-2017"},{"value":220,"label":"05-2017"},{"value":283,"label":"06-2017"},{"value":232,"label":"06-2017"},{"value":104,"label":"06-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"Last year","baseFontColor":"#333333","showXAxisLine":"1","showAlternateHGridColor":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"Commit Activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}
    $scope.commit52 = {"trendlines":[{"line":[{"color":"#0075c2","displayvalue":"neo4j/neo4j {br} Average {br} 98","startvalue":"98","valueOnRight":"1","thickness":"2"}]},{"line":[{"color":"#1aaf5d","displayvalue":"mongodb/mongo {br} Average {br} 68","startvalue":68,"valueOnRight":"1","thickness":"2"}]},{"line":[{"color":"#1aaf5d","displayvalue":"WordPress/WordPress {br} Average {br} 41","startvalue":41,"valueOnRight":"1","thickness":"2"}]}],"data":[{"value":97,"label":"07-2016"},{"value":96,"label":"07-2016"},{"value":44,"label":"07-2016"},{"value":54,"label":"07-2016"},{"value":83,"label":"08-2016"},{"value":112,"label":"08-2016"},{"value":140,"label":"08-2016"},{"value":135,"label":"08-2016"},{"value":150,"label":"09-2016"},{"value":187,"label":"09-2016"},{"value":128,"label":"09-2016"},{"value":156,"label":"09-2016"},{"value":134,"label":"10-2016"},{"value":121,"label":"10-2016"},{"value":124,"label":"10-2016"},{"value":102,"label":"10-2016"},{"value":78,"label":"10-2016"},{"value":65,"label":"11-2016"},{"value":65,"label":"11-2016"},{"value":95,"label":"11-2016"},{"value":63,"label":"11-2016"},{"value":71,"label":"12-2016"},{"value":82,"label":"12-2016"},{"value":94,"label":"12-2016"},{"value":36,"label":"12-2016"},{"value":127,"label":"01-2017"},{"value":135,"label":"01-2017"},{"value":140,"label":"01-2017"},{"value":138,"label":"01-2017"},{"value":106,"label":"01-2017"},{"value":66,"label":"02-2017"},{"value":135,"label":"02-2017"},{"value":128,"label":"02-2017"},{"value":95,"label":"02-2017"},{"value":170,"label":"03-2017"},{"value":146,"label":"03-2017"},{"value":115,"label":"03-2017"},{"value":90,"label":"03-2017"},{"value":107,"label":"04-2017"},{"value":66,"label":"04-2017"},{"value":83,"label":"04-2017"},{"value":49,"label":"04-2017"},{"value":48,"label":"04-2017"},{"value":39,"label":"05-2017"},{"value":95,"label":"05-2017"},{"value":116,"label":"05-2017"},{"value":109,"label":"05-2017"},{"value":42,"label":"06-2017"},{"value":97,"label":"06-2017"},{"value":54,"label":"06-2017"},{"value":89,"label":"06-2017"},{"value":12,"label":"07-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"neo4j/neo4j","baseFontColor":"#333333","showXAxisLine":"1","labelBinSize":"1","showAlternateHGridColor":"0","showValues":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"Last Year Commit Activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}


}]);