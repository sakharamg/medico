import google.generativeai as genai
import os
from datetime import datetime
import uuid
import json

diseases_rarity= [
  {"disease": "Common Cold", "rarity": "Common"},
  {"disease": "Flu", "rarity": "Common"},
  {"disease": "Hypertension", "rarity": "Common"},
  {"disease": "Diabetes Type 2", "rarity": "Common"},
  {"disease": "Asthma", "rarity": "Common"},
  {"disease": "Migraine", "rarity": "Common"},
  {"disease": "Gastritis", "rarity": "Common"},
  {"disease": "Anemia", "rarity": "Common"},
  {"disease": "Pneumonia", "rarity": "Common"},
  {"disease": "Chronic Fatigue Syndrome", "rarity": "Uncommon"},
  {"disease": "Osteoarthritis", "rarity": "Common"},
  {"disease": "Eczema", "rarity": "Common"},
  {"disease": "Allergies", "rarity": "Common"},
  {"disease": "Heart Disease", "rarity": "Common"},
  {"disease": "COPD", "rarity": "Common"},
  {"disease": "Thyroid Disorder", "rarity": "Common"},
  {"disease": "Peptic Ulcer", "rarity": "Common"},
  {"disease": "Urinary Tract Infection (UTI)", "rarity": "Common"},
  {"disease": "Gallstones", "rarity": "Common"},
  {"disease": "Irritable Bowel Syndrome (IBS)", "rarity": "Common"},
  {"disease": "Depression", "rarity": "Common"},
  {"disease": "Anxiety", "rarity": "Common"},
  {"disease": "Schizophrenia", "rarity": "Uncommon"},
  {"disease": "Parkinson's Disease", "rarity": "Uncommon"},
  {"disease": "Multiple Sclerosis", "rarity": "Uncommon"},
  {"disease": "Alzheimer's Disease", "rarity": "Uncommon"},
  {"disease": "Tuberculosis", "rarity": "Uncommon"},
  {"disease": "Lung Cancer", "rarity": "Common"},
  {"disease": "Leukemia", "rarity": "Uncommon"},
  {"disease": "HIV/AIDS", "rarity": "Common"},
  {"disease": "Sickle Cell Anemia", "rarity": "Uncommon"},
  {"disease": "Cystic Fibrosis", "rarity": "Uncommon"},
  {"disease": "Hemophilia", "rarity": "Rare"},
  {"disease": "Huntington's Disease", "rarity": "Rare"},
  {"disease": "Kawasaki Disease", "rarity": "Rare"},
  {"disease": "Rheumatoid Arthritis", "rarity": "Uncommon"},
  {"disease": "Fibromyalgia", "rarity": "Uncommon"},
  {"disease": "Meningitis", "rarity": "Uncommon"},
  {"disease": "Tuberculosis", "rarity": "Uncommon"},
  {"disease": "Prostate Cancer", "rarity": "Common"},
  {"disease": "Cervical Cancer", "rarity": "Common"},
  {"disease": "Ovarian Cancer", "rarity": "Uncommon"},
  {"disease": "Endometriosis", "rarity": "Uncommon"},
  {"disease": "Chlamydia", "rarity": "Common"},
  {"disease": "Gonorrhea", "rarity": "Common"},
  {"disease": "Syphilis", "rarity": "Uncommon"},
  {"disease": "Psoriasis", "rarity": "Uncommon"},
  {"disease": "Lupus", "rarity": "Uncommon"},
  {"disease": "Crohn’s Disease", "rarity": "Uncommon"},
  {"disease": "Celiac Disease", "rarity": "Uncommon"},
  {"disease": "Ehlers-Danlos Syndrome", "rarity": "Rare"},
  {"disease": "Marfan Syndrome", "rarity": "Rare"},
  {"disease": "Amyotrophic Lateral Sclerosis (ALS)", "rarity": "Rare"},
  {"disease": "Prion Disease", "rarity": "Rare"},
  {"disease": "Tay-Sachs Disease", "rarity": "Rare"},
  {"disease": "Wilson's Disease", "rarity": "Rare"},
  {"disease": "Cushing's Syndrome", "rarity": "Rare"},
  {"disease": "Addison's Disease", "rarity": "Rare"},
  {"disease": "Achondroplasia", "rarity": "Rare"},
  {"disease": "SARS", "rarity": "Rare"},
  {"disease": "Ebola", "rarity": "Rare"},
  {"disease": "Zika Virus", "rarity": "Rare"},
  {"disease": "Rabies", "rarity": "Rare"},
  {"disease": "Yellow Fever", "rarity": "Rare"},
  {"disease": "Smallpox", "rarity": "Rare"},
  {"disease": "Diphtheria", "rarity": "Rare"},
  {"disease": "Polio", "rarity": "Rare"},
  {"disease": "Typhoid Fever", "rarity": "Rare"},
  {"disease": "Malaria", "rarity": "Uncommon"},
  {"disease": "Hepatitis B", "rarity": "Uncommon"},
  {"disease": "Hepatitis C", "rarity": "Uncommon"},
  {"disease": "Mumps", "rarity": "Rare"},
  {"disease": "Measles", "rarity": "Uncommon"},
  {"disease": "Rubella", "rarity": "Rare"},
  {"disease": "Dengue Fever", "rarity": "Uncommon"},
  {"disease": "Cholera", "rarity": "Rare"},
  {"disease": "Typhus", "rarity": "Rare"},
  {"disease": "Legionnaire's Disease", "rarity": "Rare"},
  {"disease": "Sepsis", "rarity": "Uncommon"},
  {"disease": "Lymphoma", "rarity": "Uncommon"},
  {"disease": "Sarcoidosis", "rarity": "Rare"},
  {"disease": "Cystitis", "rarity": "Common"},
  {"disease": "Psoriatic Arthritis", "rarity": "Uncommon"},
  {"disease": "Bipolar Disorder", "rarity": "Common"},
  {"disease": "Schizoaffective Disorder", "rarity": "Rare"},
  {"disease": "Narcolepsy", "rarity": "Rare"},
  {"disease": "Sleep Apnea", "rarity": "Common"},
  {"disease": "Restless Leg Syndrome", "rarity": "Uncommon"},
  {"disease": "Insomnia", "rarity": "Common"},
  {"disease": "Hemorrhoids", "rarity": "Common"},
  {"disease": "Cystic Acne", "rarity": "Common"},
  {"disease": "Polycystic Ovary Syndrome (PCOS)", "rarity": "Common"},
  {"disease": "Chronic Sinusitis", "rarity": "Common"},
  {"disease": "Bacterial Vaginosis", "rarity": "Common"},
  {"disease": "Panic Disorder", "rarity": "Common"},
  {"disease": "Dystonia", "rarity": "Rare"},
  {"disease": "Myasthenia Gravis", "rarity": "Rare"},
  {"disease": "Graves' Disease", "rarity": "Rare"},
  {"disease": "Autoimmune Hepatitis", "rarity": "Rare"},
  {"disease": "Sjögren’s Syndrome", "rarity": "Rare"}
]
diseases=[]
for e in diseases_rarity:
    diseases.append(e["disease"])

