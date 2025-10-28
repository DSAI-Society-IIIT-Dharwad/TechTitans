import React from 'react';
import { Scale } from 'lucide-react';

const Header = ({ isConnected, documentsCount }) => {
  return (
    <div className="bg-gradient-to-r from-legal-700 via-legal-600 to-orange-600 text-white shadow-2xl">
      <div className="max-w-6xl mx-auto px-6 py-6">
        <div className="flex items-center justify-center">
          <div className="flex items-center gap-4">
            <div className="bg-white/20 p-4 rounded-xl backdrop-blur-sm shadow-lg">
              <Scale size={45} />
            </div>
            <div className="text-center">
              <h1 className="text-4xl md:text-5xl font-bold tracking-tight">⚖️ AI Legal Assistant</h1>
              <p className="text-legal-100 text-lg md:text-xl mt-2 font-medium">Your Guide to Indian Law</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Header;
