const mysql = require('mysql');
const { db_host, db_port, db_user, db_pass, db_base } = require('./config');

let connection = mysql.createConnection({
  host     : db_host,
  port     : db_port,
  user     : db_user,
  password : db_pass,
  database : db_base
});

connection.connect(function(err) {
  if (err) {
    console.error('error connecting: ' + err.stack);
    return;
  }
  console.log('connected as id ' + connection.threadId);
});