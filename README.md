# AI Chief of Staff 🎯

An AI-powered strategic analysis tool that helps founders and executives with decision-making, deal evaluation, and business operations planning.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.29+-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Overview

AI Chief of Staff leverages Claude (Anthropic's AI) to provide strategic analysis, scenario planning, and decision support for Series A/B stage companies. Upload documents, ask questions, and get direct, actionable insights.

## Features

- **Strategic Decision Support**: Market entry, pricing, partnerships, and more
- **Deal Analysis**: Evaluate pitch decks, financial models, competitive positioning
- **Document Processing**: Upload and analyze PDFs, PowerPoint, Excel, CSV, and text files
- **Multiple Analysis Modes**:
  - 🎯 Quick Take (3-5 key points)
  - 📊 Deep Dive (comprehensive analysis)
  - 📈 Scenario Analysis (bull/base/bear cases)
- **Export Functionality**: Save analyses as markdown files
- **Conversation Memory**: Maintains context across the session

## Demo

[Insert screenshot or demo video here]

## Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Claude Sonnet 4 (Anthropic)
- **Document Processing**: PyPDF2, python-pptx, openpyxl, pandas
- **Language**: Python 3.8+

## Quick Start

### Prerequisites

- Python 3.8 or higher
- Anthropic API key ([get one here](https://console.anthropic.com/))

### Local Installation

1. **Clone the repository:**
```bash
git clone https://github.com/YOUR_USERNAME/ai-chief-of-staff.git
cd ai-chief-of-staff
```

2. **Create a virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables:**

Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_actual_api_key_here
```

5. **Run the application:**
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Deployment

### Deploy to Streamlit Cloud (Recommended)

1. **Push your code to GitHub** (make sure `.env` is in `.gitignore`)

2. **Go to [share.streamlit.io](https://share.streamlit.io)**

3. **Deploy your app:**
   - Connect your GitHub repository
   - Select the branch (usually `main`)
   - Set the main file path: `app.py`

4. **Add secrets:**
   - In your app settings, go to "Secrets"
   - Add your API key:
   ```toml
   ANTHROPIC_API_KEY = "your_api_key_here"
   ```

5. **Deploy!** Your app will be live at `https://your-app-name.streamlit.app`

### Alternative Deployment Options

<details>
<summary>Deploy to Heroku</summary>

1. Create a `Procfile`:
```
web: streamlit run app.py --server.port=$PORT
```

2. Deploy:
```bash
heroku create your-app-name
heroku config:set ANTHROPIC_API_KEY=your_api_key
git push heroku main
```
</details>

<details>
<summary>Deploy with Docker</summary>

1. Create a `Dockerfile`:
```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

2. Build and run:
```bash
docker build -t ai-chief-of-staff .
docker run -p 8501:8501 -e ANTHROPIC_API_KEY=your_key ai-chief-of-staff
```
</details>

## Usage Guide

### Basic Usage

1. **Select Analysis Mode**: Choose between Quick Take, Deep Dive, or Scenario Analysis
2. **Upload Documents** (optional): Add pitch decks, financials, or research
3. **Ask Questions**: Type your strategic question
4. **Review Analysis**: Get structured, actionable insights
5. **Export**: Download your analysis as markdown

### Example Prompts

**Strategic Decisions:**
```
- Should we enter the enterprise market or focus on SMB?
- Evaluate this partnership opportunity with [Company X]
- Help me think through our pricing strategy
```

**Deal Analysis:**
```
- Here's a pitch deck - should we invest/acquire?
- Analyze this competitor and our positioning
- Review our financial model and projections
```

**Board/Investor Prep:**
```
- Help me frame our pivot for the board
- Create talking points for our Series B pitch
- Stress-test our growth assumptions
```

## Project Structure

```
ai-chief-of-staff/
├── app.py                    # Main Streamlit application
├── system_prompt.py          # AI system instructions and personality
├── requirements.txt          # Python dependencies
├── utils/
│   ├── __init__.py
│   └── file_processor.py     # Document processing utilities
├── .streamlit/
│   ├── config.toml          # Streamlit configuration
│   └── secrets.toml.example # Secrets template
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Configuration

### Environment Variables

- `ANTHROPIC_API_KEY`: Your Anthropic API key (required)

### Streamlit Configuration

Edit `.streamlit/config.toml` to customize:
- Theme colors
- Server settings
- Browser behavior

## Development

### Running Tests

```bash
pytest tests/
```

### Code Style

This project uses:
- Black for code formatting
- Flake8 for linting
- Type hints where applicable

```bash
black .
flake8 .
```

## Troubleshooting

**Issue: API key not found**
- Make sure you've created a `.env` file with your API key
- For Streamlit Cloud, check your app secrets in settings

**Issue: Document processing fails**
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that the uploaded file isn't corrupted

**Issue: Slow responses**
- Claude Sonnet 4 is powerful but can take time for complex analyses
- Consider using Quick Take mode for faster responses

## Roadmap

- [ ] Add support for more file types (Notion exports, Google Docs)
- [ ] Implement conversation history persistence
- [ ] Add collaborative features for team usage
- [ ] Integration with common business tools (Slack, Notion)
- [ ] Custom analysis templates
- [ ] Multi-language support

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Claude](https://www.anthropic.com/claude) by Anthropic
- UI powered by [Streamlit](https://streamlit.io/)
- Inspired by the needs of Series A/B founders

## Contact

Built by Karan Rajpal

- GitHub: [@AAP67](https://github.com/AAP67)
- LinkedIn: [linkedin.com/in/krajpal](https://www.linkedin.com/in/krajpal/)
- Email: karan_rajpal@berkeley.edu

---

**Note:** This is a demonstration project showcasing AI-powered business tools for strategic decision support. It's designed for educational and portfolio purposes.
