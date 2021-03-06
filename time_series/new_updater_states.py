import json
import itertools




# change both values





today = '4/14/2020'
yesterday = '4/13/2020'

states_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York",
  "North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]


all_states = {}

for state in states_list:
    str_state = state
    state ={}
    state['Province/State'] = str(str_state)

    state[today] = 0
    all_states[str(str_state)] = state





# change file to todays data





with open("daily_data/4-14-20.json", 'r') as myfile:
    data = myfile.read()

daily_object = json.loads(data)

for county in daily_object:
    state_name = county["Province_State"]
    if state_name in states_list:
        access_state = all_states[state_name]

        access_state[today] = access_state[today] + county["Confirmed"]
        #print(access_state["Confirmed"])
        #print(county["Confirmed"])





# change file to yesterdays data




with open("./daily_data/4-13-20.json", 'r') as myfile:
    data1 = myfile.read()

yesterday_object = json.loads(data1)

for county in yesterday_object:
    state_name = county["Province_State"]
    if state_name in states_list:
        access_state = all_states[state_name]

        access_state[today] = access_state[today] - county["Confirmed"]

print(all_states)

#all_states is an object containing current days new cases at this point in script

with open("./new_json.json", 'r') as myfile:
    data2 = myfile.read()

update_object = json.loads(data2)

#print(update_object["Alaska"])

for name_of_state in states_list:

    new_state_object = update_object[name_of_state]

    new_state_object[today] = all_states[name_of_state][today]

#update_object["Alabama"][today] =

print(update_object["Alaska"])





