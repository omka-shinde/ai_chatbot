import React, { useState } from 'react';
import { TextField, Button, Box, Paper, Typography } from '@mui/material';
import axios from 'axios'; // To interact with the backend (API call)

const ChatbotApp = () => {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);

  // Handle sending queries to the backend
  const handleSend = async () => {
    if (!input.trim()) return; // Ignore empty messages
    setMessages([...messages, { text: input, isUser: true }]);
    try {
      // Correct backend URL (make sure it's set to the correct port)
      const response = await axios.post('http://localhost:5000/query', { query: input });
      setMessages([...messages, { text: input, isUser: true }, { text: response.data.answer, isUser: false }]);
    } catch (error) {
      setMessages([...messages, { text: input, isUser: true }, { text: 'Sorry, something went wrong. Please try again later.', isUser: false }]);
    }
    setInput('');
  };

  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', height: '100vh', justifyContent: 'flex-end' }}>
      {/* Chat Header */}
      <Paper sx={{ padding: 2 }}>
        <Typography variant="h6">Product & Supplier Chatbot</Typography>
      </Paper>

      {/* Chat History */}
      <Box sx={{ flex: 1, overflowY: 'auto', padding: 2, marginBottom: 2 }}>
        {messages.map((msg, index) => (
          <Box key={index} sx={{ display: 'flex', justifyContent: msg.isUser ? 'flex-end' : 'flex-start', marginBottom: 2 }}>
            <Paper sx={{ padding: 2, maxWidth: '60%', backgroundColor: msg.isUser ? '#3f51b5' : '#f1f1f1', color: msg.isUser ? 'white' : 'black' }}>
              <Typography>{msg.text}</Typography>
            </Paper>
          </Box>
        ))}
      </Box>

      {/* Input Box */}
      <Box sx={{ display: 'flex', padding: 2 }}>
        <TextField
          variant="outlined"
          fullWidth
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && handleSend()}
          placeholder="Type your query..."
        />
        <Button onClick={handleSend} sx={{ marginLeft: 2 }} variant="contained">Send</Button>
      </Box>
    </Box>
  );
};

export default ChatbotApp;
