import os
import openai
import pyperclip

# GPT
openai.organization = "ORGANIZATION"
openai.api_key = 'API_KEY'

# Initial conversation setup
jarvis_system = 'You will be returning a well thought out and well detailed response which will be given to an AI to give that AI understandment of the project. You are the middle man between the Coder and AI describing in detail how the project is laid out and its purpose so that the user may feed your response to a AI. Make sure to give a clear layout of the project, its purpose and packages. I will be giving the directory on my own so you may refer to files solely by their name. You do not need to break down the file directory, this will already be given. Only say the purpose of the project and refer to files soley by their name. Here is your project: '


def get_directory_contents(path, indent=0, accumulator=""):
    """
    Accumulates the contents of files in a directory and its subdirectories in a string.
    
    :param path: the path to the directory
    :param indent: the indentation level (used for recursion, do not set manually)
    :param accumulator: the accumulated string (used for recursion, do not set manually)
    :return: a string with all the contents of the files
    """
    # If path is a directory, process its contents
    if os.path.isdir(path):
        accumulator += f"{'  ' * indent}Directory: {os.path.basename(path)}\n"
        indent += 1  # Increase the indentation level
        for item in os.listdir(path):
            # Recursively accumulate contents of subdirectories
            accumulator = get_directory_contents(os.path.join(path, item), indent, accumulator)
    else:
        # If path is a file, accumulate its name, directory and contents
        accumulator += f"{'  ' * indent}File: {os.path.basename(path)}\n"
        accumulator += f"{'  ' * indent}Directory: {os.path.dirname(path)}\n"
        with open(path, 'r') as file:
            try:
                # Reading contents of the file
                contents = file.read()
                # Accumulating contents of the file
                accumulator += f"{'  ' * indent}Contents:\n{contents}\n"
            except:
                # If file cannot be read (e.g. binary file), accumulate a message
                accumulator += f"{'  ' * indent}Contents: [Unable to read file]\n"
    
    return accumulator

# Example usage:
# The function will accumulate the contents of the current directory into a string
all_contents = get_directory_contents('.')

# Now, you can print the accumulated string or do whatever you want with it
jarvis_system += all_contents
conversation = [
    {"role": "system", "content": jarvis_system},
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation
)

response = response['choices'][0]['message']['content']

pyperclip.copy(f'DIRECTOY: {all_contents} PROJECT: {response}')

print('Copied to clipboard')





