/**
 * Created by Hallshit on 6/16/17.
 */
var theApp = angular.module('app',[]);



theApp.controller('appCtrl', ['$scope', '$http', function ($scope, $http) {
    $scope.work = "Hello";

    // To access data:  ---->   response.key




}]);






// Example Cross Domain POST

// var xhr = new XMLHttpRequest();
//
//
// xhr.onreadystatechange = function() {
//     if (xhr.readyState == XMLHttpRequest.DONE) {
//         console.log(JSON.parse(xhr.responseText));
//     }
// };
// xhr.open('POST', 'http://e750b460.ngrok.io/api/', true);
// xhr.setRequestHeader("Content-Type", "application/json");
// xhr.send(JSON.stringify({"text":"jfdjfeifje06/21/17fjeejff\nhfdihfeh07/2/17"}));


