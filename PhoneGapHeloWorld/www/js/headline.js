/**
 * Created by Hallshit on 6/28/17.
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
var headlineApp = angular.module('headlineApp', []);

headlineApp.controller('headlineCtrl', ['$scope', function($scope) {
    $scope.submitHeadline = function () {
        var headline = $('#headline').val();
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                console.log(xhr.responseText)
                response = xhr.responseText
                $scope.result = JSON.parse(response)
                $scope.$apply()

            }
        }
        xhr.open('POST', 'http://69609fd2.ngrok.io/tweetclf/predict/', true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify({'headline': headline}))
    };


}])

