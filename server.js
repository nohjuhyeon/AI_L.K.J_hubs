const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 3000;
app.use(bodyParser.json());

// DB 연결 및 라우트 설정
require('./db')(app);
require('./routes')(app);

app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
