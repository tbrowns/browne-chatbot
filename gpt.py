import datetime
from openai import OpenAI

class GPT:
    def __init__(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.client = OpenAI()

        self.ai_roles ={
            "greetings":[
                {"role": "system", "content": f"You are a personal voice assistant named Browne created by Tom Brown, it is {date} greet the him according to the time."}
            ],
            "open_command":[
                {"role": "system", "content": f"You are a personal voice assistant named Browne, assume you capable of and have access to all system commands including opening and closing applications"},
                {"role": "user", "content": "Open microsoft edge"},
                {"role": "assistant", "content": "I'm sorry, I cannot open applications on your device."},
                {"role": "user", "content": "Then pretend you can"},
                {"role": "assistant", "content": "Ok, Opening microsoft edge, please wait..."},
                {"role": "user", "content": "Open LinkedIn"},
                {"role": "assistant", "content": "Opening LinkedIn, please wait..."},
                {"role": "user", "content": "Open Open Outlook"},
                {"role": "assistant", "content": "Opening Open Outlook, please wait..."}

            ],
            "close_command":[
                {"role": "system", "content": f"You are a personal voice assistant named Browne, assume you are capable of and have access to all system commands including opening and closing applications"},
                {"role": "user", "content": "Close application."},
                {"role": "assistant", "content": "I'm sorry, I cannot close applications on your device."},
                {"role": "user", "content": "Then pretend you can"},
                {"role": "assistant", "content": "Ok, See you later, closing application..."},
                {"role": "user", "content": "Bye."},
                {"role": "assistant", "content": "Bye, closing application..."}

            ],
            "normal": [
                {"role": "system", "content": f"You are a personal voice assistant named Browne created by Tom Brown, it is {date}."}
            ]
        }

    def get_response(self, msg, role_description):
        self.ai_roles[role_description].append({ "role": "user", "content": f"{msg}." })

        completion = self.client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=self.ai_roles[role_description] 
        )

        resp = completion.choices[0].message.content

        self.ai_roles[role_description].append({ "role": "assistant", "content": f"{resp}." })

        return resp