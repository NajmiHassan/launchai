
from ai71 import AI71 



AI71_API_KEY = "api71-api-a4e21705-d85c-47d8-8c9f-bbf7403654cf"

def generate_completion(system_prompt, user_prompt):
    output = ""
    for chunk in AI71(AI71_API_KEY).chat.completions.create(
        model="tiiuae/falcon-180b-chat",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "assistant", "content": user_prompt},
        ],
        stream=True,
    ):
        if chunk.choices[0].delta.content:
            output += (chunk.choices[0].delta.content)
    return output.rstrip().lstrip()

system_def ="""
You are a startup specialist and you must give a consice response and if your have not the answer return no response .
"""


# PROMPT TEMPLATE: for generating goal and improved idea of the startup
system_prompt_1st = f"""{system_def}
User asks your help on elevating their startup idea. 
Please provide Idea and Goal that you would like to recommend of their startup idea. 
Please answer in 3-5 sentences. 
"""
user_prompt_1st = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### ANSWER:
"""
# PROMPT TEMPLATE: for generating a startup tagline
system_prompt_2nd = f"""{system_def}
You are a startup specialist.
User asks your help to create startup slogan. 
"""
user_prompt_2nd = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### ANSWER:
"""
# PROMPT TEMPLATE: for generating problem statement
system_prompt_3rd = f"""{system_def}
User asks your help to generate problem statement or background problem of his startup idea.
Your answer should consist 3-5 sentences.
"""
user_prompt_3rd = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### ANSWER:
"""
# PROMPT TEMPLATE: for generating solution summary
system_prompt_4th = f"""{system_def}
User has provided his starup idea, goal, and problem statement to you. 
Based on that, User asks your help to summarize a solution that may be a technology solution of his startup idea.
Your answer should consist 3-5 sentences.
"""
user_prompt_4th = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### ANSWER:
"""


def solutioning_generator(session_id, startup_name, idea_query):
    # Generate goal, tagline, problem statement, and solution
    goal = generate_completion(system_prompt_1st,user_prompt_1st.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name)).rstrip().lstrip()
    generated_slogan = generate_completion(system_prompt_2nd,user_prompt_2nd.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name).replace("<<goal>>",goal)).rstrip().lstrip().replace("\"","")
    generated_problem = generate_completion(system_prompt_3rd,user_prompt_3rd.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name).replace("<<goal>>",goal)).rstrip().lstrip()
    generated_solution = generate_completion(system_prompt_4th,user_prompt_4th.replace("<<idea>>",idea_query).replace("<<startup_name>>",startup_name).replace("<<goal>>",goal)).replace("<<problem_statement>>",generated_problem).rstrip().lstrip()
    # generate payload 
    payload = {
        "session_id":session_id,
        "generated_slogan":generated_slogan,
        "generated_problem":generated_problem,
        "generated_solution":generated_solution
    }
    
    return payload

