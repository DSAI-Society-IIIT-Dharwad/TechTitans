import React from 'react';
import { Scale } from 'lucide-react';

const TypingIndicator = () => {
  return (
    <div className="flex items-start gap-3 mb-4">
      {/* Avatar */}
      <div className="flex-shrink-0 w-10 h-10 rounded-full flex items-center justify-center bg-gradient-to-br from-orange-500 to-red-500 text-white">
        <Scale size={20} />
      </div>
      
      {/* Typing Animation */}
      <div className="chat-bubble chat-bubble-assistant">
        <div className="typing-indicator">
          <span></span>
          <span></span>
          <span></span>
        </div>
      </div>
    </div>
  );
};

export default TypingIndicator;

