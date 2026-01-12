from table_extraction_word import extract_all_tables_data
from dedupe import remove_duplicates_nested
from google import genai
from google.genai import types
from pathfinding import get_single_word_document_path
from dotenv import load_dotenv
import os

# Create a prompt text file named "prompttext.txt" in the same directory as this script. There you can describe the
# data and desired behavior of the model in more detail.
general_prompt = open("prompttext.txt", "r").read()

word_path = get_single_word_document_path('Input')



file_path = str(word_path)
# Questions should be in tables only, often First Table contains project description or other non relevant data.
# Hence skip_first_table is set to True
extracted_data = extract_all_tables_data(file_path, skip_first_table=True)

deduped = remove_duplicates_nested(extracted_data)



structured_concatenated_list =[ 
      [
            " ".join(jnnermost_strings)
            for jnnermost_strings in outer_group
      ]
      for outer_group in deduped
]



# Ab hier relevante Teil für die API
# API sollte das einzige sein was sich ändern kann. Die Dokumentation ist hier: https://ai.google.dev/gemini-api/docs?hl=de
# Ansonsten wenn alles von requirements.txt installiert ist, sollte es funktionieren. nur google-auth==2.41.1 und google-genai==1.46.0 müssen eventuell geupdatet werden.




load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = GEMINI_API_KEY)


print("Sende Anfrage an die API, bitte warten...")

response = client.models.generate_content(
    model="gemini-2.5-flash",     
    contents="Return a plain2form questionare based on the following table data: " + str(structured_concatenated_list),
    config=types.GenerateContentConfig(
          system_instruction= general_prompt
))

if response.text is None: 
    raise RuntimeError("Keine Antwort von der API erhalten")

with open("Output/response.txt", "w") as rfile: 
    rfile.write(response.text)

print("Programmierung erledigt, schau in den Output Ordner für die Antwort!")

