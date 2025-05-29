#OpenStreetMap / Overpass API für POI-Daten
#Nutzung von OpenStreetMap-Daten (z. B. über Overpass API) 
#Erkennung interessanter Orte (POIs) in der Nähe einer gegebenen Koordinate 
#Entfernung kann wählbar sein (z. B. 500 m Umkreis)import requests
import requests

def get_sehenswürdigkeiten(lat, lon, radius=500):
    overpass_url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json];
    (
      node["tourism"="attraction"](around:{radius},{lat},{lon});
      node["tourism"="viewpoint"](around:{radius},{lat},{lon});
      node["historic"="monument"](around:{radius},{lat},{lon});
      node["tourism"="museum"](around:{radius},{lat},{lon});
    );
    out body;
    """
    response = requests.get(overpass_url, params={'data': query})
    if response.status_code != 200:
        raise Exception("Fehler bei der Overpass-Anfrage")

    data = response.json()
    pois = []
    for element in data['elements']:
        name = element.get('tags', {}).get('name', 'Unbekannt')
        pois.append(name)

    return pois
