def send_messages(messages):
    while messages:
        current_message = messages.pop()
        sent_messages.append(current_message)

sent_messages = []

messages = ['hey', 'yo', 'hi', 'ola', 'salut']
send_messages(messages)
print(messages)
print('-----------')
print(sent_messages)