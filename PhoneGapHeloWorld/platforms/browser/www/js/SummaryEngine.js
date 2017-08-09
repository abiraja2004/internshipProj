/**
 * Created by Hallshit on 7/10/17.
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


// console.log(list)
// console.log(WordCloud.isSupported)
// WordCloud(document.getElementById('wordCloud'), { list: list } );

var summaryEngApp = angular.module('summaryEngApp', []);

summaryEngApp.controller('summaryEngCtrl', ['$scope', '$compile', function($scope, $compile) {
    $scope.data = "data";
    $scope.loaderBool = true;
    $scope.wcHide = true;

    //Funtion called when user submits search
    $scope.submitSearch = function () {

        $scope.loaderBool = false;

        var url = $('#url').val();

        var xhr = new XMLHttpRequest();
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == XMLHttpRequest.DONE) {
                        response = JSON.parse(xhr.responseText);

                        //WordCloud generator
                        WordCloud(document.getElementById('wordCloud'), { list: response['wCloud'], backgroundColor: 'white', shape:'diamond' } )

                        //Updates $scope
                        $scope.summaries = response['summaries'];
                        if ($scope.summaries == ""){
                            $scope.summaries = "Summary was not found"
                        }
                        $scope.loaderBool = true;
                        $scope.wcHide = false;



                        $scope.$apply()
                    }
                };

                xhr.open('POST',  "https://1c8ac5ae.ngrok.io/api/summarizerEngine", true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({'url': url}));
    }

}])
