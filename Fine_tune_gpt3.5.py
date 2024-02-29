import openai
# API_KEY=open("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","r").read()
openai.api_key="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"

chat_log=[]
while True:
    user_message=input()
    if user_message.lower()=="quit":
        break
    else:
        chat_log.append({"role":"user","content":user_message})
        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            message=chat_log

        )
        assistant_response=response['choices'[0]['message']['content']]
        print("WheelsMasail: ",assistant_response.strip("\n").strip() )
        chat_log.append({"role":"assistant","content":assistant_response.strip("\n").strip()})
