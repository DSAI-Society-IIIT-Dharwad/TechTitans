import { useState, useRef, useEffect } from 'react';
import axios from 'axios';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Scale, Send, BookOpen, Shield, FileText, Loader2, ArrowLeft, User, LogOut } from 'lucide-react';
import ChatMessage from './components/ChatMessage';
import TypingIndicator from './components/TypingIndicator';
import SuggestedQuestions from './components/SuggestedQuestions';
import Sidebar from './components/Sidebar';
import Login from './components/Login';
import Signup from './components/Signup';

function App() {
  const [user, setUser] = useState(null);
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  const [authView, setAuthView] = useState('login'); // 'login' or 'signup'
  const [conversations, setConversations] = useState([]);
  const [currentConversationId, setCurrentConversationId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const [showChat, setShowChat] = useState(false);
  const [showUserMenu, setShowUserMenu] = useState(false);
  const messagesEndRef = useRef(null);

  // Check for existing session on mount
  useEffect(() => {
    const currentUser = JSON.parse(localStorage.getItem('currentUser') || 'null');
    if (currentUser) {
      setUser(currentUser);
      setIsAuthenticated(true);
      
      // Load conversations for this user
      loadConversations(currentUser.id);
    }
  }, []);

  // Load conversations from localStorage
  const loadConversations = (userId) => {
    const allConversations = JSON.parse(localStorage.getItem('conversations') || '[]');
    const userConversations = allConversations.filter(conv => conv.userId === userId);
    setConversations(userConversations.sort((a, b) => b.timestamp - a.timestamp));
  };

  // Save conversation to localStorage
  const saveConversation = () => {
    if (!currentConversationId || messages.length === 0) return;

    const allConversations = JSON.parse(localStorage.getItem('conversations') || '[]');
    const existingIndex = allConversations.findIndex(conv => conv.id === currentConversationId);
    
    const conversationData = {
      id: currentConversationId,
      userId: user.id,
      messages: messages,
      timestamp: Date.now(),
      title: messages.find(m => m.sender === 'user')?.text.substring(0, 40) || 'New Conversation'
    };

    if (existingIndex !== -1) {
      allConversations[existingIndex] = conversationData;
    } else {
      allConversations.push(conversationData);
    }

    localStorage.setItem('conversations', JSON.stringify(allConversations));
    loadConversations(user.id);
  };

  // Auto-save conversation when messages change
  useEffect(() => {
    if (messages.length > 0 && currentConversationId) {
      saveConversation();
    }
  }, [messages]);

  // Close user menu when clicking outside
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (showUserMenu && !event.target.closest('.user-menu-container')) {
        setShowUserMenu(false);
      }
    };

    document.addEventListener('mousedown', handleClickOutside);
    return () => {
      document.removeEventListener('mousedown', handleClickOutside);
    };
  }, [showUserMenu]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (text = input) => {
    if (!text.trim()) return;

    const userMessage = { sender: 'user', text: text };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await axios.post('http://localhost:8000/api/chat', { message: text });
      const botMessage = { sender: 'bot', text: response.data.response, sources: response.data.sources };
      setMessages((prevMessages) => [...prevMessages, botMessage]);
    } catch (error) {
      console.error('Error sending message:', error);
      setMessages((prevMessages) => [
        ...prevMessages,
        { sender: 'bot', text: 'Sorry, I am having trouble connecting to the server. Please try again later.' },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const handleSuggestedQuestionClick = (question) => {
    // Create new conversation if none exists
    if (!currentConversationId) {
      const newConvId = `conv_${Date.now()}`;
      setCurrentConversationId(newConvId);
    }
    setShowChat(true);
    // Wait for next tick to ensure chat is shown
    setTimeout(() => handleSendMessage(question), 100);
  };

  const handleLoginSuccess = (userData) => {
    setUser(userData);
    setIsAuthenticated(true);
    localStorage.setItem('currentUser', JSON.stringify(userData));
    loadConversations(userData.id);
  };

  const handleSignupSuccess = (userData) => {
    setUser(userData);
    setIsAuthenticated(true);
    localStorage.setItem('currentUser', JSON.stringify(userData));
    loadConversations(userData.id);
  };

  const handleLogout = () => {
    setUser(null);
    setIsAuthenticated(false);
    setShowChat(false);
    setMessages([]);
    setConversations([]);
    setCurrentConversationId(null);
    localStorage.removeItem('currentUser');
    setShowUserMenu(false);
  };

  const handleNewChat = () => {
    const newConvId = `conv_${Date.now()}`;
    setCurrentConversationId(newConvId);
    setMessages([]);
    setShowChat(true);
  };

  const handleSelectConversation = (convId) => {
    const allConversations = JSON.parse(localStorage.getItem('conversations') || '[]');
    const conversation = allConversations.find(conv => conv.id === convId);
    
    if (conversation) {
      setCurrentConversationId(convId);
      setMessages(conversation.messages || []);
      setShowChat(true);
    }
  };

  const handleDeleteConversation = (convId) => {
    const allConversations = JSON.parse(localStorage.getItem('conversations') || '[]');
    const filteredConversations = allConversations.filter(conv => conv.id !== convId);
    localStorage.setItem('conversations', JSON.stringify(filteredConversations));
    
    loadConversations(user.id);
    
    // If deleting current conversation, create a new one
    if (convId === currentConversationId) {
      handleNewChat();
    }
  };

  // Show login/signup if not authenticated
  if (!isAuthenticated) {
    if (authView === 'login') {
      return <Login onLoginSuccess={handleLoginSuccess} onSwitchToSignup={() => setAuthView('signup')} />;
    } else {
      return <Signup onSignupSuccess={handleSignupSuccess} onSwitchToLogin={() => setAuthView('login')} />;
    }
  }

  if (!showChat) {
    return (
      <div className="min-h-screen gradient-subtle flex items-center justify-center px-4 py-12 relative">
        {/* User Menu Button - Top Right */}
        <div className="absolute top-6 right-6 user-menu-container">
          <button
            onClick={() => setShowUserMenu(!showUserMenu)}
            className="flex items-center gap-3 bg-white/90 backdrop-blur-sm px-6 py-3 rounded-full shadow-elegant hover:shadow-glow transition-smooth border-2 border-primary/20 hover:border-primary/40"
          >
            <div className="w-10 h-10 bg-gradient-to-br from-primary to-secondary rounded-full flex items-center justify-center">
              <User className="w-5 h-5 text-white" />
            </div>
            <div className="text-left">
              <p className="font-bold text-primary text-sm">{user?.username}</p>
              <p className="text-xs text-muted-foreground">{user?.email}</p>
            </div>
          </button>
          {showUserMenu && (
            <div className="absolute top-full right-0 mt-2 bg-white rounded-xl shadow-elegant border-2 border-primary/20 py-2 min-w-[200px] z-50">
              <button
                onClick={handleLogout}
                className="w-full px-4 py-3 text-left hover:bg-primary/10 transition-smooth flex items-center gap-3 text-foreground font-medium"
              >
                <LogOut className="w-5 h-5 text-destructive" />
                <span>Logout</span>
              </button>
            </div>
          )}
        </div>

        <div className="max-w-6xl w-full">
          <div className="text-center mb-12 space-y-6">
            <div className="inline-block bg-gradient-to-br from-primary to-blue-500 px-12 py-5 rounded-full mb-8 shadow-glow hover:shadow-card-hover hover:scale-105 transition-all duration-300 animate-bounce-in">
              <span className="text-white font-extrabold text-4xl md:text-5xl">
                ⚖️ AI-Powered Legal Assistant
              </span>
            </div>
            <h1 className="text-7xl md:text-9xl font-extrabold mb-10 text-transparent bg-gradient-to-r from-primary via-secondary to-primary bg-clip-text animate-gradient font-serif leading-tight animate-fade-in-up">
              Your Guide to Indian Law
            </h1>
            <p className="text-3xl md:text-4xl text-foreground/80 max-w-4xl mx-auto mb-12 font-sans leading-relaxed font-medium animate-fade-in-up [animation-delay:200ms]">
              Get instant, accurate answers to your legal questions
            </p>
            <button
              className="bg-gradient-to-br from-primary to-blue-500 hover:from-blue-500 hover:to-primary hover:scale-110 hover:shadow-glow active:scale-95 transition-all duration-300 text-2xl px-12 py-8 rounded-3xl shadow-glow font-bold text-white animate-scale-in [animation-delay:400ms] hover:animate-float"
              onClick={handleNewChat}
            >
              Start Your Legal Consultation →
            </button>
          </div>

          <div className="grid md:grid-cols-3 gap-8 mt-20">
            <div className="p-8 bg-white rounded-3xl shadow-card hover:shadow-card-hover hover:scale-105 transition-all duration-300 animate-slide-in-left [animation-delay:600ms] hover:-translate-y-2">
              <div className="bg-gradient-to-br from-blue-500 to-blue-600 w-16 h-16 rounded-2xl flex items-center justify-center mb-5 shadow-lg animate-float">
                <BookOpen className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-2xl font-bold mb-3 text-primary font-sans">Comprehensive Coverage</h3>
              <p className="text-foreground/70 font-sans text-lg leading-relaxed">Access a vast knowledge base of Indian laws and legal precedents.</p>
            </div>
            <div className="p-8 bg-white rounded-3xl shadow-card hover:shadow-card-hover hover:scale-105 transition-all duration-300 animate-slide-in-left [animation-delay:800ms] hover:-translate-y-2">
              <div className="bg-gradient-to-br from-green-500 to-emerald-600 w-16 h-16 rounded-2xl flex items-center justify-center mb-5 shadow-lg animate-float [animation-delay:1s]">
                <Shield className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-2xl font-bold mb-3 text-primary font-sans">Know Your Rights</h3>
              <p className="text-foreground/70 font-sans text-lg leading-relaxed">Understand your legal rights and obligations in various situations.</p>
            </div>
            <div className="p-8 bg-white rounded-3xl shadow-card hover:shadow-card-hover hover:scale-105 transition-all duration-300 animate-slide-in-left [animation-delay:1000ms] hover:-translate-y-2">
              <div className="bg-gradient-to-br from-purple-500 to-purple-600 w-16 h-16 rounded-2xl flex items-center justify-center mb-5 shadow-lg animate-float [animation-delay:2s]">
                <FileText className="w-8 h-8 text-white" />
              </div>
              <h3 className="text-2xl font-bold mb-3 text-primary font-sans">Clear Guidance</h3>
              <p className="text-foreground/70 font-sans text-lg leading-relaxed">Receive easy-to-understand explanations of complex legal terms.</p>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="flex h-screen bg-background font-sans overflow-hidden">
      {/* Sidebar */}
      <Sidebar
        user={user}
        onLogout={handleLogout}
        conversations={conversations}
        currentConversationId={currentConversationId}
        onSelectConversation={handleSelectConversation}
        onNewChat={handleNewChat}
        onDeleteConversation={handleDeleteConversation}
      />

      {/* Main Chat Area */}
      <div className="flex-1 flex flex-col">
        {/* Header */}
        <header className="bg-gradient-to-r from-primary via-secondary to-primary backdrop-blur-md border-b-4 border-accent shadow-elegant">
          <div className="px-8 py-6 flex items-center gap-6">
            {/* Back Button */}
            <button
              onClick={() => setShowChat(false)}
              className="w-12 h-12 bg-white/90 hover:bg-white rounded-full flex items-center justify-center shadow-lg hover:scale-110 active:scale-95 transition-all duration-300 hover:shadow-glow animate-scale-in"
              title="Back to Home"
            >
              <ArrowLeft className="w-6 h-6 text-primary" />
            </button>
            
            <div className="w-16 h-16 bg-white rounded-full flex items-center justify-center shadow-lg animate-float">
              <Scale className="w-9 h-9 text-primary" />
            </div>
            <div className="flex-1">
              <h2 className="text-3xl font-bold text-primary-foreground font-serif">⚖️ Legal AI Assistant</h2>
              <p className="text-base text-primary-foreground/90 font-medium mt-1">Powered by Advanced AI Knowledge Base</p>
            </div>
          </div>
        </header>

        {/* Messages Area */}
        <main className="flex-1 overflow-y-auto px-8 py-6 pb-40">
          <div className="max-w-5xl mx-auto">
            <div className="space-y-6">
              {messages.length === 0 && (
                <div className="text-center text-muted-foreground text-xl py-12">
                  <p className="mb-8 text-3xl font-semibold text-foreground">
                    Welcome, <span className="text-primary font-bold">{user?.username}</span>! How can I assist you with Indian law today?
                  </p>
                  <SuggestedQuestions onQuestionClick={handleSuggestedQuestionClick} />
                </div>
              )}
              {messages.map((message, index) => (
                <ChatMessage key={index} message={message} />
              ))}
              {loading && <TypingIndicator />}
              <div ref={messagesEndRef} className="h-8" />
            </div>
          </div>
        </main>

        {/* Input Area */}
        <div className="fixed bottom-0 left-80 right-0 bg-white/98 backdrop-blur-md border-t border-border shadow-card">
          <div className="px-8 py-6">
            <form onSubmit={(e) => { e.preventDefault(); handleSendMessage(); }} className="max-w-5xl mx-auto flex gap-4">
              <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                placeholder="Ask your legal question..."
                className="flex-1 bg-white text-foreground border-2 border-border hover:border-primary/40 focus:border-primary rounded-2xl px-6 py-4 focus:outline-none focus:ring-2 focus:ring-primary/20 h-16 text-lg shadow-card transition-all duration-200"
                disabled={loading}
              />
              <button
                type="submit"
                className="bg-gradient-to-br from-primary to-blue-500 hover:from-blue-500 hover:to-primary hover:scale-105 active:scale-95 transition-all duration-300 px-8 py-4 rounded-2xl shadow-glow h-16 flex items-center justify-center font-semibold disabled:opacity-50 disabled:cursor-not-allowed"
                disabled={loading}
              >
                {loading ? (
                  <Loader2 className="h-7 w-7 animate-spin text-white" />
                ) : (
                  <Send className="h-7 w-7 text-white" />
                )}
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
