var io = require('socket.io')(8010);


var facturas = [];

io.on('connection', function(socket) {

    socket.on('factura_created', function(data) {
        facturas[data.index] = data.factura;

        io.emit('factura_created', data);

        console.log("Added new factura");
    });

});
