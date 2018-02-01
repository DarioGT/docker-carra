CREATE TABLE 
"auth_group" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE 
"auth_group_permissions" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"group_id" integer NOT NULL REFERENCES 
"auth_group" (
"id"), 
"permission_id" integer NOT NULL REFERENCES 
"auth_permission" (
"id"), UNIQUE (
"group_id", 
"permission_id"));
CREATE TABLE 
"auth_permission" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"content_type_id" integer NOT NULL REFERENCES 
"django_content_type" (
"id"), 
"codename" varchar(100) NOT NULL, 
"name" varchar(255) NOT NULL, UNIQUE (
"content_type_id", 
"codename"));
CREATE TABLE 
"auth_user" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"password" varchar(128) NOT NULL, 
"is_superuser" bool NOT NULL, 
"username" varchar(30) NOT NULL UNIQUE, 
"first_name" varchar(30) NOT NULL, 
"last_name" varchar(30) NOT NULL, 
"email" varchar(254) NOT NULL, 
"is_staff" bool NOT NULL, 
"is_active" bool NOT NULL, 
"date_joined" datetime NOT NULL, 
"last_login" datetime NULL);
CREATE TABLE 
"auth_user_groups" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"user_id" integer NOT NULL REFERENCES 
"auth_user" (
"id"), 
"group_id" integer NOT NULL REFERENCES 
"auth_group" (
"id"), UNIQUE (
"user_id", 
"group_id"));
CREATE TABLE 
"auth_user_user_permissions" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"user_id" integer NOT NULL REFERENCES 
"auth_user" (
"id"), 
"permission_id" integer NOT NULL REFERENCES 
"auth_permission" (
"id"), UNIQUE (
"user_id", 
"permission_id"));
CREATE TABLE 
"django_admin_log" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"action_time" datetime NOT NULL, 
"object_id" text NULL, 
"object_repr" varchar(200) NOT NULL, 
"action_flag" smallint unsigned NOT NULL, 
"change_message" text NOT NULL, 
"content_type_id" integer NULL REFERENCES 
"django_content_type" (
"id"), 
"user_id" integer NOT NULL REFERENCES 
"auth_user" (
"id"));
CREATE TABLE 
"django_content_type" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"app_label" varchar(100) NOT NULL, 
"model" varchar(100) NOT NULL, UNIQUE (
"app_label", 
"model"));
CREATE TABLE 
"django_migrations" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"app" varchar(255) NOT NULL, 
"name" varchar(255) NOT NULL, 
"applied" datetime NOT NULL);
CREATE TABLE 
"django_session" (
"session_key" varchar(40) NOT NULL PRIMARY KEY, 
"session_data" text NOT NULL, 
"expire_date" datetime NOT NULL);
CREATE TABLE 
"protoExt_customdefinition" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"active" bool NOT NULL, 
"overWrite" bool NOT NULL, 
"metaDefinition" text NOT NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"code", 
"smOwningUser_id"));
CREATE TABLE 
"protoExt_parameters" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"parameterKey" varchar(250) NOT NULL, 
"parameterTag" varchar(250) NULL, 
"parameterValue" varchar(250) NOT NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"));
CREATE TABLE 
"protoExt_viewdefinition" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"code" varchar(200) NOT NULL UNIQUE, 
"description" text NULL, 
"active" bool NOT NULL, 
"overWrite" bool NOT NULL, 
"metaDefinition" text NOT NULL);
CREATE TABLE 
"protoLib_contextentity" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"propName" varchar(200) NULL, 
"active" bool NOT NULL, 
"contextVar_id" integer NOT NULL REFERENCES 
"protoLib_contextvar" (
"id"), 
"entity_id" integer NOT NULL REFERENCES 
"django_content_type" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"contextVar_id", 
"entity_id"));
CREATE TABLE 
"protoLib_contextuser" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"propValue" varchar(200) NULL, 
"description" text NULL, 
"active" bool NOT NULL, 
"contextVar_id" integer NOT NULL REFERENCES 
"protoLib_contextvar" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"contextVar_id", 
"smOwningUser_id"));
CREATE TABLE 
"protoLib_contextvar" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"propName" varchar(500) NOT NULL, 
"description" text NULL, 
"modelCType_id" integer NOT NULL REFERENCES 
"django_content_type" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"modelCType_id", 
"propName"));
CREATE TABLE 
"protoLib_entitymap" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"entityConfig" text NOT NULL, 
"entityBase_id" integer NOT NULL UNIQUE REFERENCES 
"django_content_type" (
"id"));
CREATE TABLE 
"protoLib_logger" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smCreatedOn" datetime NULL, 
"logType" varchar(10) NOT NULL, 
"logObject" varchar(250) NULL, 
"logNotes" varchar(250) NULL, 
"logInfo" text NULL, 
"logKey" varchar(5) NOT NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"));
CREATE TABLE 
"protoLib_teamhierarchy" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"code" varchar(200) NOT NULL UNIQUE, 
"description" text NULL, 
"site" integer NULL, 
"parentNode_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"));
CREATE TABLE 
"protoLib_userprofile" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"language" varchar(500) NULL, 
"userTree" varchar(500) NULL, 
"userConfig" text NOT NULL, 
"user_id" integer NOT NULL UNIQUE REFERENCES 
"auth_user" (
"id"), 
"userTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"));
CREATE TABLE 
"prototype_diagram" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"notes" text NULL, 
"title" varchar(100) NULL, 
"prefix" varchar(20) NULL, 
"graphLevel" integer NULL, 
"grphMode" integer NULL, 
"graphForm" integer NULL, 
"showPrpType" bool NOT NULL, 
"showBorder" bool NOT NULL, 
"showFKey" bool NOT NULL, 
"project_id" integer NOT NULL REFERENCES 
"prototype_project" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"project_id", 
"code", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_diagramentity" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"info" text NOT NULL, 
"diagram_id" integer NOT NULL REFERENCES 
"prototype_diagram" (
"id"), 
"entity_id" integer NOT NULL REFERENCES 
"prototype_entity" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"diagram_id", 
"entity_id", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_entity" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"code" varchar(200) NOT NULL, 
"dbName" varchar(200) NULL, 
"description" text NULL, 
"model_id" integer NOT NULL REFERENCES 
"prototype_model" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"model_id", 
"code", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_model" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"code" varchar(200) NOT NULL, 
"category" varchar(50) NULL, 
"modelPrefix" varchar(50) NULL, 
"description" text NULL, 
"project_id" integer NOT NULL REFERENCES 
"prototype_project" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"project_id", 
"code", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_project" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"dbEngine" varchar(20) NULL, 
"dbName" varchar(200) NULL, 
"dbUser" varchar(200) NULL, 
"dbPassword" varchar(200) NULL, 
"dbHost" varchar(200) NULL, 
"dbPort" varchar(200) NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"code", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_property" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"code" varchar(200) NOT NULL, 
"baseType" varchar(50) NULL, 
"prpLength" integer NULL, 
"prpScale" integer NULL, 
"prpDefault" varchar(50) NULL, 
"prpChoices" text NULL, 
"description" text NULL, 
"notes" text NULL, 
"isPrimary" bool NOT NULL, 
"isLookUpResult" bool NOT NULL, 
"isNullable" bool NOT NULL, 
"isRequired" bool NOT NULL, 
"isReadOnly" bool NOT NULL, 
"isForeign" bool NOT NULL, 
"vType" varchar(50) NULL, 
"isSensitive" bool NOT NULL, 
"isEssential" bool NOT NULL, 
"crudType" varchar(20) NULL, 
"dbName" varchar(200) NULL, 
"entity_id" integer NOT NULL REFERENCES 
"prototype_entity" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"entity_id", 
"code", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_propertyequivalence" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"smInfo" text NOT NULL, 
"description" text NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), 
"sourceProperty_id" integer NULL REFERENCES 
"prototype_property" (
"id"), 
"targetProperty_id" integer NULL REFERENCES 
"prototype_property" (
"id"), UNIQUE (
"sourceProperty_id", 
"targetProperty_id", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_prototable" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"info" text NOT NULL, 
"entity_id" integer NOT NULL REFERENCES 
"prototype_entity" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"));
CREATE TABLE 
"prototype_prototype" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"notes" text NULL, 
"metaDefinition" text NULL, 
"entity_id" integer NOT NULL REFERENCES 
"prototype_entity" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smVersion_id" integer NOT NULL REFERENCES 
"prototype_protoversiontitle" (
"id"), UNIQUE (
"entity_id", 
"code", 
"smOwningTeam_id", 
"smVersion_id"));
CREATE TABLE 
"prototype_protoversiontitle" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"versionCode" varchar(50) NULL, 
"description" text NULL, 
"active" bool NOT NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"versionBase_id" integer NULL REFERENCES 
"prototype_protoversiontitle" (
"id"));
CREATE TABLE 
"prototype_relationship" (
"property_ptr_id" integer NOT NULL PRIMARY KEY REFERENCES 
"prototype_property" (
"id"), 
"relatedName" varchar(50) NULL, 
"baseMin" varchar(50) NULL, 
"baseMax" varchar(50) NULL, 
"refMin" varchar(50) NULL, 
"refMax" varchar(50) NULL, 
"onRefDelete" varchar(50) NULL, 
"typeRelation" varchar(50) NULL, 
"refEntity_id" integer NULL REFERENCES 
"prototype_entity" (
"id"));
CREATE TABLE 
"rai01ref_artefact" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"info" text NOT NULL, 
"copyFrom_id" integer NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"docType_id" integer NULL REFERENCES 
"rai01ref_doctype" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"capacity_id" integer NULL REFERENCES 
"rai01ref_capacity" (
"id"), 
"requirement_id" integer NULL REFERENCES 
"rai01ref_requirement" (
"id"), 
"refArtefact_id" integer NULL REFERENCES 
"rai01ref_artefact" (
"id"));
CREATE TABLE 
"rai01ref_artefactcapacity" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"artefact_id" integer NOT NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"capacity_id" integer NOT NULL REFERENCES 
"rai01ref_capacity" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"isMain" bool NOT NULL, UNIQUE (
"artefact_id", 
"capacity_id"));
CREATE TABLE 
"rai01ref_artefactcomposition" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"condition" text NULL, 
"notes" text NULL, 
"description" text NULL, 
"containerArt_id" integer NOT NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"inputArt_id" integer NOT NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"outputArt_id" integer NULL REFERENCES 
"rai01ref_artefact" (
"id"));
CREATE TABLE 
"rai01ref_artefactrequirement" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"artefact_id" integer NOT NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"requirement_id" integer NOT NULL REFERENCES 
"rai01ref_requirement" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"isMain" bool NOT NULL, UNIQUE (
"artefact_id", 
"requirement_id"));
CREATE TABLE 
"rai01ref_artefactsource" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"artefact_id" integer NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"source_id" integer NULL REFERENCES 
"rai01ref_source" (
"id"), UNIQUE (
"source_id", 
"artefact_id"));
CREATE TABLE 
"rai01ref_capacity" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"info" text NOT NULL, 
"copyFrom_id" integer NULL REFERENCES 
"rai01ref_capacity" (
"id"), 
"docType_id" integer NULL REFERENCES 
"rai01ref_doctype" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"refCapacity_id" integer NULL REFERENCES 
"rai01ref_capacity" (
"id"));
CREATE TABLE 
"rai01ref_docattribute" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"baseType" varchar(50) NULL, 
"prpLength" integer NULL, 
"prpScale" integer NULL, 
"vType" varchar(50) NULL, 
"prpDefault" varchar(50) NULL, 
"prpChoices" text NULL, 
"isRequired" bool NOT NULL, 
"isSensitive" bool NOT NULL, 
"crudType" varchar(20) NULL, 
"description" text NULL, 
"docType_id" integer NULL REFERENCES 
"rai01ref_doctype" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"docType_id", 
"code"));
CREATE TABLE 
"rai01ref_doctype" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"document" varchar(11) NOT NULL, 
"category" varchar(50) NULL, 
"notes" text NULL, 
"description" text NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"dtype" varchar(200) NOT NULL, UNIQUE (
"document", 
"dtype"));
CREATE TABLE 
"rai01ref_projectartefact" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"artefact_id" integer NOT NULL REFERENCES 
"rai01ref_artefact" (
"id"), 
"projet_id" integer NOT NULL REFERENCES 
"rai01ref_projet" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"artefact_id", 
"projet_id"));
CREATE TABLE 
"rai01ref_projectcapacity" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"capacity_id" integer NOT NULL REFERENCES 
"rai01ref_capacity" (
"id"), 
"projet_id" integer NOT NULL REFERENCES 
"rai01ref_projet" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"projet_id", 
"capacity_id"));
CREATE TABLE 
"rai01ref_projectrequirement" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"projet_id" integer NOT NULL REFERENCES 
"rai01ref_projet" (
"id"), 
"requirement_id" integer NOT NULL REFERENCES 
"rai01ref_requirement" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), UNIQUE (
"projet_id", 
"requirement_id"));
CREATE TABLE 
"rai01ref_projet" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"notes" text NULL, 
"description" text NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"));
CREATE TABLE 
"rai01ref_requirement" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"description" text NULL, 
"info" text NOT NULL, 
"copyFrom_id" integer NULL REFERENCES 
"rai01ref_requirement" (
"id"), 
"docType_id" integer NULL REFERENCES 
"rai01ref_doctype" (
"id"), 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"refRequirement_id" integer NULL REFERENCES 
"rai01ref_requirement" (
"id"));
CREATE TABLE 
"rai01ref_source" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"smNaturalCode" varchar(50) NULL, 
"smRegStatus" varchar(50) NULL, 
"smWflowStatus" varchar(50) NULL, 
"smCreatedOn" datetime NULL, 
"smModifiedOn" datetime NULL, 
"smUUID" char(32) NOT NULL, 
"code" varchar(200) NOT NULL, 
"reference" varchar(200) NULL, 
"notes" text NULL, 
"description" text NULL, 
"smCreatedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smModifiedBy_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"smOwningTeam_id" integer NULL REFERENCES 
"protoLib_teamhierarchy" (
"id"), 
"smOwningUser_id" integer NULL REFERENCES 
"auth_user" (
"id"));
CREATE TABLE 
"reversion_revision" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"date_created" datetime NOT NULL, 
"comment" text NOT NULL, 
"user_id" integer NULL REFERENCES 
"auth_user" (
"id"), 
"manager_slug" varchar(191) NOT NULL);
CREATE TABLE 
"reversion_version" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"object_id" text NOT NULL, 
"object_id_int" integer NULL, 
"format" varchar(255) NOT NULL, 
"serialized_data" text NOT NULL, 
"object_repr" text NOT NULL, 
"content_type_id" integer NOT NULL REFERENCES 
"django_content_type" (
"id"), 
"revision_id" integer NOT NULL REFERENCES 
"reversion_revision" (
"id"));
CREATE TABLE 
"taggit_tag" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL UNIQUE, 
"slug" varchar(100) NOT NULL UNIQUE);
CREATE TABLE 
"taggit_taggeditem" (
"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"object_id" integer NOT NULL, 
"content_type_id" integer NOT NULL REFERENCES 
"django_content_type" (
"id"), 
"tag_id" integer NOT NULL REFERENCES 
"taggit_tag" (
"id"));
