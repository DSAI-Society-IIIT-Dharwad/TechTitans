import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { User, Bot } from 'lucide-react';

const ChatMessage = ({ message }) => {
  const isUser = message.sender === 'user';

  return (
    <div className={`flex items-start gap-6 mb-8 ${isUser ? 'justify-end' : 'justify-start'}`}>
      {!isUser && (
        <div className="w-16 h-16 rounded-full gradient-primary flex items-center justify-center flex-shrink-0 shadow-lg">
          <Bot className="w-8 h-8 text-primary-foreground" />
        </div>
      )}
      <div className={`p-8 flex-1 rounded-2xl break-words shadow-elegant
        ${isUser ? 'bg-gradient-to-br from-primary to-accent text-primary-foreground rounded-br-none max-w-[70%]' : 'bg-card text-card-foreground border border-border rounded-bl-none'}`}>
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
          <div className="mt-5 pt-5 border-t-2 border-primary/20 text-base">
            <p className="font-bold mb-3 text-primary">📚 Sources:</p>
            <ul className="list-disc list-inside space-y-2">
              {message.sources.map((source, index) => (
                <li key={index}>
                  <a
                    href={source.source}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-accent hover:text-secondary transition-colors duration-200 font-medium hover:underline"
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
        <div className="w-16 h-16 rounded-full gradient-accent flex items-center justify-center flex-shrink-0 shadow-lg">
          <User className="w-8 h-8 text-accent-foreground" />
        </div>
      )}
    </div>
  );
};

export default ChatMessage;
