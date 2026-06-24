from google import genai

client = genai.Client(api_key="")

alert = str(input("Enter the security alert details: "))

prompt = f"""
You are a SOC Analyst.

Analyze the security alert below.

Alert:
{alert}

Provide:

1. Incident Summary
2. Severity (Low/Medium/High/Critical)
3. MITRE ATT&CK Technique
4. Recommended Actions
"""

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
)

print(response.text)