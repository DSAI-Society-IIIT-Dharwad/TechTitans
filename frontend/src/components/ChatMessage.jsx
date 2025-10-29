import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { User, Bot } from 'lucide-react';

const ChatMessage = ({ message }) => {
  const isUser = message.sender === 'user';

  return (
    <div className={`flex items-start gap-6 mb-8 animate-fade-in-up ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-blue-400 flex items-center justify-center flex-shrink-0 shadow-glow animate-scale-in">
          <Bot className="w-8 h-8 text-white" />
        </div>
      )}
      <div className={`p-8 flex-1 rounded-3xl break-words transition-all duration-300 hover:shadow-card-hover
        ${isUser ? 'bg-gradient-to-br from-primary to-blue-500 text-white rounded-br-none max-w-[70%] shadow-glow animate-slide-in-right' : 'bg-white text-foreground border border-border shadow-card rounded-bl-none animate-slide-in-left'}`}>
        <div className="text-xl leading-relaxed">
          {isUser ? (
            <p className="whitespace-pre-wrap font-medium">{message.text}</p>
          ) : (
            <div className="prose prose-xl max-w-none">
              <ReactMarkdown remarkPlugins={[remarkGfm]}>
                {message.text}
              </ReactMarkdown>
            </div>
          )}
        </div>
        {message.sources && message.sources.length > 0 && (
          <div className="mt-5 pt-5 border-t-2 border-border text-base">
            <p className="font-bold mb-3 text-primary">📚 Sources:</p>
            <ul className="list-disc list-inside space-y-2">
              {message.sources.map((source, index) => (
                <li key={index} className="text-foreground">
                  <a
                    href={source.source}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-primary hover:text-primary/80 transition-colors duration-200 font-medium hover:underline"
                  >
                    {source.title || `Source ${index + 1}`}
                  </a>
                </li>
              ))}
            </ul>
          </div>
        )}
      </div>
      {isUser && (
        <div className="w-16 h-16 rounded-full bg-gradient-to-br from-primary to-blue-500 flex items-center justify-center flex-shrink-0 shadow-glow animate-scale-in">
          <User className="w-8 h-8 text-white" />
        </div>
      )}
    </div>
  );
};

export default ChatMessage;
