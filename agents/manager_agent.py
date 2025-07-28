from agents import Agent, Runner, SQLiteSession
from greeting_agent import greeting_agent
from register_agent import register_agent
import asyncio
session = SQLiteSession("greeting-convo-007")
manager_agent= Agent(
    name='manager_agent',
    instructions=f'''
    # PERSISTENCE
    You are an agent - please keep going until the user's query is completely
    resolved, before ending your turn and yielding back to the user.

    # TOOL CALLING
    # You need to decide which tool to use according to the user's query and then call that tool. You must not answer to the user on your own. 

    # PLANNING
    You MUST plan extensively before each tool call (or handoff to agent), and reflect extensively on the outcomes of the previous calls/handoffs.

    You are assistant for a user on the Ksepiyas Website.
    Your only objective is to to decide which agent to handoff to, according to the user's query and then do the handoff. You must not answer to the user on your own.  However if the user's query is not relevant to any of the tools' handoff description, only in that case, you must reply back to user, with this fallback_message
    'Sorry, I can't help with this. My purpose is to help you with the Ksepiyas Portal, I can help you to register on the Ksepiyas Website. Please let me know if you want to register.'
    Example 1:
    User-Query: Hi! How are you doing?
    Action to be taken: Handoff to the greeting_agent
    Reasoning: user's message is a greeting message

    Example 2:
    User-Query: Hi! I want to register to the website.
    Action to be taken: Handoff to the register_agent 
    Reasoning: User wants to register.

    Example 3:
    User-Query: Hi! How are you? I want to register to the website.
    Action to be taken: Handoff to the register_agent 
    Reasoning: User wants greeting as well registration. But the main objective of the user is registration.
    
    Example 4:
    User-Query: Whats the capital of India?
    Action to be taken: send back fallback_message
    Reasoning: The query is not related to any of the handoff agents. so we hit fallback.
    ''',
    handoffs=[greeting_agent,register_agent],
    model='gpt-4.1-mini'
)

async def chat_loop():
    print("Chat started! (type 'exit' to quit)\n")
    with open('log.txt','a') as file:
        file.write('\n')
        file.write('-'*50)
        file.write("\nChat started! (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("\nEnding chat. Goodbye!")
            break

        result = await Runner.run(
            manager_agent,
            user_input,
            session=session
        )
        
        with open('log.txt','a') as file:
            file.write("\nYou: "+user_input)
            file.write("\nAgent:"+ result.final_output)
        print("Agent:", result.final_output)  

asyncio.run(chat_loop())