from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyBP000QDKUVwZQLy98Zfbs6q0g5gwWbXy8")

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="fale sobre o ramo de desing de moda")
print(response.text)