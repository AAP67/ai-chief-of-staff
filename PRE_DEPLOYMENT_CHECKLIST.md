# Pre-Deployment Checklist

Use this checklist before deploying to ensure everything is ready.

## Code Quality

- [ ] All code is committed to Git
- [ ] No sensitive data in code (API keys, passwords)
- [ ] `.env` file is in `.gitignore`
- [ ] All imports are working
- [ ] No hardcoded file paths
- [ ] Error handling is in place

## Testing

- [ ] App runs locally without errors
- [ ] Tested file upload functionality
- [ ] Tested all analysis modes (Quick Take, Deep Dive, Scenario)
- [ ] Tested export functionality
- [ ] Tested with different file types (PDF, PPTX, etc.)
- [ ] Tested error scenarios

## Documentation

- [ ] README is up to date
- [ ] API key setup instructions are clear
- [ ] Deployment guide is ready
- [ ] Example prompts are included
- [ ] License file exists

## Configuration

- [ ] `.env.example` has all required variables
- [ ] `requirements.txt` lists all dependencies
- [ ] Streamlit config is set up (`.streamlit/config.toml`)
- [ ] `.gitignore` covers all necessary files

## Security

- [ ] API keys are environment variables, not hardcoded
- [ ] No sensitive data committed to Git
- [ ] Dependencies are up to date (no known vulnerabilities)
- [ ] Error messages don't leak sensitive information

## Performance

- [ ] Large files are handled gracefully
- [ ] API calls have timeouts
- [ ] Session state is managed efficiently
- [ ] File processing has error handling

## Deployment Prep

### For Streamlit Cloud:

- [ ] GitHub repository is public (or Streamlit has access)
- [ ] Main file is `app.py` in root directory
- [ ] Have Anthropic API key ready
- [ ] Know where to add secrets in Streamlit dashboard

### For Heroku:

- [ ] Procfile is created
- [ ] runtime.txt specifies Python version
- [ ] Heroku CLI is installed
- [ ] Have Anthropic API key ready

### For Docker:

- [ ] Dockerfile is created and tested
- [ ] .dockerignore is set up
- [ ] Docker image builds successfully
- [ ] Container runs locally

## Post-Deployment

- [ ] Test live app thoroughly
- [ ] Verify API key is working
- [ ] Test file uploads on deployed app
- [ ] Check response times
- [ ] Monitor logs for errors
- [ ] Set up error alerts (if applicable)
- [ ] Share app URL and get feedback

## Optional Enhancements

- [ ] Custom domain configured
- [ ] Analytics/monitoring set up
- [ ] Rate limiting configured
- [ ] Backup strategy in place
- [ ] Auto-scaling configured (if needed)

---

## Quick Deploy Commands

### Streamlit Cloud
```bash
# 1. Push to GitHub
git add .
git commit -m "Ready for deployment"
git push origin main

# 2. Go to share.streamlit.io and follow wizard
# 3. Add ANTHROPIC_API_KEY in secrets
```

### Heroku
```bash
heroku create your-app-name
heroku config:set ANTHROPIC_API_KEY=your_key
git push heroku main
heroku open
```

### Docker
```bash
docker build -t ai-chief-of-staff .
docker run -p 8501:8501 -e ANTHROPIC_API_KEY=your_key ai-chief-of-staff
```

---

## Common Issues

**Issue**: "Module not found" error
- **Fix**: Check `requirements.txt` has all dependencies

**Issue**: API key not working
- **Fix**: Verify key is set correctly in environment/secrets

**Issue**: File upload fails
- **Fix**: Check file size limits and supported formats

**Issue**: App is slow
- **Fix**: Review API usage, consider caching, check network

---

## Need Help?

- Check DEPLOYMENT.md for detailed guides
- Review README for setup instructions
- Open an issue on GitHub
- Contact: karan_rajpal@berkeley.edu
