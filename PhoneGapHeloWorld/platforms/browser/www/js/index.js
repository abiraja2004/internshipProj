
// app.initialize();

// Phonegap initializer

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




var searchApp = angular.module('searchApp', []);



    searchApp.controller('searchCtrl', ['$scope', '$http', function ($scope) {
        $scope.filters = ['companyName', 'role', 'seniority', 'title', 'employeeName'];


        var loadspinner = '<div class="row mx-auto pt-5" id="loadspinner"><p class="text-center mx-auto align-middle" ng-hide="loaderBool"><i class="fa fa-spinner fa-spin" style="font-size:36px; color:white"></i></p></div>'

        //$scope declarations
        $scope.mainHide = true;
        $scope.selectedFilters = [];
        $scope.filterhide = true;

        $scope.sumloaderBool = true;
        $scope.mmaploaderBool = true;


        // API calls
        function retrieveMarketMap(company) {
            console.log(company);
            // $('#mmap').html(loadspinner);
            $('#mmap').append(loadspinner);
            var xhr = new XMLHttpRequest();
            xhr.timeout = 20000;
            console.log(xhr);
            xhr.onreadystatechange = function () {
                if (xhr.readyState == XMLHttpRequest.DONE) {
                    $scope.loaderBool = true;
                    console.log($scope.loaderBool);
                    results = JSON.parse(xhr.responseText);
                    console.log(JSON.parse(xhr.responseText));
                    var mmap = results['mmap'];
                    var mmapElement = "<img style='max-width: 100%; max-height: 100%;'src='img/" + mmap + "'>"
                    $('#mmap').html(mmapElement);
                    $scope.$apply()
                };

            };
            xhr.ontimeout = function (e) {
              alert("Request timed out.  Try again later")
            };
                xhr.open('POST', 'https://93bcd139.ngrok.io/api/getMarketMap', true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({"companyName": company}))
        } ;

       function getWordCloud(company) {
           // $('#compOver').html("");
           $('.wcloud').html("");
           $scope.summaries = "";
           $('.wcloud').append(loadspinner);
           $('#summary').append(loadspinner);
           var xhr = new XMLHttpRequest();
           xhr.timeout = 20000;
                xhr.onreadystatechange = function () {
                    if (xhr.readyState == XMLHttpRequest.DONE) {
                        $('#loadspinner').remove();
                        $('#loadspinner').remove();
                        response = JSON.parse(xhr.responseText);
                        // $('#wordCloud').removeChild()
                        //WordCloud generator
                        $('.wcloud').append('<canvas class="mx-auto" id="wordCloud"></canvas>');
                        WordCloud(document.getElementById('wordCloud'), { list: response['wCloud'], color: "white", backgroundColor: 'transparent', shape: "star" } )

                        //Updates $scope
                        $scope.summaries = response['summaries'];
                        if ($scope.summaries == ""){
                            $scope.summaries = "Summary was not found"
                        }
                        $scope.loaderBool = true;
                        $scope.wcHide = false;
                        $scope.link = response['url'];
                        $scope.domain = response['url'].substring(7);
                        $scope.$apply()
                    }
                };

            xhr.ontimeout = function (e) {
              alert("Request timed out.  Try again later")
            };


                xhr.open('POST',  "https://93bcd139.ngrok.io/api/summarizerEngine", true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({'url': company}));
       }


        //Company Search function
        $scope.submitSearch = function() {
            $scope.mainHide = false;
            // $scope.loaderBool = false;
            $('#mmap').html("")
            $('#logo').html("")
            company = $('#companyName').val()
            retrieveMarketMap(company)
            getWordCloud(company)


        };
        // Adds new filters
        $scope.filterSelect = function (x) {
            $scope.filterhide = false;
            if ($.inArray(x, $scope.selectedFilters)> -1){
                console.log("Filter already chosen")
            }else {
                $scope.selectedFilters.push(x);
                console.log($scope.selectedFilters);
                $scope.$apply

            }
        }




    }]);









// Example POST
// var xhr = new XMLHttpRequest();
// xhr.onreadystatechange = function() {
//     if (xhr.readyState == XMLHttpRequest.DONE) {
//         console.log(JSON.parse(xhr.responseText));
//     }
// };
// xhr.open('POST', 'http://a5452a51.ngrok.io/api/', true);
// xhr.setRequestHeader("Content-Type", "application/json");
// xhr.send(JSON.stringify({"text":"jfdjfeifje06/21/17fjeejff\nhfdihfeh07/2/17"}));