<template>
  <section id="message-board" class="section">
    <div class="message-board-container">
  <div class="message-board">
    <h2>留言板</h2>
    <div class="messages">
      <div v-for="(message, index) in sortedMessages" :key="index" class="message" @click="openMessageDetail(message)">
        <div class="message-content">{{ truncateContent(message.content) }}</div>
      </div>
    </div>
    <div class="floating-button" @click="openMessageForm">+</div>
  </div>
  <div v-if="showMessageForm" class="message-form-overlay">
    <div class="message-form">
      <h3>发布新留言</h3>
      <textarea v-model="newMessageContent" placeholder="输入你的留言..."></textarea>
      <button @click="addMessage">发布留言</button>
      <button @click="closeMessageForm">取消</button>
    </div>
  </div>
  <div v-if="showMessageDetail" class="message-detail-overlay" @click="closeMessageDetail">
    <div class="message-detail" @click.stop>
      <h3>{{ detailedMessage.username }}</h3>
      <p>{{ detailedMessage.content }}</p>
      <p>{{ detailedMessage.timestamp }}</p>
      <button @click="closeMessageDetail">关闭</button>
    </div>
  </div>
</div>

</section>
</template>

<script>
export default {
name: 'MessageBoard',
data() {
  return {
    messages: [],
    newMessageContent: '',
    currentUser: JSON.parse(localStorage.getItem('currentUser'))?.username || '',
    showMessageForm: false,
    showMessageDetail: false,
    detailedMessage: {}
  };
},
computed: {
  sortedMessages() {
    return this.messages.slice().sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
  }
},
methods: {
  addMessage() {
    if (!this.newMessageContent.trim()) {
      alert('留言内容不能为空');
      return;
    }

    const newMessage = {
      username: this.currentUser || '匿名用户',
      content: this.newMessageContent,
      timestamp: new Date().toLocaleString()
    };

    this.messages.push(newMessage);
    localStorage.setItem('messages', JSON.stringify(this.messages));
    this.newMessageContent = '';
    this.showMessageForm = false;
  },
  loadMessages() {
    const savedMessages = JSON.parse(localStorage.getItem('messages'));
    if (savedMessages) {
      this.messages = savedMessages;
    }
  },
  openMessageForm() {
    if (!this.currentUser) {
      alert('请先登录');
      this.$router.push('/login');
    } else {
      this.showMessageForm = true;
    }
  },
  closeMessageForm() {
    this.showMessageForm = false;
  },
  truncateContent(content) {
    return content.length > 40 ? content.substring(0, 40) + '...' : content;
  },
  openMessageDetail(message) {
    this.detailedMessage = message;
    this.showMessageDetail = true;
  },
  closeMessageDetail() {
    this.showMessageDetail = false;
  }
},
created() {
  this.loadMessages();
}
};
</script>

<style scoped>
.message-board-container {
height: 100vh;
background: url('#') no-repeat center center fixed;
background-size: cover;
display: flex;
justify-content: center;
align-items: center;
position: relative;
}

.message-board {
width: 80%;
max-width: 800px;
background-color: white;
padding: 20px;
border-radius: 8px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
overflow-y: auto;
max-height: 80vh;
}

.messages {
margin-top: 20px;
display: flex;
flex-direction: column;
gap: 10px;
}

.message {
background-color: black;
color: white;
padding: 10px;
border-radius: 4px;
cursor: pointer;
}

.message-content {
margin-bottom: 5px;
}

.message-form-overlay, .message-detail-overlay {
position: fixed;
top: 0;
left: 0;
right: 0;
bottom: 0;
background: rgba(0, 0, 0, 0.5);
display: flex;
justify-content: center;
align-items: center;
}

.message-form, .message-detail {
background: white;
white-space: normal;  
padding: 20px;
border-radius: 8px;
box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
width: 300px;
max-width: 90%;
text-align: center;
white-space: normal; 
  overflow: auto;
}

.message-form h3, .message-detail h3 {
margin-bottom: 20px;
}

.message-form textarea {
width: 100%;
padding: 10px;
border-radius: 4px;
border: 1px solid #ddd;
box-sizing: border-box;
resize: vertical;
height: 80px;
margin-bottom: 20px;
}

.message-form button, .message-detail button {
padding: 10px 20px;
border: none;
border-radius: 4px;
background-color: #333;
color: white;
cursor: pointer;
margin: 5px;
}

.message-form button:hover, .message-detail button:hover {
background-color: #555;
}

.floating-button {
	position: fixed;
	bottom: 40px;
	right: 40px;
	width: 100px;
	height: 100px;
	background-color: #333;
	color: white;
	border-radius: 50%;
	display: flex;
	justify-content: center;
	align-items: center;
	font-size: 36px;
	cursor: pointer;
	box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
  }
</style>
