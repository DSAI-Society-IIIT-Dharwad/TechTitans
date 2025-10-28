import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const chatAPI = {
  // Send a chat message
  sendMessage: async (message, conversationId = null) => {
    const response = await api.post('/chat', {
      message,
      conversation_id: conversationId,
    });
    return response.data;
  },

  // Get health status
  getHealth: async () => {
    const response = await api.get('/health');
    return response.data;
  },

  // Initialize vectorstore
  initialize: async () => {
    const response = await api.post('/initialize');
    return response.data;
  },

  // Get statistics
  getStats: async () => {
    const response = await api.get('/stats');
    return response.data;
  },
};

export default api;

