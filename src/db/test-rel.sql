
--==============================================================
-- Table : A1_PHRA_INV
--==============================================================


drop table A1_PHRA_INV ;
create table A1_PHRA_INV (
AN_IMPOSI            NUMERIC(4)           not null,
COD_PHRA             VARCHAR(10)          not null,
DH_CREA_PHRA         DATE                 not null,
);

--==============================================================
-- Table : A1_CATG_PHRA_INV
--==============================================================
drop table A1_CATG_PHRA_INV; 
create table A1_CATG_PHRA_INV (
AN_IMPOSI            NUMERIC(4)           not null,
COD_PHRA             VARCHAR(10)          not null,
DH_CREA              DATE                 not null,
COD_CATG_PHRA        VARCHAR(15)          not null,
foreign key (AN_IMPOSI, COD_PHRA) references A1_PHRA_INV (AN_IMPOSI, COD_PHRA)
);
