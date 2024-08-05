# ai_final_project_kojo_lemaire_veronica_obenewaa

# Description
This repository houses the files that make up the AI dietitian app, which are:
1. app.py: the frontend layer of the app, where the user can send prompts to the model concerning diet and health-related content (weight, dietary needs, health goals, etc), and the model responds in text outputs.
2. model.py: the model file. It is a Llama 3 LLM fine-tuned with data from a patient-dietitian conversational dataset.

# How to run app
The app is run in the following way:
1. In the directory where the files (app and model) are stored, enter the following command into the shell of the operating system being used:
<kbd>python -m streamlit run app.py</kbd>
2. The app should be run on the default browser, with the user being able to interact with the AI dietitian. To close the app, simply close the browser window the app is run on.
