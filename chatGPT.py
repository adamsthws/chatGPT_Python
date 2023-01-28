import os
import sys
import openai

# Load your API key from an environment variable
openai.api_key=os.environ['CHATGPT_API_KEY']

# Load your API key directly
#openai.api_key="xxxxxxxxxxxxxxxxxxx"

# Defines the ChatGPT model to use:
model="text-davinci-003" # most capable, highest cost
#model="text-curie-001"
#model="text-babbage-001"
#model="text-ada-001" # lowest cost

# Get the temperature from user input:
temp_prompt=input("What temperature? -Choose between 0 and 1 - Leave blank for 0.5 : ")
# Temperature error handling...
# Function to test if the users input for temperature is a usable number:
def convertable_to_float(user_temp_input):
    try:
        result = float(user_temp_input)
        return True
    except ValueError:
        return False
temperror="Error: Temperature must be a number between 0 and 1 - eg 0.5"
if convertable_to_float(temp_prompt)==False or float(temp_prompt)<0 or float(temp_prompt)>1:
        sys.exit(temperror)
# If user's input is blank, use a temperature of 0.5:
elif temp_prompt=="":
        temp=0.5
# Set temperature from users's selection:
else: temp=float(temp_prompt)

# Get the ChatGPT prompt from user input:
prompt=input("-------------------\nPrompt me like you mean it, you rotten human!\n     : ")

# Define the ChatGPT API function:
def chatGPT(prompt):
        response = openai.Completion.create(
                model=model,
                prompt=prompt,
                temperature=temp,
                max_tokens=1000
                )
        return str.strip(response['choices'][0]['text']), response['usage']['total_tokens']

# Returns the ChatGPT response to the user:
(res, usage) = chatGPT(prompt)
print("-------------------\n"+res)
print("-------------------\nTokens used: "+str(usage))
print("Temperature: "+str(temp))
