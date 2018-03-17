DROP TABLE "protoGraph_edgecategory";
DROP TABLE "protoGraph_nodecategory";
DROP TABLE "protoGraph_node";
DROP TABLE "protoGraph_edge";
DROP TABLE "protoGraph_canvas";
DROP TABLE "protoGraph_canvasdetail";

DROP TABLE "rqEirq_dependance";
DROP TABLE "rqEirq_fichier";
DROP TABLE "rqEirq_responsable";
DROP TABLE "rqEirq_source";
DROP TABLE "taggit_tag";
DROP TABLE "taggit_taggeditem";

CREATE TABLE "protoGraph_nodecategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "smInfo" text NOT NULL, "code" varchar(200) NULL, "description" varchar(200) NULL, "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"));
CREATE TABLE "protoGraph_edgecategory" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "smInfo" text NOT NULL, "code" varchar(200) NULL, "description" varchar(200) NULL, "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"));
CREATE TABLE "protoGraph_node" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "smInfo" text NOT NULL, "code" varchar(200) NULL, "label" varchar(200) NULL, "description" varchar(200) NULL, "idSource" integer NULL, "category_id" integer NULL REFERENCES "protoGraph_nodecategory" ("id"), "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"), UNIQUE ("idSource", "category_id"));
CREATE TABLE "protoGraph_edge" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "smInfo" text NOT NULL, "code" varchar(200) NULL, "label" varchar(200) NULL, "description" varchar(200) NULL, "category_id" integer NULL REFERENCES "protoGraph_edgecategory" ("id"), "node0_id" integer NULL REFERENCES "protoGraph_node" ("id"), "node1_id" integer NULL REFERENCES "protoGraph_node" ("id"), "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"), UNIQUE ("node0_id", "node1_id"));
CREATE TABLE "protoGraph_canvas" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "code" varchar(200) NULL, "description" varchar(200) NULL, "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"));
CREATE TABLE "protoGraph_canvasdetail" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "canvas_id" integer NULL REFERENCES "protoGraph_canvas" ("id"), "edge_id" integer NULL REFERENCES "protoGraph_edge" ("id"), "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"));


CREATE TABLE "rqEirq_dependance" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"), "fichier_id" integer NULL REFERENCES "rqEirq_fichier" ("id"), "produit_id" integer NULL REFERENCES "rqEirq_source" ("id"));
CREATE TABLE "rqEirq_fichier" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "code" varchar(200) NULL, "responsable_id" integer NULL REFERENCES "rqEirq_responsable" ("id"), "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"), "source_id" integer NULL REFERENCES "rqEirq_source" ("id"), "label" varchar(200) NULL);
CREATE TABLE "rqEirq_responsable" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "code" varchar(200) NULL, "coordonnees" varchar(200) NULL, "notes" varchar(200) NULL, "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"), "label" varchar(200) NULL);
CREATE TABLE "rqEirq_source" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "smNaturalCode" varchar(50) NULL, "smRegStatus" varchar(50) NULL, "smWflowStatus" varchar(50) NULL, "smCreatedOn" datetime NULL, "smModifiedOn" datetime NULL, "smUUID" char(32) NOT NULL, "code" varchar(200) NULL, "typeSource" varchar(20) NULL, "responsable_id" integer NULL REFERENCES "rqEirq_responsable" ("id"), "smCreatedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smModifiedBy_id" integer NULL REFERENCES "auth_user" ("id"), "smOwningTeam_id" integer NULL REFERENCES "protoLib_teamhierarchy" ("id"), "smOwningUser_id" integer NULL REFERENCES "auth_user" ("id"), "label" varchar(200) NULL);
CREATE TABLE "taggit_tag" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL UNIQUE, "slug" varchar(100) NOT NULL UNIQUE);
CREATE TABLE "taggit_taggeditem" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "object_id" integer NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "tag_id" integer NOT NULL REFERENCES "taggit_tag" ("id"));


