
Delete from "rqEirq_dependance";
Delete from "rqEirq_fichier";
Delete from "rqEirq_responsable";
Delete from "rqEirq_source";


Delete from "protoGraph_canvas";
Delete from "protoGraph_canvasdetail";
Delete from "protoGraph_edge";
Delete from "protoGraph_edgecategory";
Delete from "protoGraph_node";
Delete from "protoGraph_nodecategory";


-- ATTACH '/home/certae/sm3/docker-carra/src/db/merveille.sqlite' AS `m`


Insert into rqEirq_responsable ( code , smUUID ) 
    Select distinct Responsable , '3e30537235d947d0996adc7faffaa088' from m.merveille2; 


Insert into rqEirq_source( code , typeSource, smUUID ) 
    Select distinct NomSource ,  TypeSource, '3e30537235d947d0996adc7faffaa088' from m.merveille2;


Update m.merveille2  
    set idSource = ( Select s.id from rqEirq_source s where  m.merveille2.NomSource = s.code );

Update m.merveille2  
    set idResponsable = ( Select s.id from rqEirq_responsable s where  m.merveille2.Responsable = s.code );


Insert into rqEirq_fichier( code , source_id, smUUID ) 
    Select distinct NomFichier ,  idSource, '3e30537235d947d0996adc7faffaa088' from m.merveille2; 


Update m.merveille2  
    set idFichier = ( Select s.id from rqEirq_fichier s where  m.merveille2.NomFichier = s.code ); 


update rqEirq_source set 
  responsable_id =  ( Select m.idResponsable from m.merveille2  as m where rqEirq_source.code =  m.NomSource ); 



--  UPD Source 

update rqEirq_fichier set 
  emplacement =  ( Select m.EmplacementDonnees from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 


update rqEirq_fichier set 
  chaineChargement =  ( Select m.ChaineChargement from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  chaineExtraction =  ( Select m.ChaineExtraction from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  chaineNettoyage =  ( Select m.ChaineNettoyage from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  codeUntTraitement =  ( Select m.CodeUntTraitement from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  dgu =  ( Select m.DGU from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  frequence =  ( Select m.Frequence from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  reception =  ( Select m.Reception from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  scenario =  ( Select m.Scenario from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 


update rqEirq_fichier set 
  typeExploitation =  ( Select m.TypeExploitation from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 

update rqEirq_fichier set 
  vpa =  ( Select m.VPA from m.merveille2  as m where rqEirq_fichier.code =  m.NomFichier ); 



-- DEPENDANCES 



-- Deepndecncias  ALGO - Dependem del ID 

Insert into rqEirq_dependance ( produit_id, fichier_id , smUUID ) 
Select 126,  idFichier, '3e30537235d947d0996adc7faffaa088'  
  from m.merveille2  where ALGO = 'x' 


Insert into rqEirq_dependance ( produit_id, fichier_id , smUUID ) 
Select 130,  idFichier, '3e30537235d947d0996adc7faffaa088'  
  from m.merveille2  where CoteISA = 'x'   





  `ALGO`  TEXT,
  `Avantagelogement`  TEXT,
  `AvantagelogementHQ`  TEXT,
  `BNR` TEXT,
  `CoteISA` TEXT,
  `CreancesFiscales`  TEXT,
  `DerivationD2BBB` TEXT,
  `DerivationD2BBC` TEXT,
  `DivulgationVolontaire` TEXT,
  `EnquetesSpeciales` TEXT,
  `ExtractionMAD` TEXT,
  `GainCapital` TEXT,
  `IGIF`  TEXT,
  `IGSEVIR` TEXT,
  `IndustrieVetement` TEXT,
  `IR_NP` TEXT,
  `IR_SD` TEXT,
  `IR_Societe`  TEXT,
  `IR_selectionNP`  TEXT,
  `IR_selectionSD`  TEXT,
  `IR_MouvementTresorerie`  TEXT,
  `IR_CasRisqueActifs`  TEXT,
  `IR_CasRisque_non_production` TEXT,
  `IR_CasRisque_sous_declaration` TEXT,
  `Location_ImmeublesParticulier` TEXT,
  `Location_ImmeublesSocietes`  TEXT,
  `Nelson_Declaration_debitrice`  TEXT,
  `PDD` TEXT,
  `Projet_MIRE` TEXT,
  `Qui_vit_la`  TEXT,
  `RAS_TAX` TEXT,
  `RDPRM` TEXT,
  `DGP_Pension_alimentaire` TEXT,
  `Recouvrement_alimentaire`  TEXT,
  `ReferentielAdresses_D2`  TEXT,
  `Referentiel_D2_ADR_REF`  TEXT,
  `Referentiel_D2_REF_ADR_COMPL`  TEXT,
  `Referentiel_D2_REF_ADR_DGEQ` TEXT,
  `Referentiel_lien_de_parente` TEXT,
  `Referentiel_lien_personne_entreprise`  TEXT,
  `Releves` TEXT,
  `Renseignements_verificateurs`  TEXT,
  `Resto` TEXT,
  `DGP_Pensions_alimentaires` TEXT,
  `Resto_Indices` TEXT,
  `RQAP`  TEXT,
  `SMCM`  TEXT,
  `Statut_de_residence` TEXT,
  `Tableau_de_bord_Centrale_de_donnees` TEXT,
  `Tableau_de_bord_DGP` TEXT,
  `Tableau_de_bord_DGTT`  TEXT,
  `Tableau_de_bord_Service_client`  TEXT,
  `Taxes_percues_non_remises` TEXT,
  `Transactions_immob_personnes_liees`  TEXT,
  `RPSIPA`  TEXT,
  `Cube_D3_Renseignement` TEXT,
  `Cube_D3_Renseignements_en_erreur`  TEXT,
  `IGALFI`  TEXT,
  `IGSEVIR2`  TEXT,
  `Cubes_SICAR` TEXT,
  `F7_DIVO` TEXT,
  `id`  INTEGER NOT NULL,
  `Responsable` TEXT,
  `idResponsable` INTEGER,
  `idSource`  INTEGER,
  `idFichier` INTEGER
)