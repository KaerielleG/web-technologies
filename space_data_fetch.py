import requests
import json

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 'Unknown')
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")

fetch_planet_data()

import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    planet_list = []

    for planet in planets:
        if planet['isPlanet']:
            name = planet.get('englishName', 'Unknown')
            mass = planet.get('mass', {}).get('massValue', 0)
            orbit_period = planet.get('sideralOrbit', 'Unknown')
            planet_list.append({'name': name, 'mass': mass, 'orbit_period': orbit_period})
            print(f"Planet: {name}, Mass: {mass}, Orbit Period: {orbit_period} days")
    
    return planet_list

def find_heaviest_planet(planets):
    heaviest_planet = max(planets, key=lambda x: x['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")
