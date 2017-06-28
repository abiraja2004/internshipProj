/**
 * Created by Hallshit on 6/21/17.
 */

var ghubApp = angular.module('ghubApp', ['ng-fusioncharts']);

ghubApp.controller('ghubCtrl', ['$scope', '$compile', function($scope, $compile) {




    $scope.submitSearch = function (){
        var company = $('#companyName').val();
        var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                    if (xhr.readyState == XMLHttpRequest.DONE) {

                        console.log(xhr.responseText);

                        $scope.commitData = xhr.responseText;
                        $afterPostData = $scope.myDataSource
                        console.log(xhr.responseText);
                        $scope.myDataSource = JSON.parse(xhr.responseText);
                        var commitChartDirective = $compile( '<fusioncharts margin: auto width="80%" height="400" type="column2d" datasource="{{myDataSource.stars}}"></fusioncharts>' )( $scope )
                        var starGrowthChartDirective = $compile('<fusioncharts class="p-5" margin=auto width="80%" height="400" type="line" datasource="{{myDataSource.starshistory}}"></fusioncharts>' )( $scope )
                        angular.element(document.querySelector( '#commitChart' )).html('');
                        angular.element(document.querySelector( '#commitChart' )).append(commitChartDirective);
                        angular.element(document.querySelector( '#commitChart' )).append(starGrowthChartDirective);
                        $scope.$apply()

                        // $compile(commitChartDirective)($scope)


                    }
                };
                xhr.open('POST', ' http://acec6fed.ngrok.io/api/commitData/', true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({'company': company}))
    }

    // $scope.myDataSource = {"data":[{"value":100,"label":"06-2016"},{"value":100,"label":"07-2016"},{"value":100,"label":"07-2016"},{"value":176,"label":"07-2016"},{"value":170,"label":"07-2016"},{"value":182,"label":"07-2016"},{"value":216,"label":"08-2016"},{"value":197,"label":"08-2016"},{"value":281,"label":"08-2016"},{"value":194,"label":"08-2016"},{"value":197,"label":"09-2016"},{"value":257,"label":"09-2016"},{"value":283,"label":"09-2016"},{"value":271,"label":"09-2016"},{"value":221,"label":"10-2016"},{"value":331,"label":"10-2016"},{"value":352,"label":"10-2016"},{"value":353,"label":"10-2016"},{"value":341,"label":"10-2016"},{"value":251,"label":"11-2016"},{"value":286,"label":"11-2016"},{"value":192,"label":"11-2016"},{"value":311,"label":"11-2016"},{"value":338,"label":"12-2016"},{"value":281,"label":"12-2016"},{"value":193,"label":"12-2016"},{"value":82,"label":"12-2016"},{"value":168,"label":"01-2017"},{"value":231,"label":"01-2017"},{"value":275,"label":"01-2017"},{"value":255,"label":"01-2017"},{"value":330,"label":"01-2017"},{"value":306,"label":"02-2017"},{"value":253,"label":"02-2017"},{"value":179,"label":"02-2017"},{"value":239,"label":"02-2017"},{"value":192,"label":"03-2017"},{"value":263,"label":"03-2017"},{"value":240,"label":"03-2017"},{"value":255,"label":"03-2017"},{"value":192,"label":"04-2017"},{"value":190,"label":"04-2017"},{"value":198,"label":"04-2017"},{"value":207,"label":"04-2017"},{"value":245,"label":"04-2017"},{"value":243,"label":"05-2017"},{"value":288,"label":"05-2017"},{"value":260,"label":"05-2017"},{"value":220,"label":"05-2017"},{"value":283,"label":"06-2017"},{"value":232,"label":"06-2017"},{"value":104,"label":"06-2017"}],"chart":{"divlineColor":"#999999","divLineGapLen":"1","xAxisLineThickness":"1","divLineIsDashed":"1","bgColor":"#ffffff","showShadow":"0","xAxisLineColor":"#999999","lineThickness":"2","baseFont":"Helvetica Neue,Arial","subcaptionFontSize":"14","divlineThickness":"1","divlineAlpha":"100","subcaptionFontBold":"0","subCaption":"Last year","baseFontColor":"#333333","showXAxisLine":"1","showAlternateHGridColor":"0","xAxisName":"Week","showBorder":"0","canvasBgColor":"#ffffff","paletteColors":"#0075c2","caption":"Commit Activity","yAxisName":"# of commits","captionFontSize":"14","divLineDashLen":"1","canvasBorderAlpha":"0"}}



}]);