const express = require('express');
// const { server_pkey, server_cert, server_list, server_port, server_host } = require('./config');
const TOKEN = process.env.TELEGRAM_TOKEN || 'YOUR_TELEGRAM_BOT_TOKEN';
const url = 'https://';
const port = process.env.PORT || 3000;
const TelegramBot = require('node-telegram-bot-api');
const bodyParser = require('body-parser');
const bot = new TelegramBot(TOKEN);


// bot.setWebHook(`${url}/bot${TOKEN}`);

const app = express();

app.set('port', port);
app.use(bodyParser.json());

app.get(`/`, (req, res) => {
  console.log('Success!');
  res.sendStatus(200);
});

app.post(`/bot${TOKEN}`, (req, res) => {
  // bot.processUpdate(req.body);
  console.log('Success!');
  res.sendStatus(200);
});

app.listen(port, () => {
  console.log(`Express server is listening on ${app.get('port')}`);
});


/*
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, '*Hi!*', {
    parse_mode: 'markdown'
  });
});

bot.on('message', msg => {
  bot.sendMessage(msg.chat.id, 'I am alive!');
});
*/