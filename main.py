from services.service_salle import ServiceSalle
from models.salle import Salle

service = ServiceSalle()

s1 = Salle("S2", "Salle informatique", "laboratoire", 30)
if service.ajouter_salle(s1):
    print("ajout réussi")
else:
    print("erreur ajout")
s1.capacite = 40
if service.modifier_salle(s1):
    print("modification réussie")
else:
    print("erreur modification")
salle = service.rechercher_salle("S1")
if salle:
    salle.afficher_infos()
salles = service.recuperer_salles()
for s in salles:
    s.afficher_infos()
service.supprimer_salle("S1")
print("salle supprimée")