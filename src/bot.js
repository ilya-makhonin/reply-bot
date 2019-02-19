const TelegramBot = require('node-telegram-bot-api');
const { start, help, answer } = require('./variables');
const { admins, token, chat } = require('./config');

let bot = new TelegramBot(token, { polling: true });

bot.onText(/\/start/, (msg) => {
  bot.sendMessage(msg.chat.id, start, {
    parse_mode: 'markdown'
  });
});

bot.onText(/\/help/, (msg) => {
  bot.sendMessage(msg.chat.id, help, {
    parse_mode: 'markdown'
  });
});

bot.on('message', (msg) => {
  bot.forwardMessage(chat, msg.chat.id, msg.message_id);
  bot.sendMessage(msg.chat.id, answer, {
    parse_mode: 'markdown'
  })
});