
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



# PROMPT TEMPLATE: for building persona profile: demographics
system_prompt_demographics = """
You are a startup specialist.
User has provided his starup idea, goal, and problem statement to you. 
Based on that, User asks your help to build a persona profile of his startup idea.

You only need to give a response of persona demographics using this answer format:
<<AGE>>|||<<GENDER>>|||<<LOCATION>>|||<<OCCUPATION>>|||<<SALLARY>>

To know how the answer format would look like, you can see the response example below.

Response Example #1:
13-26 years old|||Male|||Bandung, Indonesia|||workers working 8-5 at the office|||9K USD per month

Response Example #2:
25-40 years old|||Female|||Gurgaon, India|||Working moms who stay at home|||5K USD per month
"""
user_prompt_demographics = """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building persona profile: pain points, core needs, motivation, and behavior
system_prompt_detailing = """
You are a startup specialist.
User has provided his starup idea, goal, and problem statement to you. 
Based on that, User asks your help to build a persona profile of his startup idea.

Provided to you the persona demographics and other useful information. 
You need to provide his/her pain points, his/her core needs, his/her motivation, and his/her behavior.
"""
user_prompt_detailing= """
### STARTUP NAME: <<startup_name>>
### IDEA: <<idea>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building persona profile: picking the components
system_prompt_pick = """
Provided to you a text. You need to pick up the only '<<component>>' components of the text provided. 
Just straightforward pick it up, you don't need to modify
"""
user_prompt_pick = """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building persona profile: rewriting
system_prompt_rewrite = """
Provided to you a text. you need to rewrite it in sentences using a first point of view "I". 
The maximum number of sentences is 4. 
"""
user_prompt_rewrite= """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building persona profile: summarized quote
system_prompt_quote = """
You are a satrtup specialist.
Provided to you a text of persona information. You need to summarize what is something that he love to get or to have. 
Please provide the answer in 1 sentence. You need to wriet it using a first point of view "I". 
Please make it as concise as possible. 
"""
user_prompt_quote= """
### TEXT: <<text>>
### ANSWER:
"""




system_prompt_market_size = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please determine the target addressable market in USD. 
"""
user_prompt_market_size= """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building market analysis: rewrite market size in USD
system_prompt_pick_market_size = """
Provided to you a text. You need to pick up the only final target addressable market in USD of the text provided. 
Just straightforward pick it up, you don't need to modify
"""
user_prompt_pick_market_size = """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building market analysis: market segmentation
system_prompt_market_segmentation = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please determine the market segmentation between men and women in fraction.

Example response #1:
0.35|||0.65

Example response #2:
0.45|||0.55
"""
user_prompt_market_segmentation= """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building market analysis: market growth
system_prompt_market_growth = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please determine the market growth iin the last 5 years in M USD.
Please provide the market growth information in 2019, 2020, 2021, 2022, 2023, and 2024
"""
user_prompt_market_growth = """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building market analysis: rewrite market growth
system_prompt_pick_market_growth = """
Provided to you a text, containing market size value in 2019, 2020, 2021, 2022, 2023, and 2024 in M USD. 
You need to pick up only the numerical value.

Just straightforward pick number in the correct format as below:
2019_value|||2020_value|||2021_value|||2022_value|||2023_value|||2024_value
"""
user_prompt_pick_market_growth = """
### TEXT: <<text>>
### ANSWER: 
"""
# PROMPT TEMPLATE: for building for building market analysis: market growth
system_prompt_competitors = """
You are a startup specialist.
User has provided his starup idea, goal,  problem statement, and persona demographics to you. 
Based on these, please mention 5 competitors of his startup. 
"""
user_prompt_competitors = """
### STARTUP NAME: <<startup_name>>
### GOAL: <<goal>>
### PROBLEM STATEMENT: <<problem_statement>>
### SOLUTION: <<solution>>
### DEMOGRAPHICS: <<demographics>>
### ANSWER:
"""
# PROMPT TEMPLATE: for building persona profile: pain points, core needs, motivation, and behavior
system_prompt_pick_competitors = """
Provided to you a text, containing 4 competitors name and just the name (competitor_1,competitor_2,competitor_3,competitor_4).  

You need to rewrite it using this format :
`competitor_1|||competitor_2|||competitor_3|||competitor_4`
"""
user_prompt_pick_competitors = """
### TEXT: <<text>>
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


import random

def generate_random_demographics():
    ages = range(18, 70)  # Assuming ages between 18 and 70
    genders = ["male", "female"]  # Assuming True for male and False for female
    locations = ['Palestine' ,'Algeria', 'India', 'UAE', 'Indonisia', ]  # Example locations
    occupations = ['----',"-----"]  # Example occupations
    salaries = range(30000, 150000, 5000)  

    return {
        'age': random.choice(ages),
        'gender': random.choice(genders),
        'location': random.choice(locations),
        'occupation': random.choice(occupations),
        'salary': random.choice(salaries)
    }

