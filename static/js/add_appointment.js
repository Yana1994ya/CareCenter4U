    angular.module('CC4U', [])
       .controller('DoctorSelect', function($scope, $http) {
           $scope.cities = [];
           $scope.city = null;

           $scope.centers = [];
           $scope.center = null;

           $scope.doctors = [];
           $scope.doctor = null;

           $http.get("/centers/cities.json").then(
               function(success){
                   $scope.cities = success.data;
               },
               function(error){
                   alert("error loading cities:" + error);
               }
           )

           $scope.select_city = function(city){
               $scope.city = city;

               $http.get("/centers/centers.json?city=" + $scope.city.id).then(
                   function(success){
                       $scope.centers = success.data;
                   },
                   function(error){
                       alert("error loading centers:" + error);
                   }
               )
           }

           $scope.unselect_city = function(){
               $scope.city = null;
               $scope.unselect_center();
               $scope.centers = null;
           }

           $scope.select_center = function(center){
               $scope.center = center;

               $http.get("/centers/doctors.json?center=" + $scope.center.id).then(
                   function(success){
                       $scope.doctors = success.data;
                   },
                   function(error){
                       alert("error loading centers:" + error);
                   }
               )
           }

           $scope.unselect_center = function(){
               $scope.center = null;
               $scope.doctors = null;
               $scope.doctor = null;
           }

           $scope.select_doctor = function(doctor){
               $scope.doctor = doctor;
           }

           $scope.unselect_doctor = function(){
               $scope.doctor = null;
           }

           $scope.$watch('doctor', function () {
               if($scope.doctor == null){
                   document.getElementById("myform").style.display = 'none';
               } else {
                   document.getElementById("myform").style.display = 'block';
                   document.getElementById("id_doctor").value = $scope.doctor.id;
               }
           });
    });