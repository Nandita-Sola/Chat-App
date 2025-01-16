// chatapp/static/chat/chat.js

document.addEventListener("DOMContentLoaded", function() {
    const roomName = window.location.pathname.split('/').pop();  // Extract room name from URL
    
    // Set up the WebSocket connection
    const chatSocket = new WebSocket(
        'ws://' + window.location.host + '/ws/chat/' + roomName + '/'  // Construct the WebSocket URL
    );

    chatSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log('Message from server:', data);
        
        // Here, you can insert data into the HTML to display the chat messages
        const chatLog = document.getElementById('chat-log');
        chatLog.value += (data.message + '\n');
    };

    chatSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };

    // Sending a message when the user submits a form
    document.getElementById('chat-message-input').focus();
    document.getElementById('chat-message-input').onkeyup = function(e) {
        if (e.keyCode === 13) {  // If the "Enter" key is pressed
            const messageInputDom = document.getElementById('chat-message-input');
            const message = messageInputDom.value;
            chatSocket.send(JSON.stringify({
                'message': message
            }));
            messageInputDom.value = '';  // Clear input after sending
        }
    };
});
