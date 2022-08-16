import requests
import json
from selenium import webdriver


def name_giver(func):
    def executor():
        print("STARTING function {}".format(func.__name__))
        func()
        print("FINISHED function {}".format(func.__name__))
        print("-"*25)
    return executor()

# API testing
@name_giver
def git_repo_check():
    response = requests.get('https://api.github.com/users/avielb/repos')
    response_file = response.json()
    print(len(response_file) >= 5)


@name_giver
def agify_check():
    for i in range(3):
        name = input("Please enter a random name:\n")
        response = requests.get('https://api.agify.io/?name={}'.format(name))
        print(name+": "+str(response.json()["age"]))
        if response.json()["age"] > 120 or response.json()["age"] < 0:
            print("False")
    print("True")


@name_giver
def university_check():
    response = requests.get('http://universities.hipolabs.com/search?country=Israel')
    print(len(response.json()) > 5)


# UI testing
@name_giver
def y_container_t_check():
    driver = webdriver.Chrome()
    driver.get("https://www.ycombinator.com/")
    expected = "Y Combinator"
    print(expected == driver.title)


@name_giver
def docker_hub_t_check():
    driver = webdriver.Chrome()
    driver.get("https://hub.docker.com/")
    expected = "Docker Hub Container Image Library | App Containerization"
    print(expected == driver.title)