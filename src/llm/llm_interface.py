import requests
import json
import gradio as gr

url = "http://localhost:11434/api/generate"

conversation_history = []

headers = {
  'Content-type': "dolphin2.2-mistral",
}

def generate_response(prompt):
  conversation_history.append(prompt)

  full_prompt = "\n".join(conversation_history)

  data = {
    "model": "security",
    "stream": False,
    "prompt": full_prompt,
  }

  response = requests.post(url, data=json.dumps(data), headers=headers)

  if response.status_code == 200:
    response_text = response.text
    data = json.loads(response_text)
    actual_response = data["response"]
    conversation_history.append(actual_response)
    return actual_response
  else:
    print("Error: ", response.status_code, response.text)
    return "Error: " + str(response.status_code)

iface = gr.Interface(
  fn=generate_response,
  inputs="text",
  outputs="text")

iface.launch()