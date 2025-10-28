import React from 'react';

const suggestedQuestions = [
  "What are my rights if a teacher beats my child?",
  "How to file a consumer complaint for a defective product?",
  "What is the procedure for property registration after parents' demise?",
  "What are the legal provisions for domestic violence?",
  "How can I file a cybercrime complaint?",
  "What is Article 21 of the Indian Constitution?",
];

const SuggestedQuestions = ({ onQuestionClick }) => {
  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mt-8 w-full">
      {suggestedQuestions.map((question, index) => (
        <button
          key={index}
          className="h-auto py-6 px-7 text-left justify-start text-xl hover:bg-primary/10 hover:border-primary/50 hover:scale-105 transition-all duration-300 border-2 border-primary/20 rounded-xl text-foreground bg-white shadow-md hover:shadow-elegant font-medium"
          onClick={() => onQuestionClick(question)}
        >
          {question}
        </button>
      ))}
    </div>
  );
};

export default SuggestedQuestions;
