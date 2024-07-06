import os
import PIL
import google.generativeai as genai
import json
# do not reveal your api key when submitting the assignment
GOOGLE_API_KEY=os.environ.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)
dish_list = []

def list_genai_models():
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            print(m.name)


def read_file_as_string(filename, dish):
  # Append kitchen.txt, input.json, and prompt.txt
  with open("kitchen.txt", "r") as f:
     kitchen_content = f.read()
  f.close()
  with open("input.json", "r") as f:
    input_content = f.read()
    input_list = f.readlines()
    for line in input_list:
      if "dish" in line:
        dish_list.append(line)
  f.close()
  with open(filename, "r") as f:
    content = f.read()
  f.close()
  content = content.replace("<DISH_NAME>", dish)
  return kitchen_content + '\n' + input_content + '\n' + content


def detect_object(model, filepath):
    img = PIL.Image.open(filepath)
    prompt = "list objects in the image in this way: 1. ing 2. ing 3. ing etc"
    response = model.generate_content([prompt, img])
    print(response.text)

if __name__ == "__main__":
  model = genai.GenerativeModel('gemini-1.0-pro-latest')
  # Extract dish names from the input.json file
  with open("input.json", "r") as f:
    input_list = f.readlines()
    for line in input_list:
      if "dish" in line:
        templine = line.rstrip('\n')
        templine = templine.split(":")
        newtempline = templine[1].lstrip()
        newtempline = newtempline.replace(",", "")
        newtempline = newtempline.replace("\"", "")
        dish_list.append(newtempline)
  f.close()
  # Output json file from prompt response
  file_complete = 0
  for dish in dish_list:
    prompt = read_file_as_string("prompt.txt", dish)
    response = model.generate_content(prompt)
    filename = dish + ".json"
    with open(filename, "w") as f:
      f.write(response.text)
    f.close()
    file_complete += 1
    print("Files generated: "+str(file_complete)+"/31")
  print("All output files have been generated!")