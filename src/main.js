const express = require('express');
// const { server_pkey, server_cert, server_list, server_port, server_host } = require('./config');

const TOKEN = process.env.TELEGRAM_TOKEN || 'YOUR_TELEGRAM_BOT_TOKEN';
const url = 'https://';
const port = process.env.PORT || 3000;

const TelegramBot = require('node-telegram-bot-api');
const bodyParser = require('body-parser');

// No need to pass any parameters as we will handle the updates with Express
const bot = new TelegramBot(TOKEN);

// This informs the Telegram servers of the new webhook.
bot.setWebHook(`${url}/bot${TOKEN}`);

const app = express();

// parse the updates to JSON
app.use(bodyParser.json());

// We are receiving updates at the route below!
app.post(`/bot${TOKEN}`, (req, res) => {
  // bot.processUpdate(req.body);
  console.log('Success!');
  res.sendStatus(200);
});

// Start Express Server
app.listen(port, () => {
  console.log(`Express server is listening on ${port}`);
});

// Just to ping!
bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, '*Hi!*', {
    parse_mode: 'markdown'
  });
});

bot.on('message', msg => {
  bot.sendMessage(msg.chat.id, 'I am alive!');
});