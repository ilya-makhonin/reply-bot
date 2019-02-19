const express = require('express');
const bodyParser = require('body-parser');
const morgan = require('morgan');
const { token, server_port, server_host } = require('./config');


const url = `http://${server_host}:${server_port}`;
const TelegramBot = require('node-telegram-bot-api');


const bot = new TelegramBot(token);
const app = express();

bot.setWebHook(`${url}/bot${token}`);


app.set('port', server_port);
app.use(morgan('dev'));
app.use(bodyParser.json());


app.get(`/`, (req, res) => {
  console.log('Success!');
  res.sendStatus(200);
});


app.post(`/bot${token}`, (req, res) => {
  bot.processUpdate(req.body);
  res.sendStatus(200);
});


app.listen(server_port, () => {
  console.log(`Express server is listening on ${app.get('port')}`);
});



bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, '*Hi!*', {
    parse_mode: 'markdown'
  });
});

bot.on('message', msg => {
  bot.sendMessage(msg.chat.id, 'I am alive!');
});
