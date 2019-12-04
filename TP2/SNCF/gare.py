#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sqlite3

## Chemin vers la base
SQLITE_DATABASE = '/nfs/home/sasl/eleves/main/3802928/TP/BDD/TP2/SNCF/sncf.db'

## Connexion à la base
conn = sqlite3.connect(SQLITE_DATABASE)
c = conn.cursor()

#############
## Exemple 1
## Requête avec un résultat attendu de plusieurs lignes
query = 'select Code_UIC,intitule from gare where (departement ="Aude")'

## Exécution de la requête
c.execute(query)

## Parcours des résultats
for (att_code, commune_nom) in c.fetchall():
    print '{} : {}'.format(att_code, commune_nom.encode('utf-8'))
