# Multi-Agent Medical Image Analyzer

Multi-agent AI medical Image Analyzer is a state-of-the-art AI-powered healthcare platform designed to transform healthcare interactions for professionals and patients alike. The platform includes three core modules that work together to enhance accessibility, diagnostic accuracy, and patient engagement:

- *AI Image Analyzer*: Leverages deep learning to analyze medical images (e.g., X-rays, MRIs) for abnormalities with precision.  
- *AI Chatbox*: Provides real-time health advice, symptom-based disease predictions, and personalized recommendations.  


---

## Features

- *Advanced Image Diagnostics*: Accurate and real-time analysis of medical images using AI-powered algorithms.  
- *AI-Driven Health Advice*: Symptom analysis and disease predictions through an interactive chatbot.  
- *Medicine Insights*: Detailed information about medicines, including advantages, disadvantages, and recommended usage.  
- *Powered by Generative AI*: Integration with Google Generative AI for intelligent healthcare insights and enhanced user experience.

---

## Getting Started

### *Prerequisites*  

Before setting up Multi-Agent Medical Image Analyzer  ensure the following are installed:  
- Python 3.8 or higher  
- Streamlit  
- Google Generative AI (MakerSuite) API Key  
- Git  

### *Setup Instructions*

1. *Clone the Repository*  
   Download the Multi-Agent Medical Image Analyzer project using Git:  
   bash
   git clone https://github.com/<your-username>/medicalImageAnalyzer
   cd AI-Powered Medical Image Analyzer
   

2. *Set Up a Virtual Environment*  
   Create and activate a virtual environment to manage dependencies:  
   - *Create*: python -m venv env  
   - *Activate*:  
     - For Linux/Mac: source env/bin/activate  
     - For Windows: env\Scripts\activate  

3. *Install Dependencies*  
   Install the required dependencies from the requirements.txt file:  
   bash
   pip install -r requirements.txt
   

4. *Configure API Keys*  
   open the api_key.py and add your api key
   
   api_key="your api key here"

5. **Run the Application**  
   Start the local development server with Streamlit:  
   bash
   streamlit run imageAnalyser.py
   streamlit run Chatbot.py
   ```  
   This will launch the application in your default web browser.

   then open the Index.html

7. *Explore the Platform*  
   - Use the *AI Image Analyzer* to analyze medical images.  
   - Chat with the *AI Chatbox* for real-time health advice.
---