print("Imported Libraries")
API_KEY="AIzaSyCEM6U_KUPh03mG8T8eawsP4zZpkkORk-A"
os.environ['GEMINI_API_KEY'] = API_KEY
print("Key Loaded")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-flash")
print("Model Loaded")

prompt="""
Problem Statement: Medical assistant for edge devices that for SOS, appointments, reminders and reports

Booking Appointment:
1. User prompts his/her/their problems
2. Coordinator asks counter questions for gaining clarity 
3. Coordinator also checks recent complains of such symptoms using RAG
4. Based on symptoms, specialist along with
their available slots and on users schedule, a slot is presented to user
5. User says Yes or No
6. If yes: Booking stored in hospital DB
7. Irrespective of Yes and No: Also store the symptoms/complains in user DB (for later purposes for recurring usecases )

Example of trajectory:
{"id":123,"tools":[
{
  "Name": "analyze_symptoms",
  "Description": "Analyzes user-provided symptoms and suggest a medical specialization for disease e.g. cardiologist, dermetalogist, dietician, etc",
  "Parameters": [
    {"param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user."},
    {"param_name": "symptoms", "type": "string", "default": "None", "description": "The symptoms described by the user in natural language."}
  ],
  "Required Parameters": ["user_id", "symptoms"],
  "Returns": {
    "type": "dictionary",
    "description": {"analysis":"string containing detailed symptom analysis.","specialization":"specialization name for the disease}
  }
},
{
  "Name": "get_available_specialists",
  "Description": "Fetches a list of specialists based on analyzed symptoms and their availability.",
  "Parameters": [
    {"param_name": "symptoms", "type": "string", "default": "None", "description": "List of symptoms derived from user input."},
    {"param_name": "specialization", "type": "string", "default": "None", "description": "specialization name for the appointment"},
    {
      "param_name": "user_schedule", 
      "type": "object", 
      "default": "None", 
      "description": "User's preferred schedule for appointments in key-value pairs (e.g., {'date': 'YYYY-MM-DD', 'time_range': 'HH:MM-HH:MM'})."
    }
  ],
  "Required Parameters": ["symptoms", "user_schedule"],
  "Returns": {
    "type": "dictionary",
    "description": " returns single best schedule {specialist_id,name, available_slot including time in HH:MM-HH:MM format and date in DD/MM/YY format}."
  }
},
{
  "Name": "confirm_appointment",
  "Description": "Confirms an appointment slot and stores it in the hospital's database.",
  "Parameters": [
    {"param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user."},
    {"param_name": "specialist_id", "type": "string", "default": "None", "description": "Unique identifier for the chosen specialist."},
    {"param_name": "appointment_time_date", "type": "string", "default": "None", "description": "The selected time slot for the appointment as time in HH:MM-HH:MM format and date in DD/MM/YY format."}
  ],
  "Required Parameters": ["user_id", "specialist_id", "appointment_time"],
  "Returns": {
    "type": "boolean",
    "description": "Always returns True."
  }
},
{
  "Name": "save_appointment_history",
  "Description": "Saves appointment information in the user's database for later reference and recurring use cases.",
  "Parameters": [
    {"param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user."},
    {"param_name": "symptoms", "type": "string", "default": "None", "description": "The symptoms described by the user."},
    {"param_name": "specialist_id", "type": "string", "default": "None", "description": "Unique identifier for the chosen specialist."},
    {"param_name": "appointment_time_date", "type": "string", "default": "None", "description": "The selected time slot for the appointment as time in HH:MM-HH:MM format and date in DD/MM/YY format."}
  ],
  "Required Parameters": ["user_id", "symptoms", "specialist_id", "appointment_time_date" ],
  "Returns": {
    "type": "boolean",
    "description": "Always true"
  }
},
{
  "Name": "get_appointment_history",
  "Description": "Retrieves the user's appointment history for analysis and reminders.",
  "Parameters": [
    {"param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user."}
  ],
  "Required Parameters": ["user_id"],
  "Returns": {
    "type": "array",
    "description": "Array containing past appointment records."
  }
},

{
  "Name": "retrieve_past_complaints",
  "Description": "Fetches the user's past complaints matching the given symptoms for analysis and reference.",
  "Parameters": [
    {"param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user."},
    {"param_name": "symptoms", "type": "string", "default": "None", "description": "List of symptoms to search for in past complaints."},
    {"param_name": "date_range", "type": "object", "default": "None", "description": "Optional date range filter in the format {'start_date': 'YYYY-MM-DD', 'end_date': 'YYYY-MM-DD'}."}
  ],
  "Required Parameters": ["user_id", "symptoms"],
  "Returns": {
    "type": "array",
    "description": "Array of past complaints related to the specified symptoms."
  }
},
{
  "Name": "follow_up_with_user",
  "Description": "Initiates a follow-up interaction with the user based on their past complaints and current symptoms.",
  "Parameters": [
    {"param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user."},
    {"param_name": "past_complaints", "type": "array", "default": "[]", "description": "List of past complaints to reference during the follow-up."},
    {"param_name": "current_symptoms", "type": "string", "default": "None", "description": "Current symptoms reported by the user."},
    {"param_name": "preferred_contact_method", "type": "string", "default": "None", "description": "User's preferred method for follow-up (e.g., 'call', 'email', 'chat')."}
  ],
  "Required Parameters": ["user_id", "current_symptoms"],
  "Returns": {
    "type": "object",
    "description": "Details of the follow-up initiated, including method and next steps."
  }
},
{
  "Name": "store_symptoms",
  "Description": "Stores the symptoms reported by the user and initiates a follow-up process to gather additional details for a more accurate analysis.",
  "Parameters": [
    {
      "param_name": "user_id",
      "type": "string",
      "default": "None",
      "description": "Unique identifier for the user."
    },
    {
      "param_name": "symptoms",
      "type": "string",
      "default": "None",
      "description": "Symptoms of user."
    },
{"param_name": "timestamp", "type": "object", "default": "None", "description": "Save date and time of the event"
  ],
  "Required Parameters": ["user_id", "symptoms" ,"timestamp"],
  "Returns": {
    "type": "boolean",
    "description": "Status always true"
  }
}
],
{
  "interaction_trajectory": [
  {
    "from": "user",
    "value": "I've been having severe headaches and blurry vision for the past few days. Can I book an appointment?"
  },
  {
    "from": "assistant",
    "value": {
      "reason": "User has provided symptoms of headaches and blurry vision, indicating a potential medical issue.",
      "action": "Check if user has had similar complaints recently from memory."
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "retrieve_past_complaints",
      "parameters": {
        "user_id": "123",
        "symptoms": "headaches, blurry vision"
      }
    }
  },
  {
    "from": "caller",
    "value": {
      "result": [
        {
          "date": "2024-10-10",
          "symptoms": "mild headache and eye discomfort",
          "diagnosis": "eye strain"
        }
      ]
    }
  },
  {
    "from": "assistant",
    "value": {
      "reason": "The system found a prior complaint related to headaches and eye discomfort, which could help refine the diagnosis.",
      "action": "Suggest the best specialist based on current symptoms and past records."
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "get_available_specialists",
      "parameters": {
        "symptoms": "severe headaches, blurry vision",
        "user_schedule": {
          "date": "2024-11-22",
          "time_range": "09:00-17:00"
        }
      }
    }
  },
  {
    "from": "caller",
    "value": {
      "result": {
        "specialist_id": "456",
        "name": "Dr. Emily Carter (Neurologist)",
        "available_slot": {
          "date": "2024-11-22",
          "time": "10:30-11:00"
        }
      }
    }
  },
  {
    "from": "assistant",
    "value": {
      "reason": "Based on the analysis of symptoms and availability, Dr. Emily Carter is the best match for the user.",
      "action": "Suggest the user confirm the appointment for the available time slot."
    }
  },
  {
    "from": "user",
    "value": "Yes, please confirm."
  },
  {
    "from": "caller",
    "value": {
      "tool": "confirm_appointment",
      "parameters": {
        "user_id": "123",
        "specialist_id": "456",
        "appointment_time_date": "10:30-11:00, 22/11/2024"
      }
    }
  },
  {
    "from": "caller",
    "value": {
      "result": true
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "save_appointment_history",
      "parameters": {
        "user_id": "123",
        "symptoms": "severe headaches, blurry vision",
        "specialist_id": "456",
        "appointment_time_date": "10:30-11:00, 22/11/2024"
      }
    }
  },
  {
    "from": "caller",
    "value": {
      "result": true
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "store_symptoms",
      "parameters": {
        "user_id": "123",
        "symptoms": "severe headaches, blurry vision",
        "timestamp": "2024-11-21T15:30:00"
      }
    }
  },
  {
    "from": "caller",
    "value": {
      "result": true
    }
  },
  {
    "from": "assistant",
    "value": {
      "reason": "The appointment has been confirmed, and the symptoms have been stored for future reference.",
      "action": "Inform the user about the confirmed appointment and the stored symptoms."
    }
  },
  {
    "from": "assistant",
    "value": "Your appointment with Dr. Emily Carter is confirmed for 10:30 AM on 2024-11-22. We've also stored your symptoms for future reference. Let me know if there's anything else I can assist you with!"
  }
]
}
An example of examplee trajectory:
[
  {
    "from": "user",
    "value": "I've been having severe headaches and blurry vision for the past few days. Can I book an appointment?"
  },
  {
    "from": "planner",
    "value": {
      "reason": "User has provided symptoms of headaches and blurry vision, indicating a potential medical issue.",
      "action": "Check if user has had similar complaints recently from memory."
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "retrieve_past_complaints",
      "parameters": {
        "user_id": "123",
        "symptoms": "headaches, blurry vision"
      }
    }
  },
  {
    "from": "observation",
    "value": {
      "result": [
        {
          "date": "2024-10-10",
          "symptoms": "mild headache and eye discomfort",
          "diagnosis": "eye strain"
        }
      ]
    }
  },
  {
    "from": "planner",
    "value": {
      "reason": "The system found a prior complaint related to headaches and eye discomfort, which could help refine the diagnosis.",
      "action": "Suggest the best specialist based on current symptoms and past records."
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "get_available_specialists",
      "parameters": {
        "symptoms": "severe headaches, blurry vision",
        "user_schedule": {
          "date": "2024-11-22",
          "time_range": "09:00-17:00"
        }
      }
    }
  },
  {
    "from": "observation",
    "value": {
      "result": {
        "specialist_id": "456",
        "name": "Dr. Emily Carter (Neurologist)",
        "available_slot": {
          "date": "2024-11-22",
          "time": "10:30-11:00"
        }
      }
    }
  },
  {
    "from": "planner",
    "value": {
      "reason": "Based on the analysis of symptoms and availability, Dr. Emily Carter is the best match for the user.",
      "action": "Suggest the user confirm the appointment for the available time slot."
    }
  },
  {
    "from": "user",
    "value": "Yes, please confirm."
  },
  {
    "from": "caller",
    "value": {
      "tool": "confirm_appointment",
      "parameters": {
        "user_id": "123",
        "specialist_id": "456",
        "appointment_time_date": "10:30-11:00, 22/11/2024"
      }
    }
  },
  {
    "from": "observation",
    "value": {
      "result": true
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "save_appointment_history",
      "parameters": {
        "user_id": "123",
        "symptoms": "severe headaches, blurry vision",
        "specialist_id": "456",
        "appointment_time_date": "10:30-11:00, 22/11/2024"
      }
    }
  },
  {
    "from": "observation",
    "value": {
      "result": true
    }
  },
  {
    "from": "caller",
    "value": {
      "tool": "store_symptoms",
      "parameters": {
        "user_id": "123",
        "symptoms": "severe headaches, blurry vision",
        "timestamp": "2024-11-21T15:30:00"
      }
    }
  },
  {
    "from": "observation",
    "value": {
      "result": true
    }
  },
  {
    "from": "planner",
    "value": {
      "reason": "The appointment has been confirmed, and the symptoms have been stored for future reference.",
      "action": "Inform the user about the confirmed appointment and the stored symptoms."
    }
  },
  {
    "from": "planner",
    "value": "Your appointment with Dr. Emily Carter is confirmed for 10:30 AM on 2024-11-22. We've also stored your symptoms for future reference. Let me know if there's anything else I can assist you with!"
  }
]
You only speak json. The output should strictly follow the ReAct reasoning framework i.e. {"reason":"" , "action":""} in value "planner". Generate another such "interaction_trajectory" strictly in JSON format where trajectory starts with user complaining about some symptoms for which dietician is needed without explicitly mentioning need of dietician. 
"""

for i in range(2000):
  try:
      response = model.generate_content(prompt)
      print(response.text)

      # Split the string into lines
      lines = response.text.strip().split('\n')

      # Remove the first and last lines
      trimmed_lines = lines[1:-1]

      # Join the remaining lines back into a single string
      trimmed_string = '\n'.join(trimmed_lines)

      data=json.loads(trimmed_string)
      print(data)

      # Generate a filename with the current timestamp and a UUID
      current_timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
      unique_id = uuid.uuid4().hex  # Generate a unique identifier
      filename = f'data_gen/data/diet/{current_timestamp}_{unique_id}.txt'

      # Save the response text to a file with the unique filename
      with open(filename, 'w') as json_file:
          json.dump(data, json_file, indent=4)
      print(f"Output saved to {filename}")
  except:
      continue



