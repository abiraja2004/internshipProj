/**
 * Created by Hallshit on 6/13/17.
 */

console.log("Hi")

var searchapp = angular.module('app', []);

searchapp.controller('searchCtrl', ['$scope', function ($scope) {
    $scope.data = "theData";
    var clearbit = require('clearbit')('sk_8f708ad4e5975cdd82d69c0ba095c091');

    clearbit.Prospector.search({domain: 'twitter.com', role: 'marketing'})
  .then(function (people) {
    people.forEach(function(person){
      console.log(person.name.fullName, person.title);
    });
  })
  .catch(function (err) {
    console.error(err);
  });

}])