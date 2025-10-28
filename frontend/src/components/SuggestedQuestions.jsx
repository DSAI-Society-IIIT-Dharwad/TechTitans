import React from 'react';
import { MessageCircle } from 'lucide-react';

const suggestedQuestions = [
  "What are the fundamental rights under the Indian Constitution?",
  "Explain the process of house registration after parents' demise",
  "What is Article 21 of the Indian Constitution?",
  "What are the legal requirements for property inheritance in India?",
];

const SuggestedQuestions = ({ onSelect }) => {
  return (
    <div className="mb-4">
      <h3 className="text-base font-bold text-gray-700 mb-3 flex items-center gap-2">
        <MessageCircle size={18} />
        Try asking me:
      </h3>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
        {suggestedQuestions.map((question, index) => (
          <button
            key={index}
            onClick={() => onSelect(question)}
            className="text-left p-3 rounded-lg border-2 border-gray-200 bg-white hover:bg-legal-50 hover:border-legal-400 hover:shadow-md transition-all duration-200 text-sm font-medium text-gray-700 hover:text-legal-800"
          >
            💬 {question}
          </button>
        ))}
      </div>
    </div>
  );
};

export default SuggestedQuestions;

