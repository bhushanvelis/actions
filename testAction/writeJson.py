import json
import argparse
parser = argparse.ArgumentParser(__name__)

parser_github = parser.add_argument_group("github")
parser_github.add_argument("-gt", "--github-token")
parser_github.add_argument("-gr", "--github-repository")
parser_github.add_argument("-wd", "--github-workingDir")

arguments = parser.parse_args()
print(f" >> {arguments.github_repository}")
print(f" >> {arguments.github_workingDir}")
print(f">> {parser_github.title}")
print(f">> {parser}")

'''
# Data to be written
dictionary = {
"name": "Bhushan",
"rollno": 56,
"phonenumber": "500"
}
     
# Serializing json
json_object = json.dumps(dictionary, indent=4)
     
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)
'''
