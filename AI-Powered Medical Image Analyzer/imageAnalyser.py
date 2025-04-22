
import streamlit as st
import google.generativeai as genai
from api_key import api_key
# Inject CSS for styling


# === Configure Generative AI ===
#def analyze_image(uploaded_xray,uploaded_report):
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.9,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}

safety_setting = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# === System Prompts for Each Agent ===
xray_prompt = """
You are an X-ray analysis agent. Your job is to:
1. Detailed Analysis: Thoroughly analyze each image, focusing on identifying any abnormal findings.

2. Findings Report: Document all observed anomalies or signs of disease. Clearly articulate these findings in a structured format.

3. Recommendations and Next Steps: Based on your analysis, suggest potential next steps, including further tests or treatments as applicable.

4. Treatment Suggestions: If appropriate, recommend possible treatment options or interventions.

5. Detect abnormalities (e.g., fractures, lung issues, bone structure problems).

6. Highlight potential diagnosis.
Important Notes:

1. Scope of Response: Only respond if the image pertains to human health issues.

2. Clarity of Image: In cases where the image quality impedes clear analysis, note that certain aspects are 'Unable to be determined based on the provided image.

3. Disclaimer: Accompany your analysis with the disclaimer: "Consult with a Doctor before making any decisions."

4. Your insights are invaluable in guiding clinical decisions. Please proceed with the analysis, adhering to the structured approach outlined above

Only respond based on visual data from the X-ray.
"""

history_prompt = """
You are a medical history analysis agent. Your job is to:
1. Read the patient's previous medical report.
2. Identify any relevant pre-existing conditions or treatments.
3. Correlate any findings with known patterns.
4. Suggest how the history may relate to current symptoms.

Respond only if the report contains relevant human medical history.
"""

# === Streamlit App Config ===
st.set_page_config(
    page_title="Multi-Agent Medical Analysis",
    page_icon=":brain:",
    layout="wide",
)
st.markdown("""

    <style>
    <style>
  body {
        background: linear-gradient(135deg, #f8fbff, #e0f7fa, #fff1f5);
        color: #2a2a2a;
        font-family: 'Titillium Web', sans-serif;
    }
    .stApp {
        background: linear-gradient(135deg, #f0faff, #fefefe);
    }

    h1, h2, h3, h4 {
        color: #5c6bc0;
        text-align: center;
        font-weight: 700;
        text-shadow: 0 1px 2px rgba(255,255,255,0.6);
        transition: color 0.3s ease;
    }

    h1:hover, h2:hover, h3:hover, h4:hover {
        color: #6e8efb;
        cursor: pointer;
    }

    .css-1v0mbdj p {
        color: #2e3d49;
        font-size: 1.05rem;
        transition: transform 0.3s ease;
    }

    .css-1v0mbdj p:hover {
        transform: scale(1.02);
    }

    .css-1cpxqw2, .css-ffhzg2 {
        background-color: #ffffffdd;
        border: 1px solid #dee2e6;
        border-radius: 12px;
        padding: 16px;
        color: #333;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
        transition: all 0.3s ease-in-out;
    }

    .css-1cpxqw2:hover, .css-ffhzg2:hover {
        transform: translateY(-6px);
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        border-color: #b3e5fc;
    }

    .stButton > button {
        background: linear-gradient(145deg, #a1c4fd, #c2e9fb);
        color: #1a237e;
        border-radius: 12px;
        padding: 0.8em 1.4em;
        font-weight: 600;
        font-size: 1rem;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 5px 15px rgba(161, 196, 253, 0.4);
        border: none;
    }

    .stButton > button:hover {
        background: linear-gradient(145deg, #89d4cf, #6e8efb);
        color: white;
        transform: scale(1.05);
        box-shadow: 0 8px 25px rgba(126, 203, 255, 0.6);
    }

    .stFileUploader label {
        color: #37474f;
        font-weight: bold;
        font-size: 1rem;
    }

    .stFileUploader:hover label {
        color: #00acc1;
        transition: color 0.3s ease;
    }

    .css-5rimss {
        background-color: #f3f7fa;
        padding: 16px;
        border-radius: 14px;
        border: 1px solid #cfd8dc;
        transition: all 0.3s ease;
    }

    .css-5rimss:hover {
        box-shadow: 0 10px 30px rgba(173, 216, 230, 0.3);
        transform: scale(1.02);
    }
    </style>


""", unsafe_allow_html=True)

st.title("🧠 Multi-Agent Medical Image Analyser")
st.markdown("Analyze X-rays,Scans and previous reports using specialized AI agents")

uploaded_xray = st.file_uploader("Upload an X-ray Image (JPG, JPEG, PNG):", type=["jpg", "jpeg", "png"])
uploaded_report = st.file_uploader("Upload Previous Medical Report (TXT or PDF):", type=["txt", "pdf"])

# === Generate Button ===
if uploaded_xray:
    st.image(uploaded_xray, caption="Uploaded Medical Image", use_container_width=True)
if st.button("Run Multi-Agent Analysis"):
    if uploaded_xray:
        st.subheader("Analysis")
        image_data = uploaded_xray.getvalue()
        image_parts = [{"mime_type": "image/jpeg", "data": image_data}]
        xray_model = genai.GenerativeModel("gemini-1.5-pro-002", generation_config=generation_config, safety_settings=safety_setting)
        xray_response = xray_model.generate_content([image_parts[0], xray_prompt])
        st.markdown("*Findings:*")
        st.success("Analysis generated successfully!")
        st.markdown(xray_response.text if xray_response else "No response from X-ray agent.")
    else:
        st.warning("Please upload an X-ray image.")

    if uploaded_report:
        st.subheader("Insights from Medical History")
    if uploaded_report.type == "application/pdf":
        import fitz  # PyMuPDF
        pdf = fitz.open(stream=uploaded_report.read(), filetype="pdf")
        text = "\n".join([page.get_text() for page in pdf])
    else:
        text = uploaded_report.read().decode("utf-8")

    if text.strip():  # Ensure it's not empty or just spaces
        history_model = genai.GenerativeModel("gemini-1.5-pro-002", generation_config=generation_config, safety_settings=safety_setting)
        history_response = history_model.generate_content([text, history_prompt,xray_response.txt])
        st.markdown("*Insights from History:*")
        st.markdown(history_response.text if history_response else "No response from history agent.")
    else:
        st.error("Uploaded report is empty or unreadable. Please try another file.")

