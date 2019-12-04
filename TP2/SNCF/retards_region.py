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


def retards_region ( database_cursor , region_name ):
    query = 'select  mois,G1.intitule depart ,G2.intitule arrivee,trains_programmes,trains_annules,trains_retardes, G1.region regionDep,G2.region regionArr from Regularite R JOIN Gare G1 on R.depart=G1.code_UIC join Gare G2 on G2.code_UIC=R.arrivee where(regionDep="{}" or regionArr="{}") limit 5'.format(region_name,region_name)

    print query
    database_cursor.execute(query)
    for (att_mois, att_intitule1, att_intitule2,trains_prog,trains_annules,trains_retardes ,RD,RA) in c.fetchall():
        print 'Mois:{} | {}--->{} | Trains_programmes : {} | Trains_annules : {} | trains_retardes : {}'.format(att_mois, att_intitule1.encode('utf-8'), att_intitule2.encode('utf-8'),trains_prog,trains_annules,trains_retardes)

    return()

retards_region ( c , sys.argv[1] )
