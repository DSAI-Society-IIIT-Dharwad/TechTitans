import React, { useState, useEffect, useRef } from 'react';
import { Send, AlertCircle, CheckCircle, Scale } from 'lucide-react';
import Header from './components/Header';
import ChatMessage from './components/ChatMessage';
import TypingIndicator from './components/TypingIndicator';
import SuggestedQuestions from './components/SuggestedQuestions';
import { chatAPI } from './services/api';

function App() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [conversationId, setConversationId] = useState(null);
  const [isConnected, setIsConnected] = useState(false);
  const [documentsCount, setDocumentsCount] = useState(0);
  const [error, setError] = useState(null);
  const messagesEndRef = useRef(null);

  // Scroll to bottom of messages
  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages, isLoading]);

  // Check health on mount
  useEffect(() => {
    const checkHealth = async () => {
      try {
        const health = await chatAPI.getHealth();
        setIsConnected(health.status === 'healthy');
        setDocumentsCount(health.documents_count || 0);
        
        // Add welcome message
        if (health.vectorstore_loaded) {
          setMessages([{
            role: 'assistant',
            content: `**Welcome! 👋**\n\nI'm your AI Legal Assistant for Indian law. I can help you understand:\n\n• Indian Constitution and fundamental rights\n• Legal procedures and requirements\n• Property and inheritance laws\n• General legal guidance\n\nFeel free to ask me anything! 💬`,
            timestamp: new Date().toISOString(),
          }]);
        } else {
          setError('Knowledge base not initialized. Please run the scraper first.');
        }
      } catch (err) {
        console.error('Health check failed:', err);
        setError('Unable to connect to backend. Please ensure the server is running.');
      }
    };

    checkHealth();
  }, []);

  const handleSendMessage = async (messageText = null) => {
    const text = messageText || inputMessage.trim();
    if (!text) return;

    // Clear error
    setError(null);

    // Add user message
    const userMessage = {
      role: 'user',
      content: text,
      timestamp: new Date().toISOString(),
    };
    
    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    try {
      // Send to API
      const response = await chatAPI.sendMessage(text, conversationId);
      
      // Update conversation ID
      if (!conversationId) {
        setConversationId(response.conversation_id);
      }

      // Add assistant message
      const assistantMessage = {
        role: 'assistant',
        content: response.response,
        timestamp: new Date().toISOString(),
        sources: response.sources,
      };
      
      setMessages(prev => [...prev, assistantMessage]);
    } catch (err) {
      console.error('Error sending message:', err);
      setError('Failed to get response. Please try again.');
      
      // Add error message
      const errorMessage = {
        role: 'assistant',
        content: '❌ I apologize, but I encountered an error processing your request. Please try again.',
        timestamp: new Date().toISOString(),
      };
      setMessages(prev => [...prev, errorMessage]);
    } finally {
      setIsLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
    }
  };

  return (
    <div className="h-screen flex flex-col overflow-hidden">
      {/* Fixed Header at Top - Always Visible */}
      <div className="flex-shrink-0">
        <Header isConnected={isConnected} documentsCount={documentsCount} />
      </div>

      {/* Scrollable Content Area - Only this part scrolls */}
      <div className="flex-1 overflow-y-auto bg-gray-50">
        <div className="w-full px-12 py-4">
          {/* Error Banner */}
          {error && (
            <div className="mb-4 p-4 bg-red-50 border border-red-200 rounded-lg flex items-start gap-3">
              <AlertCircle className="text-red-600 flex-shrink-0 mt-0.5" size={20} />
              <div>
                <p className="text-red-800 font-medium">Error</p>
                <p className="text-red-600 text-sm">{error}</p>
              </div>
            </div>
          )}

          {/* Compact Welcome Message */}
          {messages.length === 0 && !isLoading && (
            <div className="text-center py-4">
              <div className="w-16 h-16 mx-auto mb-3 bg-gradient-to-br from-legal-500 to-orange-500 rounded-full flex items-center justify-center shadow-lg">
                <Scale size={32} className="text-white" />
              </div>
              <h2 className="text-4xl font-bold text-gray-800 mb-3">
                How can I help you today?
              </h2>
              <p className="text-xl text-gray-600 mb-3">
                Ask me anything about Indian law 📚
              </p>
              
              {/* Suggested Questions - Compact */}
              <div className="mt-2">
                <SuggestedQuestions onSelect={handleSendMessage} />
              </div>
            </div>
          )}

          {/* Messages */}
          {messages.map((message, index) => (
            <ChatMessage key={index} message={message} />
          ))}
          
          {/* Loading Indicator */}
          {isLoading && <TypingIndicator />}
          
          {/* Auto-scroll anchor */}
          <div ref={messagesEndRef} />
        </div>
      </div>

      {/* Fixed Input at Bottom - Always Visible */}
      <div className="flex-shrink-0 border-t-2 border-gray-200 bg-white shadow-2xl">
        <div className="w-full px-12 py-5">
          <div className="flex gap-4 items-end">
            <textarea
              value={inputMessage}
              onChange={(e) => setInputMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Type your legal question here... 💬"
              className="flex-1 resize-none border-2 border-gray-300 rounded-2xl px-6 py-4 text-xl focus:outline-none focus:ring-2 focus:ring-legal-500 focus:border-legal-500 max-h-40 transition-all shadow-md"
              rows="2"
              style={{ minHeight: '70px', fontSize: '1.25rem' }}
            />
            <button
              onClick={() => handleSendMessage()}
              disabled={!inputMessage.trim() || isLoading}
              className="bg-gradient-to-r from-legal-600 to-legal-700 text-white px-8 py-4 rounded-2xl hover:from-legal-700 hover:to-legal-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 flex items-center gap-3 font-semibold text-lg shadow-lg hover:shadow-xl"
            >
              <Send size={24} />
              <span>Send</span>
            </button>
          </div>
          
          <div className="mt-2 text-center">
            <p className="text-xs text-gray-500">
              Press <kbd className="px-1.5 py-0.5 bg-gray-100 rounded font-mono text-xs">Enter</kbd> to send • 🇮🇳 Made for India
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;

