# 🚀 Deployment Guide

This guide covers deploying the AI Legal Chatbot to production.

## 🌐 Deployment Options

### Option 1: Deploy to Render (Recommended for Hackathons)

#### Backend Deployment

1. Create a `render.yaml`:

```yaml
services:
  - type: web
    name: legal-chatbot-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.9.0
```

2. Push to GitHub
3. Connect to Render
4. Deploy!

#### Frontend Deployment

1. Build the frontend:
```bash
cd frontend
npm run build
```

2. Deploy `frontend/dist` to Netlify, Vercel, or Render

### Option 2: Deploy to Heroku

#### Backend (Heroku)

1. Create `Procfile`:
```
web: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
```

2. Create `runtime.txt`:
```
python-3.9.16
```

3. Deploy:
```bash
heroku create legal-chatbot-backend
git push heroku main
```

#### Frontend (Netlify)

1. Build:
```bash
cd frontend
npm run build
```

2. Deploy to Netlify:
```bash
npm install -g netlify-cli
netlify deploy --prod --dir=dist
```

### Option 3: Docker Deployment

#### Docker Compose Setup

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  backend:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
      - ./vectorstore:/app/vectorstore
    environment:
      - PYTHONUNBUFFERED=1

  frontend:
    build: ./frontend
    ports:
      - "3000:3000"
    depends_on:
      - backend
```

Create `Dockerfile` (root):

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend ./backend
COPY data ./data

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Create `frontend/Dockerfile`:

```dockerfile
FROM node:18-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "run", "preview", "--", "--host", "0.0.0.0", "--port", "3000"]
```

Deploy:
```bash
docker-compose up -d
```

## 🔒 Production Checklist

- [ ] Add environment variables for sensitive data
- [ ] Enable HTTPS
- [ ] Set up proper CORS origins
- [ ] Add rate limiting
- [ ] Set up logging and monitoring
- [ ] Add error tracking (Sentry)
- [ ] Set up CI/CD pipeline
- [ ] Add health check endpoints
- [ ] Configure backup for vector database
- [ ] Add authentication (if needed)

## 🌍 Environment Variables

Create `.env` file:

```env
# Backend
OPENAI_API_KEY=your_key_here
FRONTEND_URL=https://your-frontend.com
ENVIRONMENT=production

# Database
VECTOR_DB_PATH=/app/vectorstore

# Security
SECRET_KEY=your_secret_key_here
```

## 📊 Monitoring

Set up monitoring with:
- **Backend:** Sentry, New Relic
- **Frontend:** Google Analytics, Vercel Analytics
- **Uptime:** UptimeRobot, Pingdom

## 🔐 Security Best Practices

1. **API Keys:** Use environment variables
2. **CORS:** Restrict to specific domains
3. **Rate Limiting:** Prevent abuse
4. **Input Validation:** Sanitize user input
5. **HTTPS:** Always use SSL/TLS

## 📈 Scaling Considerations

- Use Redis for caching
- Implement request queuing
- Use CDN for frontend assets
- Consider serverless functions
- Scale horizontally with load balancer

---

**Good luck with deployment!**

