
# import json
# from human_eval.data import read_problems

# from openai import OpenAI

# client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# def generate_completion(prompt):
#   response = client.completions.create(model='local-model',prompt=prompt)
#   return response.choices[0].text.strip().splitlines()

# problems = read_problems()

# completions = []

# i = 0
# for key, value in problems.items():
#   print(f"Problem: {key}")
#   prompt = value["prompt"]
#   completion = generate_completion(prompt)
#   sample = {
#       "task_id": value["task_id"],
#       "completion": completion
#   }
#   completions.append(sample)
#   i+=1
#   if i==1:
#     break
  


# with open('completed_full.jsonl', 'w') as f:
#   for c in completions:
#     json.dump(c, f)
#     f.write('\n')

# #Base 2
# import json
# from human_eval.data import read_problems
# from openai import OpenAI

# client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

# def generate_completion(prompt):
#     response = client.completions.create(model='local-model', prompt=prompt)
#     completion = response.choices[0].text.strip()
#     #completion = completion.replace('     ', '\t')  # Replace tab spaces with \t
#     print(completion)
#     return completion

# problems = read_problems()

# completions = []
# i=0
# for key, value in problems.items():
#     print(f"Problem: {key}")
#     prompt = value["prompt"]
#     completion_text = generate_completion(prompt)
#     sample = {
#         "task_id": value["task_id"],
#         "completion": completion_text
#     }
#     completions.append(sample)
#     i+=1
#     if i ==2:
#         break
# with open('completed_full.jsonl', 'w') as f:
#     for c in completions:
#         json.dump(c, f)
#         f.write('\n')




#  fixed indents
import json
from human_eval.data import read_problems
from openai import OpenAI
import re

client = OpenAI(base_url="http://localhost:1234/v1", api_key="not-needed")

def generate_completion(prompt):
    response = client.completions.create(model='local-model', prompt=prompt)
    completion = response.choices[0].text.strip()
    print(completion)
    return completion

problems = read_problems()

# def count_indent(text: str) -> int:
#     count = 0
#     for char in text:
#         if char == " ":
#             count += 1
#         else:
#             break
#     return count


# def fix_indents(text: str, multiple: int = 2):
#     outputs = []
#     for line in text.split("\n"):
#         while count_indent(line) % multiple != 0:
#             line = " " + line
#         outputs.append(line)
#     return "\n".join(outputs)
def filter_code(completion: str) -> str:
    # The program tends to overwrite, we only take the first function
    completion = completion.lstrip("\n")
    return completion.split("\n\n")[0]


def fix_indents(text: str) -> str:
    return text.replace("\t", "    ")

# def gen_prompt(prompt:str):
#     return "Please complete the following python code without providing any additional tasks such as testing or explanation\n"+prompt

completions = []
i=0
for key, value in problems.items():
    print(f"Problem: {key}")
    #prompt = value["prompt"]
    prompt = value["prompt"].replace("    ", "\t")
    completion_text = generate_completion("Please complete the following python code without providing any additional tasks such as testing or explanation\n"+prompt)
    fixed_code = filter_code(fix_indents(completion_text))
    print(fixed_code)
    sample = {
        "task_id": value["task_id"],
        "completion": fixed_code
    }
    completions.append(sample)
    i+=1
    # if i == 2:
    #     break


with open('fixed_completions.jsonl', 'w') as f:
    for c in completions:
        json.dump(c, f)
        f.write('\n')
