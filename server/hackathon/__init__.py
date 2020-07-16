import os

customerService = {
    "key": "CUSTOMER_SERVICE",
    "project": "hackethon-283217",
    "filename": "CUSTOMER_SERVICE.json"
}

personalAssistant = {
    "key": "PERSONAL_ASSISTANT",
    "project": "online-shopping-spsvwi",
    "filename": "PERSONAL_ASSISTANT.json"
}


def write_to_file(chatbot):
    with open(chatbot["filename"], 'w') as outfile:
        outfile.write(os.environ[chatbot["key"]])


if not os.environ.get("LOCAL") == "true":
    write_to_file(customerService)
    write_to_file(personalAssistant)