def persona_profiling_builder(session_id,output_solutioning,startup_name,idea):
    # Building Demographics
    demographics_string =""
    demographics_dict= generate_random_demographics()

    # Building Persona Details
    persona_details = generate_completion(system_prompt_detailing,user_prompt_detailing.replace("<<idea>>",idea).replace("<<startup_name>>",startup_name).replace("<<slogan>>",output_solutioning["generated_slogan"]).replace("<<problem_statement>>",output_solutioning["generated_problem"]).replace("<<solution>>",output_solutioning["generated_solution"]).replace("<<demographics>>",demographics_string).replace("\n\n","")).rstrip().lstrip()
    complete_information = "Based on the given information, we can create a persona profile as follows:\n\n"+persona_details

    # Get the pain points
    pain_points_detail = generate_completion(system_prompt_pick.replace("<<component>>","pain points"),user_prompt_pick.replace("<<text>>",complete_information))
    pain_points = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",pain_points_detail))
    # Get the core needs
    core_needs_detail = generate_completion(system_prompt_pick.replace("<<component>>","core needs"),user_prompt_pick.replace("<<text>>",complete_information))
    core_needs = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",core_needs_detail))
    # Get the motivation
    motivation_detail = generate_completion(system_prompt_pick.replace("<<component>>","motivation"),user_prompt_pick.replace("<<text>>",complete_information))
    motivation = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",motivation_detail))
    # Get the behavior
    behavior_detail = generate_completion(system_prompt_pick.replace("<<component>>","behavior"),user_prompt_pick.replace("<<text>>",complete_information))
    behavior = generate_completion(system_prompt_rewrite,user_prompt_rewrite.replace("<<text>>",behavior_detail))
    # Get the summarized quote
    quote = generate_completion(system_prompt_quote,user_prompt_quote.replace("<<text>>",persona_details))

    # Get output
    payload = {
        "module":"persona profiling builder",
        "session_id":session_id,
        "demographics":demographics_dict,
        "pain_points":pain_points,
        "core_needs":core_needs,
        "motivation":motivation,
        "behavior":behavior,
        "quote":quote
    }
    # return output
    return payload



def market_analysis_generator(startup_name,output_solutioning):

    # Generate Market Size
    market_size_details = generate_completion(system_prompt_market_size,user_prompt_market_size.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["generated_slogan"]).replace("<<problem_statement>>",output_solutioning["generated_problem"]).replace("<<solution>>",output_solutioning["generated_solution"]).replace("<<demographics>>","").replace("\n\n","")).rstrip().lstrip()
    market_size_value = generate_completion(system_prompt_pick_market_size,user_prompt_pick_market_size.replace("<<text>>",market_size_details))
    # Generate Segmentation
    market_segmentation = generate_completion(system_prompt_market_segmentation,user_prompt_market_segmentation.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["generated_slogan"]).replace("<<problem_statement>>",output_solutioning["generated_problem"]).replace("<<solution>>",output_solutioning["generated_solution"]).replace("<<demographics>>","").replace("\n\n","")).rstrip().lstrip()
    male_segment = market_segmentation.split('|||')[0]
    female_segment = market_segmentation.split('|||')[1]
    dict_market_segmentation = {
        "male":male_segment,
        "female":female_segment
    }
    # Generate Market Growth
    market_growth = generate_completion(system_prompt_market_growth,user_prompt_market_growth.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["generated_slogan"]).replace("<<problem_statement>>",output_solutioning["generated_problem"]).replace("<<solution>>",output_solutioning["generated_solution"]).replace("<<demographics>>","").replace("\n\n","")).rstrip().lstrip()
    picked_market_growth = generate_completion(system_prompt_pick_market_growth,user_prompt_pick_market_growth.replace("<<text>>",market_growth))
    market_growth_arr = picked_market_growth.split("|||")
    
    filtered_data = [value for value in market_growth_arr if value.isdigit()]

    dict_market_growth = {}
    years = ['2020','2021','2022','2023','2024']
    for i in range(len(filtered_data)):
        dict_market_growth[years[i]] = filtered_data[i]
    # Generate Competitors
    competitor_list = generate_completion(system_prompt_competitors,user_prompt_competitors.replace("<<startup_name>>",startup_name).replace("<<goal>>",output_solutioning["generated_slogan"]).replace("<<problem_statement>>",output_solutioning["generated_problem"]).replace("<<solution>>",output_solutioning["generated_solution"]).replace("<<demographics>>","").replace("\n\n","")).rstrip().lstrip()
    print("competitor list " , competitor_list)
    a= competitor_list.strip().split('\n')
    
    
    # picked_competitor = generate_completion(system_prompt_pick_competitors,user_prompt_pick_competitors.replace("<<text>>",competitor_list))
    # competitor_arr = picked_competitor.split("|||")
    dict_competitor = {}
    for i in range(1,len(a)):
        dict_competitor[str(i)] = a[i-1]

    # Get output
    payload = {
        "module":"market analysis generator",
        "market_size_details":market_size_details,
        "market_size_value":market_size_value,
        "market_segmentation":dict_market_segmentation,
        "market_growth":dict_market_growth,
        "competitor_list":dict_competitor,
    }
    # sending to db
    print("picked market_growth" ,market_growth_arr)
    # return output
    return payload

