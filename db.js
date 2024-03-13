const MongoClient = require('mongodb').MongoClient;

const dbUrl = 'mongodb://192.168.10.240:27017';
const dbName = 'AI_LKJ';

module.exports = function(app) {
  MongoClient.connect(dbUrl, { useUnifiedTopology: true }, (err, client) => {
    if (err) return console.log(err);
    const db = client.db(dbName);
    app.locals.db = db; // 앱 전역에서 사용할 수 있게 db 객체를 저장
  });
};
