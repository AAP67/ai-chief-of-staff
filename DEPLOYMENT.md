# Deployment Guide

This guide covers deploying AI Chief of Staff to various platforms.

## Table of Contents

- [Streamlit Cloud](#streamlit-cloud-recommended)
- [Heroku](#heroku)
- [Docker](#docker)
- [AWS](#aws)
- [Google Cloud](#google-cloud)

---

## Streamlit Cloud (Recommended)

**Cost**: Free tier available
**Difficulty**: Easy
**Best for**: Quick deployment, demos, portfolio projects

### Steps

1. **Prepare your repository**
   ```bash
   # Make sure .env is in .gitignore
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Connect your GitHub account
   - Select your repository
   - Set main file: `app.py`
   - Click "Deploy"

3. **Add secrets**
   - In your app dashboard, click "⚙️ Settings"
   - Go to "Secrets"
   - Add your API key:
   ```toml
   ANTHROPIC_API_KEY = "sk-ant-..."
   ```
   - Save changes

4. **Access your app**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Share the link!

### Updating Your App

Just push to GitHub - Streamlit Cloud auto-deploys:
```bash
git add .
git commit -m "Update features"
git push origin main
```

---

## Heroku

**Cost**: $5-7/month for hobby tier
**Difficulty**: Medium
**Best for**: Production apps, custom domains

### Steps

1. **Install Heroku CLI**
   ```bash
   # macOS
   brew tap heroku/brew && brew install heroku
   
   # Windows
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

2. **Create Procfile**
   ```bash
   echo "web: streamlit run app.py --server.port=\$PORT --server.address=0.0.0.0" > Procfile
   ```

3. **Create runtime.txt** (specify Python version)
   ```bash
   echo "python-3.9.18" > runtime.txt
   ```

4. **Deploy**
   ```bash
   heroku login
   heroku create your-app-name
   heroku config:set ANTHROPIC_API_KEY=your_key_here
   git push heroku main
   heroku open
   ```

### Updating

```bash
git push heroku main
```

---

## Docker

**Cost**: Varies by hosting
**Difficulty**: Medium-Hard
**Best for**: Custom infrastructure, enterprise deployments

### Steps

1. **Create Dockerfile**
   ```dockerfile
   FROM python:3.9-slim

   WORKDIR /app

   # Install dependencies
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt

   # Copy app files
   COPY . .

   # Expose port
   EXPOSE 8501

   # Health check
   HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

   # Run app
   CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
   ```

2. **Create .dockerignore**
   ```
   .env
   venv/
   __pycache__/
   *.pyc
   .git/
   .gitignore
   README.md
   ```

3. **Build and run**
   ```bash
   # Build image
   docker build -t ai-chief-of-staff .
   
   # Run container
   docker run -p 8501:8501 \
     -e ANTHROPIC_API_KEY=your_key \
     ai-chief-of-staff
   ```

4. **Deploy to Docker Hub**
   ```bash
   docker tag ai-chief-of-staff:latest username/ai-chief-of-staff:latest
   docker push username/ai-chief-of-staff:latest
   ```

---

## AWS

**Cost**: ~$10-20/month
**Difficulty**: Hard
**Best for**: Enterprise, scalability needs

### Option 1: AWS Elastic Beanstalk

1. **Install EB CLI**
   ```bash
   pip install awsebcli
   ```

2. **Initialize EB**
   ```bash
   eb init -p python-3.9 ai-chief-of-staff
   eb create production
   ```

3. **Set environment variables**
   ```bash
   eb setenv ANTHROPIC_API_KEY=your_key
   ```

4. **Deploy**
   ```bash
   eb deploy
   eb open
   ```

### Option 2: AWS ECS (Docker)

1. Create ECR repository
2. Push Docker image to ECR
3. Create ECS cluster
4. Create task definition
5. Create service
6. Configure load balancer

[Detailed AWS guide here](https://docs.aws.amazon.com/elasticbeanstalk/)

---

## Google Cloud

**Cost**: ~$10-20/month
**Difficulty**: Hard
**Best for**: Google Cloud ecosystem integration

### Using Cloud Run

1. **Install gcloud CLI**
   ```bash
   # macOS
   brew install google-cloud-sdk
   ```

2. **Build and deploy**
   ```bash
   gcloud init
   gcloud builds submit --tag gcr.io/PROJECT_ID/ai-chief-of-staff
   gcloud run deploy --image gcr.io/PROJECT_ID/ai-chief-of-staff \
     --platform managed \
     --set-env-vars ANTHROPIC_API_KEY=your_key
   ```

---

## Environment Variables

All platforms need these environment variables:

| Variable | Required | Description |
|----------|----------|-------------|
| `ANTHROPIC_API_KEY` | Yes | Your Anthropic API key |

---

## Custom Domain

### Streamlit Cloud
1. Go to app settings
2. Add custom domain
3. Update DNS records as instructed

### Heroku
```bash
heroku domains:add www.yourdomain.com
# Follow DNS instructions
```

### Others
Configure through platform's domain management.

---

## SSL/HTTPS

- **Streamlit Cloud**: Automatic HTTPS
- **Heroku**: Automatic HTTPS  
- **Docker/Custom**: Use Let's Encrypt + Nginx

---

## Monitoring

### Streamlit Cloud
- Built-in analytics
- View logs in dashboard

### Heroku
```bash
heroku logs --tail
```

### Docker
```bash
docker logs -f container_name
```

---

## Troubleshooting

### App won't start
- Check logs for errors
- Verify all dependencies in requirements.txt
- Ensure API key is set correctly

### Slow performance
- Upgrade to paid tier
- Add caching with `@st.cache_resource`
- Optimize document processing

### Out of memory
- Reduce max file upload size
- Process documents in chunks
- Clear session state more frequently

---

## Cost Comparison

| Platform | Free Tier | Paid | Best For |
|----------|-----------|------|----------|
| Streamlit Cloud | ✅ 1 app | $20/mo | Demos, portfolios |
| Heroku | ❌ | $7/mo | Production apps |
| AWS | ✅ 12 months | $10-50/mo | Enterprise |
| GCP | ✅ Limited | $10-50/mo | Google integration |
| Docker + VPS | ❌ | $5-20/mo | Full control |

---

## Security Checklist

- [ ] API keys in environment variables, not code
- [ ] `.env` in `.gitignore`
- [ ] HTTPS enabled
- [ ] Input validation on file uploads
- [ ] Rate limiting configured
- [ ] Error messages don't leak sensitive info
- [ ] Dependencies regularly updated

---

## Next Steps

After deployment:

1. **Test thoroughly**
   - Try all features
   - Upload different file types
   - Test error scenarios

2. **Monitor usage**
   - Check API usage
   - Monitor costs
   - Review logs regularly

3. **Collect feedback**
   - Share with users
   - Track issues
   - Iterate on features

4. **Scale as needed**
   - Upgrade plan
   - Add caching
   - Optimize performance

---

## Support

- **Streamlit**: [docs.streamlit.io](https://docs.streamlit.io)
- **Heroku**: [devcenter.heroku.com](https://devcenter.heroku.com)
- **Docker**: [docs.docker.com](https://docs.docker.com)
- **AWS**: [docs.aws.amazon.com](https://docs.aws.amazon.com)

## Questions?

Open an issue or contact: karan_rajpal@berkeley.edu
