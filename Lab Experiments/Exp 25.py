from google import genai
client = genai.Client(api_key="AQ.Ab8RN6KPPnnQLcpCaM16e80vdjx15ZjCY88pkP2H98EJazyZSA")
prompt = input("Enter your prompt: ")
response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=prompt
)
print("\nGenerated Text:")
print(response.text)
