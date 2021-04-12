var express = require('express');
var app = express();
var fs = require("fs");

var cors = require('cors')  //to disable cors in web api
var app = express()
app.use(cors()) 

app.get('/questions', function (req, res) {
   fs.readFile( __dirname + "/" + "questions.json", 'utf8', function (err, data) {
      console.log( data );
      res.end( data );
   });
})

app.get('/results', function (req, res) {
    fs.readFile( __dirname + "/" + "results.json", 'utf8', function (err, data) {
       console.log( data );
       res.end( data );
    });
 })

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)
})