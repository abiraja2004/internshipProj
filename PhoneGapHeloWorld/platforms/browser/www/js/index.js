
document.addEventListener('deviceready', onDeviceReady, false);

function onDeviceReady(){
     console.log("Device Ready")
    };


var searchApp = angular.module('searchApp', []);

    searchApp.controller('searchCtrl', ['$scope', '$http', function ($scope) {
        $scope.filters = ['companyName', 'role', 'seniority', 'title', 'employeeName'];
        $scope.selectedFilters = [];

        // Send search criteria
        $scope.submitSearch = function() {
            var xhr = new XMLHttpRequest();
            xhr.onreadystatechange = function() {
                    if (xhr.readyState == XMLHttpRequest.DONE) {
                        console.log(JSON.parse(xhr.responseText));
                    }
                };
                xhr.open('POST', ' http://acec6fed.ngrok.io/api/', true);
                xhr.setRequestHeader("Content-Type", "application/json");
                xhr.send(JSON.stringify({"companyName": $('#companyName').val(),
                                         "role": $('#role').val(),
                                         "seniority": $('#seniority').val(),
                                         "title": $('#title').val(),
                                         "employeeName": $('#employeeName').val()
                }))
            $('#FormHeadContainer').slideUp(600);
        };
        // Adds new filters
        $scope.filterSelect = function (x) {
            if ($.inArray(x, $scope.selectedFilters)> -1){
                console.log("Filter already chosen")
            }else {
                $scope.selectedFilters.push(x);
                console.log($scope.selectedFilters);
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