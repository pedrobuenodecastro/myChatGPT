# request GPT-3 to generate a response to a given prompt
# and return the response
import openai
import time
import os

# set the log file
logFile = "/app/log/myChatGPT.log"

# set the API key from file openaiAPIkey
openai.api_key = open("/app/key/openaiAPIkey").read()

# set the engine from environment variable ENGINE
try:
    engine = os.environ["ENGINE"]
except:
    engine = "text-davinci-001"
    print("Warning: ENGINE environment variable not set. Using default engine: " + engine)

# set the temperature
temperature = 0.9

# set the max tokens
max_tokens = 2000

# set the stop sequence
stop = '.'

# set the prompt from environment variable PROMPT
# prompt = os.environ["PROMPT"]

# request GPT-3 to generate a response to a given prompt
# and return the response
def generateResponse(prompt):

    # request GPT-3 to generate a response to a given prompt
    response = openai.Completion.create(
        engine = engine,
        temperature = temperature,
        max_tokens = max_tokens,
        prompt = prompt
    )

    # return the response
    return response

# log the response
def logResponse(prompt, response):
    # create and append to the log file if it does not exist
    log = open(logFile, "a")

    # write the prompt with a timestamp 
    log_string = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + prompt + ": " + response.choices[0].text + "\n"
    log.write(log_string)

# print the response
def printResponse(response):
    # print the response
    print(response.choices[0].text + "\n\n")

# define main
def main():
    # request GPT-3 to generate a response to a given prompt
    # and return the response
    response = generateResponse(prompt)

    # log the response
    logResponse(prompt, response)

    # print the response
    printResponse(response)

    return response

# call main
if __name__ == "__main__":
    # run indefinitely and wait for a new prompt
    past_prompt = ''
    total_usage = 0
    while True:
        try:
            # print message
            print("Enter a prompt: ")
            prompt = past_prompt + input()
            if prompt[-1] != '?':
                prompt = prompt + '?'
            response = main()
            past_prompt = past_prompt + '\n' + response.choices[0].text
            total_usage = total_usage + response.usage['total_tokens']
            if total_usage > max_tokens*0.9:
                print("Warning: GPT-3 usage is approaching the limit.")
                past_prompt = ''
        except Exception as e:
            print(f"Error: {e}")
            past_prompt = ''
            time.sleep(1)
