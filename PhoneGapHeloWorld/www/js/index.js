
// app.initialize();


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
        $scope.selectedFilters = [];

        // Send search criteria
        $scope.filterhide = true;
        $scope.submitSearch = function() {
            $('#mmap').html("")
            $('#logo').html("")
            company = $('#companyName').val()
            // var logo =  "<img src='//logo.clearbit.com/" +company + ".com'>"
            //
            //
            // $('#logo').append(logo)

            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                    if (xhr.readyState == XMLHttpRequest.DONE) {
                        results = JSON.parse(xhr.responseText)
                        console.log(JSON.parse(xhr.responseText));
                        var mmap = results['mmap']
                        var mmapElement = "<img style='max-width: 100%; max-height: 100%;'src='/img/taggedMarketMaps/"+ mmap + "'>"
                        $('#mmap').append(mmapElement)

                    }
                };
                xhr.open('POST', 'http://69609fd2.ngrok.io/api/getMarketMap', true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({"companyName": $('#companyName').val()
                                         // "role": $('#role').val(),
                                         // "seniority": $('#seniority').val(),
                                         // "title": $('#title').val(),
                                         // "employeeName": $('#employeeName').val()
                }))
            // $('#FormHeadContainer').slideUp(600);
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