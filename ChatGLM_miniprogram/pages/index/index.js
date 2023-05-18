//index.js
const app = getApp()

Page({
  data: {
    dialogList: [],
  },

  sendMessage(e) {
    const value = e.detail.value;
    if (!value) {
      return;
    }

    this.setData({
      dialogList: [
        ...this.data.dialogList,
        {type: 'user', content: value}
      ]
    });

    wx.request({
      //url: 'http://192.168.31.133:1722',
      url: 'http://172.30.7.253:1722',
      method: 'POST',
      header: {'Content-Type': 'application/json'},
      data: JSON.stringify({
        prompt: value,
        // history: this.data.dialogList.map(item => item.content)
        history: []
      }),
      success: (res) => {
        const data = res.data;
        this.setData({
          dialogList: [
            ...this.data.dialogList,
            {type: 'robot', content: data.response}
          ]
        });
      }
    });

    e.detail.value = '';
  },
})
