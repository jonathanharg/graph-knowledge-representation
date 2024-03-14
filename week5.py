import networkx as nx
import requests
import pickle

base_module_url = "https://udb2.emps.ex.ac.uk/api/index.php/databases/teaching/modules/modulecode/"

modules = {}

def get_module(code:str):
    res = requests.get(base_module_url + code)
    return res.json()

def dfs_module(code: str):
    module = get_module(code)
    if code in modules:
        return
    
    modules[code] = module
    
    for requirment in module["requisites"]:
        req_code = requirment["_moduleCode"]
        print(f"{code} {module["title"]} requires {req_code}")
        dfs_module(req_code)

# dfs_module("MTH3022")

courses = {}

base_course_url = "https://udb2.emps.ex.ac.uk/api/index.php/databases/teaching/programmes/info/"
# maths: 3891

def get_course(code:int):
    res = requests.get(base_course_url + str(code))
    if res.status_code == 404:
        return None
    return res.json()

# for i in range(5000):
#     course = get_course(i)
#     if course is not None:
#         courses[i] = course

with open('courses.pickle', 'rb') as handle:
    courses = pickle.load(handle)

course_key_types = {}

print("Done")