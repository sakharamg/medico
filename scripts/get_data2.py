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
API_KEY="AIzaSyCEZh1dfMW5hJ1d-svcbEUlXasZENyIzKE"
os.environ['GEMINI_API_KEY'] = API_KEY
print("Key Loaded")

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

model = genai.GenerativeModel(model_name="gemini-1.5-pro")
print("Model Loaded")

prompt="""

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
  "Name": "get_available_specialists",
  "Description": "Fetches a list of specialists and their availability.",
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
{ "Name": "notify_user", "Description": "Sends a notification to the user ", "Parameters": [ { "param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user." }, { "param_name": "message", "type": "string", "default": "None", "description": "The notification message to send." }, ], "Required Parameters": ["user_id", "message"], "Returns": { "type": "boolean", "description": "Always returns status as True" } },
{ "Name": "get_input_from_user", "Description": "Collects input from the user for specified parameters.", "Parameters": [ { "param_name": "user_id", "type": "string", "default": "None", "description": "Unique identifier for the user." }, { "param_name": "questions", "type": "string", "default": "[]", "description": "Question to ask the user." }, ], "Required Parameters": ["user_id", "questions"], "Returns": { "type": "string", "description": "User's response to the specified questions." } },
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
            "value": "I've been experiencing severe stomach pain, nausea, and vomiting for the past two days.  It's really debilitating."
        },
        {
            "from": "planner",
            "value": {
                "reason": "User reports severe stomach pain, nausea, and vomiting, suggesting a potential gastrointestinal issue.",
                "action": "Check for past similar complaints using the retrieve_past_complaints tool."
            }
        },
        {
            "from": "caller",
            "value": {
                "tool": "retrieve_past_complaints",
                "parameters": {
                    "user_id": "789",
                    "symptoms": "stomach pain, nausea, vomiting"
                }
            }
        },
        {
            "from": "observation",
            "value": {
                "result": [
                    {
                        "date": "2024-09-15",
                        "symptoms": "mild stomach discomfort, indigestion",
                        "diagnosis": "indigestion"
                    }
                ]
            }
        },
        {
            "from": "planner",
            "value": {
                "reason": "Past records show mild gastrointestinal discomfort but nothing as severe as the current complaint.  The severity warrants a consultation with a gastroenterologist.",
                "action": "Use the get_available_specialists tool to find a gastroenterologist with available appointments."
            }
        },
        {
            "from": "caller",
            "value": {
                "tool": "get_available_specialists",
                "parameters": {
                    "symptoms": "severe stomach pain, nausea, vomiting",
                    "specialization": "gastroenterologist",
                    "user_schedule": {
                        "date": "2024-11-25",
                        "time_range": "13:00-18:00"
                    }
                }
            }
        },
        {
            "from": "observation",
            "value": {
                "result": {
                    "specialist_id": "987",
                    "name": "Dr. Alex Ramirez (Gastroenterologist)",
                    "available_slot": {
                        "date": "2024-11-25",
                        "time": "14:30-15:00"
                    }
                }
            }
        },
        {
            "from": "planner",
            "value": {
                "reason": "Dr. Ramirez is available on the user's preferred date and time.",
                "action": "Suggest the appointment to the user and proceed with booking if confirmed. Dr. Alex Ramirez (Gastroenterologist) on 2024-11-25 between 14:30-15:00"
        },
        {
            "from": "caller",
            "value": {
                "tool": "get_input_from_user",
                "parameters": {
                    "question": "Dr. Alex Ramirez (Gastroenterologist) has an opening at 2:30 PM on November 25th. Would you like to schedule an appointment?",
                }
            }
        },
        {
            "from": "observation",
            "value": {
                "result": {
                    "user": "Yes, please"
            }
        },
        {
            "from": "planner",
            "value": {
                "reason": "User has confirmed the appointment",
                "action": "I should confirm the appointment"
        },
        {
            "from": "caller",
            "value": {
                "tool": "confirm_appointment",
                "parameters": {
                    "user_id": "789",
                    "specialist_id": "987",
                    "appointment_time_date": "14:30-15:00, 25/11/2024"
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
                "reason": "Appointment confirmed. Next, I should save the aapointment history.",
                "action": "Save the appointment history."
            }
        },
        {
            "from": "caller",
            "value": {
                "tool": "save_appointment_history",
                "parameters": {
                    "user_id": "789",
                    "symptoms": "severe stomach pain, nausea, vomiting",
                    "specialist_id": "987",
                    "appointment_time_date": "14:30-15:00, 25/11/2024"
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
                "reason": "Appointment confirmed and stored.",
                "action": "Also store the current symptoms for future reference."
            }
        },
        {
            "from": "caller",
            "value": {
                "tool": "store_symptoms",
                "parameters": {
                    "user_id": "789",
                    "symptoms": "severe stomach pain, nausea, vomiting",
                    "timestamp": "2024-11-23T10:00:00"
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
                "reason": "Appointment confirmed and symptoms stored.",
                "action": "Inform the user of the successful booking."
            }
        },
        {
            "from": "caller",
            "value": {
                "tool": "notify_user",
                "parameters": {
                    "user_id": "789",
                    "symptoms": "Your appointment with Dr. Ramirez is confirmed for 2:30 PM on November 25th. Your symptoms have been recorded for future reference.",
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
                "reason": "The task is completed successfully.",
                "action": "<END>"
            }
        }
    ]
}
You only speak json. The output should strictly follow the ReAct reasoning framework i.e. {"reason":"" , "action":""} in "value" of "planner". Generate only "interaction_trajectory". The ineraction trajectory begins with user then iterates between planner -> caller -> observation -> planner , strictly in the sequence as showin in above example. It must strictly in JSON format where trajectory starts with user complaining about some symptoms for . 
"""
diseases = [
    "Influenza",
    "Diabetes Mellitus",
    "Hypertension",
    "Asthma",
    "Coronary Artery Disease",
    "Stroke",
    "HIV/AIDS",
    "Tuberculosis",
    "Hepatitis B",
    "Hepatitis C",
    "Dengue Fever",
    "Malaria",
    "Chickenpox",
    "Measles",
    "Mumps",
    "Rubella",
    "Zika Virus",
    "Ebola",
    "COVID-19",
    "Cancer",
    "Alzheimer's Disease",
    "Parkinson's Disease",
    "Arthritis",
    "Lupus",
    "Multiple Sclerosis",
    "Crohn's Disease",
    "Ulcerative Colitis",
    "Gastroesophageal Reflux Disease (GERD)",
    "Celiac Disease",
    "Anemia",
    "Bronchitis",
    "Pneumonia",
    "Sinusitis",
    "Chlamydia",
    "Gonorrhea",
    "Syphilis",
    "Herpes",
    "Human Papillomavirus (HPV)",
    "Tetanus",
    "Rabies",
    "Polio",
    "Yellow Fever",
    "Smallpox",
    "Typhoid Fever",
    "Leprosy",
    "Plague",
    "Hemophilia",
    "Sickle Cell Disease",
    "Thalassemia",
    "Hemochromatosis",
    "Meningitis",
    "Encephalitis",
    "Glaucoma",
    "Cataracts",
    "Macular Degeneration",
    "Otitis Media",
    "Tonsillitis",
    "Appendicitis",
    "Hemorrhoids",
    "Diverticulitis",
    "Irritable Bowel Syndrome (IBS)",
    "Kidney Stones",
    "Chronic Kidney Disease",
    "Renal Failure",
    "Osteoporosis",
    "Osteopenia",
    "Rheumatoid Arthritis",
    "Gout",
    "Psoriasis",
    "Eczema",
    "Vitiligo",
    "Alopecia",
    "Hypothyroidism",
    "Hyperthyroidism",
    "Cushing's Syndrome",
    "Addison's Disease",
    "Prostate Cancer",
    "Breast Cancer",
    "Lung Cancer",
    "Colorectal Cancer",
    "Pancreatic Cancer",
    "Liver Cancer",
    "Skin Cancer",
    "Melanoma",
    "Leukemia",
    "Lymphoma",
    "Myeloma",
    "Basal Cell Carcinoma",
    "Squamous Cell Carcinoma",
    "Esophageal Cancer",
    "Gastric Cancer",
    "Ovarian Cancer",
    "Cervical Cancer",
    "Endometrial Cancer",
    "Bladder Cancer",
    "Kidney Cancer",
    "Testicular Cancer",
    "Thyroid Cancer",
    "Mesothelioma",
    "Brain Tumors",
    "Spinal Cord Tumors",
    "Heart Failure",
    "Atrial Fibrillation",
    "Cardiomyopathy",
    "Angina",
    "Atherosclerosis",
    "Pericarditis",
    "Myocarditis",
    "Endocarditis",
    "Congenital Heart Disease",
    "Valvular Heart Disease",
    "Peripheral Artery Disease",
    "Deep Vein Thrombosis",
    "Pulmonary Embolism",
    "Varicose Veins",
    "Hypertensive Heart Disease",
    "Coronary Microvascular Disease",
    "Dyslipidemia",
    "Familial Hypercholesterolemia",
    "Hypertrophic Cardiomyopathy",
    "Dilated Cardiomyopathy",
    "Restrictive Cardiomyopathy",
    "Takotsubo Cardiomyopathy",
    "Sleep Apnea",
    "Insomnia",
    "Narcolepsy",
    "Restless Leg Syndrome",
    "Epilepsy",
    "Migraine",
    "Cluster Headache",
    "Tension Headache",
    "Trigeminal Neuralgia",
    "Multiple System Atrophy",
    "Amyotrophic Lateral Sclerosis (ALS)",
    "Huntington's Disease",
    "Dystonia",
    "Myasthenia Gravis",
    "Guillain-Barre Syndrome",
    "Spinal Muscular Atrophy",
    "Muscular Dystrophy",
    "Fibromyalgia",
    "Chronic Fatigue Syndrome",
    "Complex Regional Pain Syndrome",
    "Temporomandibular Joint Disorders",
    "Sjogren's Syndrome",
    "Raynaud's Disease",
    "Scleroderma",
    "Mixed Connective Tissue Disease",
    "Behcet's Disease",
    "Wegener's Granulomatosis",
    "Giant Cell Arteritis",
    "Polyarteritis Nodosa",
    "Sarcoidosis"
]
prefixes=["Problem Statement: Edge device medical assistant for initiating SOS alerts, scheduling appointments, setting reminders, and managing medical reports.",
"Problem Statement: Developing a medical assistant for edge devices to handle SOS emergencies, appointment scheduling, reminders, and report management.",
"Problem Statement: Creating a medical assistant on edge devices for SOS alerts, managing appointments, sending reminders, and handling patient reports.",
"Problem Statement: Medical assistant implementation on edge devices for emergency SOS, appointment management, reminders, and report generation.",
"Problem Statement: Edge device-based medical assistant for SOS alert activation, appointment coordination, reminder notifications, and report handling.",
"Problem Statement: Designing a medical assistant for edge devices to manage SOS alerts, appointments, reminders, and patient reports.",
"Problem Statement: Edge device medical assistant for providing SOS alerts, managing appointments, reminders, and handling medical reports.",
"Problem Statement: Development of a medical assistant on edge devices for managing SOS alerts, scheduling appointments, sending reminders, and handling reports.",
"Problem Statement: Implementing a medical assistant for edge devices that supports SOS alerts, appointment scheduling, reminders, and report management.",
"Problem Statement: Edge device-based medical assistant for triggering SOS alerts, managing appointments, sending reminders, and handling patient medical reports."]
for prefix in prefixes:
    for disease in diseases:
        print(disease)
        try:
            response = model.generate_content(prefix+"\n"+prompt+disease + " without necessarily explicitly mentioning about the disease.")
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
            filename = f'data_gen/data/new/out/{current_timestamp}_{unique_id}.txt'

            # Save the response text to a file with the unique filename
            with open(filename, 'w') as json_file:
                json.dump(data, json_file, indent=4)
            print(f"Output saved to {filename}")
        except:
            continue



