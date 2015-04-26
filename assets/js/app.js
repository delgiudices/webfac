var server = io.connect('http://localhost:8010');
var facturacion = angular.module('facturacion', []);

facturacion.config(function($interpolateProvider) {
  $interpolateProvider.startSymbol('{$');
  $interpolateProvider.endSymbol('$}');
});

facturacion.controller('FacturacionCtrl', function($scope) {

  $scope.facturas = [];

  $scope.crear_factura = function() {
    var nuevo_numero = 0;

    while ( $scope.facturas[nuevo_numero] != undefined )
      nuevo_numero++;

    $scope.facturas[nuevo_numero] = { numero : nuevo_numero };
    server.emit('factura_created', { factura : $scope.facturas[nuevo_numero], index : nuevo_numero });

  }

  server.on('factura_created', function(data) {
      if ( $scope.facturas[data.index] == undefined || $scope.facturas[data.index] == null ) {
        $scope.$apply(function(){
          $scope.facturas[data.index] = data.factura;
        });
      }
  });

  $scope.agregar_articulo = function() {
    var articulos = $scope.facturas[$scope.factura_seleccionada].articulos;

    if ( articulos == undefined ) {
      $scope.facturas[$scope.factura_seleccionada].articulos = {};
    }

    var array = $scope.articulo_seleccionado.split(':');
    var pk = array[0];
    var precio = array[1];
    var nombre = array[2];

    $scope.facturas[$scope.factura_seleccionada].articulos[pk] = { nombre : array[2], precio : array[1], cantidad : $scope.cantidad };
  }



});


server.on('event', function(data){
    alert(data.data);
});
