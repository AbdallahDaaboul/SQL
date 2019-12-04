#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import sqlite3

## Chemin vers la base
## Connexion à la base
SQLITE_DATABASE = '/nfs/home/sasl/eleves/main/3802928/TP/BDD/TP2/SNCF/sncf.db'
conn = sqlite3.connect(SQLITE_DATABASE)
c = conn.cursor()
#############


def get_gare_info ( database_cursor , gare_name ):
    query = 'select latitude,longitude from gare where (intitule ="' + gare_name + '")'
    print(query)
    database_cursor.execute(query)
    latitude,longitude = database_cursor.fetchone()
    return (( latitude , longitude) )

def pire_taux(database_cursor):
    query ='select mois,G1.intitule,G2.intitule,1-(trains_annules+trains_retardes)*1.0/trains_programmes taux from Regularite JOIN Gare G1 ON Regularite.depart = G1.Code_UIC JOIN Gare G2 ON Regularite.arrivee = G2.Code_UIC where (trains_programmes>0) order by taux limit 10;'
    database_cursor.execute(query)
    for (att_mois, att_intitule1, att_intitule2, taux_regularite) in c.fetchall():
        print 'Mois:{} | {}--->{} | Taux Régularité : {}'.format(att_mois, att_intitule1.encode('utf-8'), att_intitule2.encode('utf-8'), taux_regularite)
    return()

(la,lo)= get_gare_info(c,sys.argv[1])
print(la,lo)

pire_taux(c)
