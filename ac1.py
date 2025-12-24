import os
from google import generativeai as g
from google.generativeai import types

client=g.configure(api_key="AIzaSyAhKCXXHgbr8f9Ld0NPzLuF0jKnfESUz2A")

def genearte_response(prompt,temperature=0.3):
    try:
        contents=[types.Content(role="user",parts=[types.Part.from_text(text=prompt)])]
        config_params=types.GenerateContentConfig(temperature=temperature)
        response=client.models.generate_content(model="gemini-2.0-flash",contents=contents,config=config_params)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
    
def reinforcement_learning_activity():
    print("\n=== REINFORCEMENT LEARNING ACTIVITY ==\n")

    prompt=input("Enter a prompt for the AI model (e.g., 'Describe the lion'):")
    initial_response=genearte_response(prompt)
    print(f"\nIntial AI Response: {initial_response}")

    rating=int(input("Rate the response from 1 (bad) to 5 (good):"))
    feedback=input("Provide feedback for improvement:")

    improved_response=f"{initial_response} (Improved with your feedback :{feedback})"
    print(f"\nImproved AI Repsonse: {improved_response}")

    print("\nReflection:")
    print("1.HOw did the model's response improve with feedback?")
    print("2. How does reinforcement learning help AI to improve its performance over time?")

def role_based_prompt_activity():
    print("\n=== ROLE-BAED PROMPTS ACTIVITY ===\n")

    category=input("Enter a category (e.g., science,history,math):")
    item=input(f"Enter a specific {category} topic (e.g., 'photosynthesiis' for science):")

    teacher_prompt=f"Yoy are a teacher.Explain {item} in simple terms."
    expert_prompt=f"You are an expert in {category}. Explain {item} in a detailed,technical manner."

    teacher_response=genearte_response(teacher_prompt)
    expert_response=genearte_response(expert_prompt)

    print(f"\n Teacher's Perspective ---\n{teacher_response}")
    print(f"\n Expert's Perspective ---\n{expert_response}")

    print("\nReflection:")
    print("1. How did the AI's response differ between the teacher'sand expert's perspectives?")
    print("2. How can role-based prompts help tailor AI responses for different contexts?")

def run_activity():
    print("\n=== AI LEARNING ACTIVITY ===")

    activity_choice=input("Which activity would you like to run? (1. Reinforcement Learning, 2: Role-Based Prompt):")

    if activity_choice=="1":
        reinforcement_learning_activity()
    elif activity_choice=="2":
        role_based_prompt_activity()
    else:
        print("Invalid choie. Please choose either 1 or 2.")

if __name__=="__main__":
    run_activity()
