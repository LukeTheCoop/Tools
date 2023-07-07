# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

openai.organization = "org-XzStKmWQcLGpiopghiRMh7a0"
openai.api_key = "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"
transcript = ''


print("\n\nPLEASE MAKE SURE ALL REQUIRED AUDIO FILES ARE PLACED INTO THE 'Audio' FOLDER\n\n|| If using multiple files each file should share the same name with the number of the file after. EX: 'CoolAudio1', 'CoolAudio2', 'CoolAudio3'... ||")
user_input = input('S for a single file, M for multiple files:\n').lower()
if user_input == 's':
	file_name, type_of = input('File name:\n'), input("Type of File (m4a, mp3, wav, etc)")
	print(f'Catching file {file_name}')
	audio_file = open((f"audio/{file_name}.{type_of}"), "rb")
	print('Caught!')
	print(openai.Audio.transcribe("whisper-1", audio_file)["text"])
elif user_input == 'm':
	num_of_files, name, type_of= input("Number of files:\n"), input("Shared Name of Files:\n"), input("Type of File (m4a, mp3, wav, etc)")
	for i in range(num_of_files):
		file_name = f"{name}{i+1}.{type_of}"
		print(f'Catching file {file_name}')
		audio_file= open(file_name, "rb")
		print('Caught!')
		transcript += openai.Audio.transcribe("whisper-1", audio_file)["text"]
		print(f'File {i+1} finished!')

print(transcript)

