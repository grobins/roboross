var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

app.get('/', function(req, res){
  res.sendfile('www/index.html');
});

//log connection
io.on('connection', function(socket){
  console.log('a user connected');
});

//logs on server
io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    console.log('message: ' + msg);
  });
});

//returns to client
io.on('connection', function(socket){
  socket.on('chat message', function(msg){
    io.emit('chat message', msg);
  });
});


http.listen(3000, function(){
  console.log('listening on *:3000');
});