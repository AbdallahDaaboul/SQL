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


def retards_cumules ( database_cursor , gare_name ):

    TotTrainProg=0
    TotTrainAnn=0
    TotTrainRet=0
    query = 'select  mois,G1.intitule depart ,G2.intitule arrivee,trains_programmes,trains_annules,trains_retardes,1-(trains_annules+trains_retardes)*1.0/trains_programmes taux from Regularite R JOIN Gare G1 on R.depart=G1.code_UIC join Gare G2 on G2.code_UIC=R.arrivee where G2.intitule="{}"'.format(gare_name)
    print query
    database_cursor.execute(query)
    for (att_mois, att_intitule1, att_intitule2,trains_prog,trains_annules,trains_retardes, taux) in c.fetchall():
        print 'Mois:{} | {}--->{} | Trains_programmes : {} | Trains_annules : {} | trains_retardes : {}'.format(att_mois, att_intitule1.encode('utf-8'), att_intitule2.encode('utf-8'),trains_prog,trains_annules,trains_retardes)
        TotTrainProg=TotTrainProg + trains_prog
        TotTrainAnn=TotTrainAnn +  trains_annules
        TotTrainRet=TotTrainRet + trains_retardes
    print 'Total trains programmés :{}'.format(TotTrainProg)
    print 'Total trains annulés : {}'.format(TotTrainAnn)
    print 'Total trains retardés : {}'.format(TotTrainRet)
    taux_reg=1-(TotTrainAnn + TotTrainRet)*1.0 / TotTrainProg*1.0
    print 'Taux de régularité : {}'.format(taux_reg)
    return()

retards_cumules ( c , sys.argv[1] )
