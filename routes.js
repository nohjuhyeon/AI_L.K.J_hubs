module.exports = function(app) {
  app.post('/api/verifyPassword', async (req, res) => {
    const { inquiryNumber, password } = req.body;
    const db = req.app.locals.db;
    try {
      const inquiryNumberInt = parseInt(inquiryNumber, 10); // 문자열을 정수로 변환
      const inquiry = await db.collection('one_on_one_CS').findOne({ "inquiryNumber": inquiryNumberInt });
      if (!inquiry) {
        return res.status(404).send({ message: 'Inquiry not found.' });
      }
      if (inquiry.password === password) {
        res.send({ isValid: true });
      } else {
        res.send({ isValid: false });
      }
    } catch (error) {
      console.error('Error:', error);
      res.status(500).send({ message: 'Server error' });
    }
  });
  
};