CREATE INDEX "protoGraph_canvas_2236446a" ON "protoGraph_canvas" ("smCreatedBy_id");
CREATE INDEX "protoGraph_canvas_55b4cdd2" ON "protoGraph_canvas" ("smModifiedBy_id");
CREATE INDEX "protoGraph_canvas_5acf3455" ON "protoGraph_canvas" ("smOwningTeam_id");
CREATE INDEX "protoGraph_canvas_b0755eff" ON "protoGraph_canvas" ("smOwningUser_id");
CREATE INDEX "protoGraph_canvasdetail_2236446a" ON "protoGraph_canvasdetail" ("smCreatedBy_id");
CREATE INDEX "protoGraph_canvasdetail_4b1022ba" ON "protoGraph_canvasdetail" ("canvas_id");
CREATE INDEX "protoGraph_canvasdetail_55b4cdd2" ON "protoGraph_canvasdetail" ("smModifiedBy_id");
CREATE INDEX "protoGraph_canvasdetail_5acf3455" ON "protoGraph_canvasdetail" ("smOwningTeam_id");
CREATE INDEX "protoGraph_canvasdetail_b0755eff" ON "protoGraph_canvasdetail" ("smOwningUser_id");
CREATE INDEX "protoGraph_canvasdetail_df37d0b4" ON "protoGraph_canvasdetail" ("edge_id");
CREATE INDEX "protoGraph_edge_0799597f" ON "protoGraph_edge" ("node0_id");
CREATE INDEX "protoGraph_edge_2236446a" ON "protoGraph_edge" ("smCreatedBy_id");
CREATE INDEX "protoGraph_edge_55b4cdd2" ON "protoGraph_edge" ("smModifiedBy_id");
CREATE INDEX "protoGraph_edge_5acf3455" ON "protoGraph_edge" ("smOwningTeam_id");
CREATE INDEX "protoGraph_edge_6532ee89" ON "protoGraph_edge" ("node1_id");
CREATE INDEX "protoGraph_edge_b0755eff" ON "protoGraph_edge" ("smOwningUser_id");
CREATE INDEX "protoGraph_edge_b583a629" ON "protoGraph_edge" ("category_id");
CREATE INDEX "protoGraph_edgecategory_2236446a" ON "protoGraph_edgecategory" ("smCreatedBy_id");
CREATE INDEX "protoGraph_edgecategory_55b4cdd2" ON "protoGraph_edgecategory" ("smModifiedBy_id");
CREATE INDEX "protoGraph_edgecategory_5acf3455" ON "protoGraph_edgecategory" ("smOwningTeam_id");
CREATE INDEX "protoGraph_edgecategory_b0755eff" ON "protoGraph_edgecategory" ("smOwningUser_id");
CREATE INDEX "protoGraph_node_2236446a" ON "protoGraph_node" ("smCreatedBy_id");
CREATE INDEX "protoGraph_node_55b4cdd2" ON "protoGraph_node" ("smModifiedBy_id");
CREATE INDEX "protoGraph_node_5acf3455" ON "protoGraph_node" ("smOwningTeam_id");
CREATE INDEX "protoGraph_node_b0755eff" ON "protoGraph_node" ("smOwningUser_id");
CREATE INDEX "protoGraph_node_b583a629" ON "protoGraph_node" ("category_id");


CREATE INDEX "rqEirq_dependance_2236446a" ON "rqEirq_dependance" ("smCreatedBy_id");
CREATE INDEX "rqEirq_dependance_55b4cdd2" ON "rqEirq_dependance" ("smModifiedBy_id");
CREATE INDEX "rqEirq_dependance_5acf3455" ON "rqEirq_dependance" ("smOwningTeam_id");
CREATE INDEX "rqEirq_dependance_8eb6132c" ON "rqEirq_dependance" ("produit_id");
CREATE INDEX "rqEirq_dependance_b0755eff" ON "rqEirq_dependance" ("smOwningUser_id");
CREATE INDEX "rqEirq_dependance_d31e77c8" ON "rqEirq_dependance" ("fichier_id");
CREATE INDEX "rqEirq_fichier_0afd9202" ON "rqEirq_fichier" ("source_id");
CREATE INDEX "rqEirq_fichier_1ba06e10" ON "rqEirq_fichier" ("responsable_id");
CREATE INDEX "rqEirq_fichier_2236446a" ON "rqEirq_fichier" ("smCreatedBy_id");
CREATE INDEX "rqEirq_fichier_55b4cdd2" ON "rqEirq_fichier" ("smModifiedBy_id");
CREATE INDEX "rqEirq_fichier_5acf3455" ON "rqEirq_fichier" ("smOwningTeam_id");
CREATE INDEX "rqEirq_fichier_b0755eff" ON "rqEirq_fichier" ("smOwningUser_id");
CREATE INDEX "rqEirq_responsable_2236446a" ON "rqEirq_responsable" ("smCreatedBy_id");
CREATE INDEX "rqEirq_responsable_55b4cdd2" ON "rqEirq_responsable" ("smModifiedBy_id");
CREATE INDEX "rqEirq_responsable_5acf3455" ON "rqEirq_responsable" ("smOwningTeam_id");
CREATE INDEX "rqEirq_responsable_b0755eff" ON "rqEirq_responsable" ("smOwningUser_id");
CREATE INDEX "rqEirq_source_1ba06e10" ON "rqEirq_source" ("responsable_id");
CREATE INDEX "rqEirq_source_2236446a" ON "rqEirq_source" ("smCreatedBy_id");
CREATE INDEX "rqEirq_source_55b4cdd2" ON "rqEirq_source" ("smModifiedBy_id");
CREATE INDEX "rqEirq_source_5acf3455" ON "rqEirq_source" ("smOwningTeam_id");
CREATE INDEX "rqEirq_source_b0755eff" ON "rqEirq_source" ("smOwningUser_id");

