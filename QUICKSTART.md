# Quick Start Guide

Get AI Chief of Staff running in 5 minutes.

## For Local Development

```bash
# 1. Clone and navigate
git clone https://github.com/YOUR_USERNAME/ai-chief-of-staff.git
cd ai-chief-of-staff

# 2. Run setup script
chmod +x setup.sh
./setup.sh

# 3. Add your API key to .env
# Edit .env and replace 'your_api_key_here' with your actual key
# Get key at: https://console.anthropic.com/

# 4. Activate environment and run
source venv/bin/activate
streamlit run app.py
```

Done! App runs at `http://localhost:8501`

## For Streamlit Cloud (Recommended for Demo)

```bash
# 1. Push to GitHub
git add .
git commit -m "Initial commit"
git push origin main

# 2. Deploy
# - Go to https://share.streamlit.io
# - Click "New app"
# - Select your repo
# - Click "Deploy"

# 3. Add API key
# - In app settings, go to "Secrets"
# - Add: ANTHROPIC_API_KEY = "your_key_here"
# - Save
```

Done! Your app is live at `https://your-app.streamlit.app`

## First Time Using?

Try these prompts:

**Quick Test:**
```
What's 2+2? (Just to make sure it's working)
```

**Strategic Question:**
```
Should a Series A SaaS company focus on enterprise or SMB customers first?
```

**With Document Upload:**
1. Upload a PDF or PowerPoint
2. Ask: "Summarize the key points in this document"

**Scenario Analysis:**
1. Select "Scenario Analysis" mode
2. Ask: "What are bull/base/bear revenue scenarios for a SaaS company growing 20% MoM?"

## Troubleshooting

**"Module not found" error**
```bash
pip install -r requirements.txt
```

**"API key not found" error**
- Check `.env` file has your key
- For Streamlit Cloud, check secrets are added

**App won't start**
```bash
# Check if port 8501 is in use
lsof -i :8501
# Kill if needed, then restart
```

## Next Steps

- Read [README.md](README.md) for full documentation
- Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment options
- See [CONTRIBUTING.md](CONTRIBUTING.md) to contribute

## Need Help?

- Open an issue on GitHub
- Email: karan_rajpal@berkeley.edu

Happy analyzing! 🎯
