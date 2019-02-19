/**
 * Constants for bot
 * @type { string, number }
 */

const CHAT = '';
const TOKEN = '';
const ADMINS = [
  // admin_list
];


/**
 * Constants for connecting to MySQL
 * @type { string, number }
 */

const DB_HOST = '';
const DB_PORT = 3306;
const DB_USER = '';
const DB_PASS = '';
const DB_BASE = '';


/**
 * Constants for setting web hook
 * @type { string, number }
 */

const SERVER_PKEY = '';
const SERVER_CERT = '';
const SERVER_LIST = '';
const SERVER_PORT = '';
const SERVER_HOST = '';


module.exports = function () {
    return {
      chat: CHAT,
      token: TOKEN,
      admins: ADMINS,
      db_host: DB_HOST,
      db_port: DB_PORT,
      db_user: DB_USER,
      db_pass: DB_PASS,
      db_base: DB_BASE,
      server_pkey: SERVER_PKEY,
      server_cert: SERVER_CERT,
      server_list: SERVER_LIST,
      server_port: SERVER_PORT,
      server_host: SERVER_HOST
    };
}();