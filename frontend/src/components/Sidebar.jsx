import { useState } from 'react';
import { MessageSquarePlus, History, User, LogOut, ChevronLeft, ChevronRight, Trash2 } from 'lucide-react';

const Sidebar = ({ user, onLogout, conversations, currentConversationId, onSelectConversation, onNewChat, onDeleteConversation }) => {
  const [isCollapsed, setIsCollapsed] = useState(false);
  const [showAccountDetails, setShowAccountDetails] = useState(false);

  const formatDate = (timestamp) => {
    const date = new Date(timestamp);
    const now = new Date();
    const diffTime = Math.abs(now - date);
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24));
    
    if (diffDays === 0) {
      return 'Today';
    } else if (diffDays === 1) {
      return 'Yesterday';
    } else if (diffDays < 7) {
      return `${diffDays} days ago`;
    } else {
      return date.toLocaleDateString();
    }
  };

  const getConversationTitle = (conv) => {
    if (conv.title) return conv.title;
    if (conv.messages && conv.messages.length > 0) {
      const firstUserMsg = conv.messages.find(m => m.sender === 'user');
      if (firstUserMsg) {
        return firstUserMsg.text.substring(0, 40) + (firstUserMsg.text.length > 40 ? '...' : '');
      }
    }
    return 'New Conversation';
  };

  return (
    <>
      {/* Sidebar */}
      <div className={`${isCollapsed ? 'w-20' : 'w-80'} bg-gradient-to-b from-primary to-secondary h-screen flex flex-col transition-all duration-300 shadow-elegant relative`}>
        
        {/* Toggle Button */}
        <button
          onClick={() => setIsCollapsed(!isCollapsed)}
          className="absolute -right-3 top-8 w-6 h-6 bg-white rounded-full shadow-md flex items-center justify-center hover:scale-110 transition-smooth z-20"
        >
          {isCollapsed ? (
            <ChevronRight className="w-4 h-4 text-primary" />
          ) : (
            <ChevronLeft className="w-4 h-4 text-primary" />
          )}
        </button>

        {/* Header - User Info */}
        <div className="p-4 border-b border-white/20">
          <div className="flex items-center gap-3">
            <div className="w-12 h-12 bg-white rounded-full flex items-center justify-center flex-shrink-0">
              <User className="w-6 h-6 text-primary" />
            </div>
            {!isCollapsed && (
              <div className="flex-1 overflow-hidden">
                <p className="font-bold text-primary-foreground text-sm truncate">{user?.username}</p>
                <p className="text-xs text-primary-foreground/80 truncate">{user?.email}</p>
              </div>
            )}
          </div>
        </div>

        {/* New Chat Button */}
        <div className="p-4">
          <button
            onClick={onNewChat}
            className="w-full bg-white/20 hover:bg-white/30 backdrop-blur-sm py-3 rounded-xl shadow-md transition-smooth flex items-center justify-center gap-2 font-semibold text-primary-foreground"
            title="New Chat"
          >
            <MessageSquarePlus className="w-5 h-5" />
            {!isCollapsed && <span>New Chat</span>}
          </button>
        </div>

        {/* Chat History */}
        <div className="flex-1 overflow-y-auto px-4 pb-4">
          {!isCollapsed && (
            <div className="mb-3 flex items-center gap-2 text-primary-foreground/80">
              <History className="w-4 h-4" />
              <p className="text-sm font-semibold">Chat History</p>
            </div>
          )}
          <div className="space-y-2">
            {conversations.length === 0 ? (
              !isCollapsed && (
                <p className="text-sm text-primary-foreground/60 text-center py-4">No conversations yet</p>
              )
            ) : (
              conversations.map((conv) => (
                <div
                  key={conv.id}
                  className={`group relative rounded-xl transition-smooth ${
                    currentConversationId === conv.id
                      ? 'bg-white/30 backdrop-blur-sm'
                      : 'bg-white/10 hover:bg-white/20'
                  } ${isCollapsed ? 'p-3' : 'p-3'}`}
                >
                  <button
                    onClick={() => onSelectConversation(conv.id)}
                    className="w-full text-left"
                    title={isCollapsed ? getConversationTitle(conv) : ''}
                  >
                    {isCollapsed ? (
                      <MessageSquarePlus className="w-5 h-5 text-primary-foreground mx-auto" />
                    ) : (
                      <>
                        <p className="text-sm font-medium text-primary-foreground truncate">
                          {getConversationTitle(conv)}
                        </p>
                        <p className="text-xs text-primary-foreground/60 mt-1">
                          {formatDate(conv.timestamp)}
                        </p>
                      </>
                    )}
                  </button>
                  {!isCollapsed && (
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onDeleteConversation(conv.id);
                      }}
                      className="absolute right-2 top-1/2 -translate-y-1/2 opacity-0 group-hover:opacity-100 p-1 hover:bg-destructive/80 rounded-lg transition-all"
                      title="Delete conversation"
                    >
                      <Trash2 className="w-4 h-4 text-white" />
                    </button>
                  )}
                </div>
              ))
            )}
          </div>
        </div>

        {/* Bottom Actions */}
        <div className="border-t border-white/20 p-4 space-y-2">
          {/* Account Details Button */}
          <button
            onClick={() => setShowAccountDetails(true)}
            className="w-full bg-white/10 hover:bg-white/20 py-3 rounded-xl transition-smooth flex items-center justify-center gap-2 text-primary-foreground font-medium"
            title="Account Details"
          >
            <User className="w-5 h-5" />
            {!isCollapsed && <span>Account Details</span>}
          </button>

          {/* Logout Button */}
          <button
            onClick={onLogout}
            className="w-full bg-destructive/80 hover:bg-destructive py-3 rounded-xl transition-smooth flex items-center justify-center gap-2 text-white font-medium"
            title="Logout"
          >
            <LogOut className="w-5 h-5" />
            {!isCollapsed && <span>Logout</span>}
          </button>
        </div>
      </div>

      {/* Account Details Modal */}
      {showAccountDetails && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm z-50 flex items-center justify-center p-4">
          <div className="bg-white rounded-2xl shadow-elegant max-w-md w-full p-8 animate-fade-in">
            <div className="flex items-center justify-between mb-6">
              <h2 className="text-2xl font-bold text-primary font-serif">Account Details</h2>
              <button
                onClick={() => setShowAccountDetails(false)}
                className="text-muted-foreground hover:text-foreground transition-smooth"
              >
                ✕
              </button>
            </div>
            
            <div className="space-y-4">
              <div className="flex items-center gap-4 pb-4 border-b border-border">
                <div className="w-16 h-16 bg-gradient-to-br from-primary to-secondary rounded-full flex items-center justify-center">
                  <User className="w-8 h-8 text-white" />
                </div>
                <div>
                  <p className="text-lg font-bold text-foreground">{user?.username}</p>
                  <p className="text-sm text-muted-foreground">{user?.email}</p>
                </div>
              </div>

              <div className="space-y-3">
                <div>
                  <p className="text-sm font-semibold text-muted-foreground">Username</p>
                  <p className="text-base text-foreground">{user?.username}</p>
                </div>
                <div>
                  <p className="text-sm font-semibold text-muted-foreground">Email</p>
                  <p className="text-base text-foreground">{user?.email}</p>
                </div>
                <div>
                  <p className="text-sm font-semibold text-muted-foreground">Member Since</p>
                  <p className="text-base text-foreground">
                    {user?.createdAt ? new Date(user.createdAt).toLocaleDateString('en-US', {
                      year: 'numeric',
                      month: 'long',
                      day: 'numeric'
                    }) : 'N/A'}
                  </p>
                </div>
              </div>

              <button
                onClick={() => setShowAccountDetails(false)}
                className="w-full gradient-accent py-3 rounded-xl font-semibold text-accent-foreground shadow-glow hover:opacity-90 transition-smooth mt-6"
              >
                Close
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

export default Sidebar;

