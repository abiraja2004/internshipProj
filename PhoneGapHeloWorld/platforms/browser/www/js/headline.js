/**
 * Created by Hallshit on 6/28/17.
 */


var headlineApp = angular.module('headlineApp', []);

headlineApp.controller('headlineCtrl', ['$scope', function($scope) {
    $scope.submitHeadline = function () {
        var headline = $('#headline').val();
        var xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function () {
            if (xhr.readyState == XMLHttpRequest.DONE) {
                console.log(xhr.responseText)
            }
        }
        xhr.open('POST', ' http://acec6fed.ngrok.io/tweetclf/predict/', true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.send(JSON.stringify({'headline': headline}))
    };


}])

