from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI()

messages = []

end_conversation = False
while (not end_conversation) :
  user_input = input('Input your inquiry (type \'n\' to end): ')

  if user_input == 'n':
    end_conversation = True
    break
  else :
    messages.append({
      'role': 'user',
      'content': user_input
    })
    completion = client.chat.completions.create(
      model='gpt-3.5-turbo',
      messages=messages
    )
  print('-----------------------------------------------------')
  for choice in completion.choices:
    message = choice.message.content
    messages.append({
      'role': choice.message.role,
      'content': choice.message.content
    })
    print(message)
    print('\n')
  print('-----------------------------------------------------')
  print('Current Token Usage: ')
  print(completion.usage.total_tokens)
  print('-----------------------------------------------------')

