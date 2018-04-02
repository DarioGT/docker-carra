
CREATE TABLE "rqEirq_responsable" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "code" varchar(200) NULL,
    "coordonnees" varchar(200) NULL,
    "notes" varchar(200) NULL,
    "label" varchar(200) NULL);

CREATE TABLE "rqEirq_technologie" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "code" varchar(200) NULL,
    "label" varchar(200) NULL,
    "description" varchar(500) NULL,
    "typeT" varchar(20) NULL, );

CREATE TABLE "rqEirq_source" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "code" varchar(200) NULL,
    "typeSource" varchar(20) NULL,
    "label" varchar(200) NULL,
    "description" varchar(500) NULL,
    "notes" varchar(500) NULL,
    "pilote_id" integer NULL REFERENCES "rqEirq_responsable" ("id"),
    "urlDoc" varchar(500) NULL,
    "responsable_id" integer NULL REFERENCES "rqEirq_responsable" ("id"));

CREATE TABLE "rqEirq_fichier" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "code" varchar(200) NULL,
    "responsable_id" integer NULL REFERENCES "rqEirq_responsable" ("id"),
    "source_id" integer NULL REFERENCES "rqEirq_source" ("id"),
    "label" varchar(200) NULL,
    "chaineChargement" varchar(50) NULL,
    "chaineExtraction" varchar(50) NULL,
    "chaineNettoyage" varchar(50) NULL,
    "codeUntTraitement" varchar(50) NULL,
    "description" varchar(500) NULL,
    "dgu" varchar(50) NULL,
    "emplacement" varchar(50) NULL,
    "frequence" varchar(50) NULL,
    "notes" varchar(500) NULL,
    "reception" varchar(50) NULL,
    "scenario" varchar(50) NULL,
    "typeExploitation" varchar(50) NULL,
    "typeF" varchar(50) NULL,
    "urlDoc" varchar(500) NULL,
    "urlMeta" varchar(500) NULL,
    "urlModel" varchar(500) NULL,
    "vpa" integer NULL);

CREATE TABLE "rqEirq_dependance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,  ,
    "fichier_id" integer NULL REFERENCES "rqEirq_fichier" ("id"),
    "produit_id" integer NULL REFERENCES "rqEirq_source" ("id"));

CREATE TABLE "rqEirq_ressourcetech" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "ressource_id" integer NULL REFERENCES "rqEirq_responsable" ("id"),
    "technologie_id" integer NULL REFERENCES "rqEirq_technologie" ("id"));

CREATE TABLE "rqEirq_techchargement" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "fichier_id" integer NULL REFERENCES "rqEirq_fichier" ("id"),
    "technologie_id" integer NULL REFERENCES "rqEirq_technologie" ("id"));

CREATE INDEX "rqEirq_dependance_8eb6132c" ON "rqEirq_dependance" ("produit_id");
CREATE INDEX "rqEirq_dependance_d31e77c8" ON "rqEirq_dependance" ("fichier_id");
CREATE INDEX "rqEirq_fichier_0afd9202" ON "rqEirq_fichier" ("source_id");
CREATE INDEX "rqEirq_fichier_1ba06e10" ON "rqEirq_fichier" ("responsable_id");
CREATE INDEX "rqEirq_ressourcetech_01c920d8" ON "rqEirq_ressourcetech" ("technologie_id");
CREATE INDEX "rqEirq_ressourcetech_a9a2ddb4" ON "rqEirq_ressourcetech" ("ressource_id");
CREATE INDEX "rqEirq_source_03c49425" ON "rqEirq_source" ("pilote_id");
CREATE INDEX "rqEirq_source_1ba06e10" ON "rqEirq_source" ("responsable_id");
CREATE INDEX "rqEirq_techchargement_01c920d8" ON "rqEirq_techchargement" ("technologie_id");
CREATE INDEX "rqEirq_techchargement_d31e77c8" ON "rqEirq_techchargement" ("fichier_id");
