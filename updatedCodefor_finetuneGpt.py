import openai

openai.api_key = "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"


test_messages = []

system_message = "Welcome to WheelsMasail! Your go-to chatbot for all things related to wheels. Ask me anything about cars, maintenance, troubleshooting, or any automotive topic. I'm here to assist you!"
test_messages.append({"role": "system", "content": system_message})
user_message = "I have a Nissan Moco 2015, import 2017. It was owned by us since it was imported so we are kind of the first owners. It came 7000 km driven and right now it is at 127k. First of all, I am not well aware about cars and I only started going for its maintenance since my father's amputation last year. 1st December, I changed its gear oil as sometimes it would do sudden jerks on AC and a mechanic (a friend's known) suggested CVT gear oil that I got from Karachi. I would usually take my friend's help but he has passed away. It's spark plugs were changed at the time but with Chinese ones. About a month ago, the car itself turned off on D in Eco IDLE but didn't turn back on and then its check engine light came on which was an error for its catalytic converter. The converter got cleaned and so did the fuel and I added a catalytic converter cleaner in my car. After a few days, it started jerking. These are slow jerks while accelerating and then at a constant speed of 60/80 it would do these jerks like it's trying to push itself but something is blocking it. I have gone to 4 mechanics since then, its spark plugs were replaced as two days back as it gave blinking check engine light while doing the same jerks but the problem was swear. Tapad work was done as well 2 weeks back as the car was turning off on D and R and vibrating. Its coils have been checked, fuel injector, fuel pump, catalytic converter. Last night its oxygen sensor was changed too. There are no DTCs but the jerking doesn't go away. Sometimes it's evident, other times its not so noticeable. The only two things left to try is to accelerate the car for 100 kms or so as one mechanic suggested it has air in its transmission and another friend suggested that it's time to replace its assembly. Can anyone of you guys help me as to what could be the cause? I am very distressed. The car has only been driven by me and my father."
test_messages.append({"role": "user", "content": user_message})

print(test_messages)

response = openai.ChatCompletion.create(
    model='ft:gpt-3.5-turbo-0613:personal:wheelsmasail:8pBRhdn7', 
    messages=test_messages,
    temperature=0,
    max_tokens=500
)
print(response["choices"][0]["message"]["content"])