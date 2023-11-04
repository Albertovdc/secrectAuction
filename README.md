# Dictionaries
| Key      | Value                                                                     |
|----------|---------------------------------------------------------------------------|
| Bug      | An error in a program that prevents the program from running as expected. |
| Function | A piece of code that you can easily call over and over again.             |
| Loop     | The action of doing something over and over again.                        |
## syntax
````python
{key : value,
 key_2 : value
 key_3 : value
 key_n : value}
````
## example
````python
programming_dictionary = {"Bug":"An error in a program  that prevents the program from running as expected.",
                          "Function":"A piece of code that you can easily call over and over again."}
# Retriving items from dictionary.
print(programming_dictionary["Bug"])

# Adding new items to dictionary.
# 
programming_dictionary["Loop"] = "The action of doing something over and over again."

# empty dictionary
example = {}

# Wipe an existing dictionary
programming_dictionary = {}

# Loop through a dictionary.
for item in programming_dictionary:
    # Just give the keys
    print(item)
    # Give the value
    print(programming_dictionary[item])
````

# Nesting list and dictionaries
````python
# Nesting list in a dictionary
travel_log={
    "France":["Paris", "Lille", "Dijon"],
    "Germany":["Berlin", "Hamburg", "Stuttgart"]
}

````
````python
# Nesting dictionary in a dictionary

cities_visited = {
    1: "Paris",
    2: "Lille",
    3: "Dijon"
}
travel_log = {
    "France" : cities_visited 
}

travel_log = {
    "France" : {"cities_visited" : ["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany" : {"cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], "total_visits" : 20}
}
````
````python
#Nesting dictionary in a list
travel_log = [
    # Dictionary 1
    {
        "country" : "France",
        "cities_visited" : ["Paris", "Lille", "Dijon"], 
        "total_visits" : 12
    },
    # Dictionary 2
    {
        "country" : "Germany", 
        "cities_visited" : ["Berlin", "Hamburg", "Stuttgart"], 
        "total_visits" : 20
     }
]
````

## Example
````python
country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(a, b, c):
  travel_log.append({"country":a, "visits":b, "cities":c})
    
# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")

````
