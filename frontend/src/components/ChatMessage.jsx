import React from 'react';
import ReactMarkdown from 'react-markdown';
import { User, Scale } from 'lucide-react';

const ChatMessage = ({ message }) => {
  const isUser = message.role === 'user';
  
  return (
    <div className={`flex items-start gap-6 mb-8 ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>
      {/* Avatar */}
      <div className={`flex-shrink-0 w-16 h-16 rounded-full flex items-center justify-center shadow-lg ${
        isUser 
          ? 'bg-gradient-to-br from-legal-600 to-legal-700 text-white' 
          : 'bg-gradient-to-br from-orange-500 to-red-500 text-white'
      }`}>
        {isUser ? <User size={28} /> : <Scale size={28} />}
      </div>
      
      {/* Message Bubble */}
      <div className={`chat-bubble ${isUser ? 'chat-bubble-user' : 'chat-bubble-assistant'}`}>
        {isUser ? (
          <p className="text-xl font-medium leading-relaxed">{message.content}</p>
        ) : (
          <div className="prose prose-lg max-w-none">
            <ReactMarkdown
              components={{
                p: ({ children }) => <p className="mb-3 last:mb-0 text-xl leading-relaxed">{children}</p>,
                strong: ({ children }) => <strong className="font-bold text-legal-900">{children}</strong>,
                em: ({ children }) => <em className="italic">{children}</em>,
                ul: ({ children }) => <ul className="list-disc list-inside mb-3 space-y-2">{children}</ul>,
                ol: ({ children }) => <ol className="list-decimal list-inside mb-3 space-y-2">{children}</ol>,
                li: ({ children }) => <li className="mb-2 text-xl">{children}</li>,
              }}
            >
              {message.content}
            </ReactMarkdown>
          </div>
        )}
        
        {/* Timestamp */}
        <div className={`text-xs mt-2 font-medium ${isUser ? 'text-legal-100' : 'text-gray-500'}`}> 
          {new Date(message.timestamp).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })}
        </div>
      </div>
    </div>
  );
};

export default ChatMessage;

