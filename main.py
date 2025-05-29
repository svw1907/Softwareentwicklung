#Hier soll das Hauptprogramm auftauchen

from poi import get_sehenswürdigkeiten

latitude = 49.0069
longitude = 8.4037

pois = get_sehenswürdigkeiten(latitude, longitude, radius=1000)

print("Sehenswürdigkeiten im Radius 1 km, Ausgehend vom Bundesgerichtshof:")
for poi in pois:
    print("-", poi)

