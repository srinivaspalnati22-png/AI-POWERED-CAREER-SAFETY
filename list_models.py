import google.generativeai as genai
import os

GEMINI_API_KEY = "AIzaSyBPMlm4y9E0XTFSJCVOilbq1ECD_hHixAw"
genai.configure(api_key=GEMINI_API_KEY)

for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)
