
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



-- Deepndecncias  ALGO - Dependem del ID 

Insert into rqEirq_dependance ( produit_id, fichier_id , smUUID ) 
Select 126,  idFichier, '3e30537235d947d0996adc7faffaa088'  
  from m.merveille2  where ALGO = 'x' 


Insert into rqEirq_dependance ( produit_id, fichier_id , smUUID ) 
Select 130,  idFichier, '3e30537235d947d0996adc7faffaa088'  
  from m.merveille2  where CoteISA = 'x'   


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

