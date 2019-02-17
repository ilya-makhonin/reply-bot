const mysql = require('mysql');
const { db_host, db_port, db_user, db_pass, db_base } = require('./config');

let connection = () => mysql.createConnection({
  host     : db_host,
  port     : db_port,
  user     : db_user,
  password : db_pass,
  database : db_base
});

let check_connection = () => {
  const conn = connection();
  conn.connect(function(error) {
    if (error) {
      console.error('error connecting: ' + error.stack);
      return false;
    }
    console.log('connected as id ' + conn.threadId);
    return true;
  });
};


class Sql {
  constructor() {
    this.connection = connection;

  }

  /**
   * Methods list...
   */
}

console.log(check_connection());