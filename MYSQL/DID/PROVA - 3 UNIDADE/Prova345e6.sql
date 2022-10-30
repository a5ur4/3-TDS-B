CREATE DATABASE Prova2;

use Prova2;

CREATE TABLE tabela1(
	id int auto_increment,
    valor decimal(6,2) default 1.55,
    PRIMARY KEY (id)
);

insert into tabela1(produto) value("Carro");
insert into tabela1 (produto) value("Moto");

CREATE TABLE tabela2(
    nome varchar(255) default "ABC"
);

alter table tabela1 add column produto enum('Carro','Moto') not null;
alter table tabela1 add column remover1 tinyint default 1;

alter table tabela2 add column id int auto_increment primary key;
alter table tabela2 add column remover2 BLOB not null;

alter table tabela1 drop column remover1;
alter table tabela2 drop column remover2;

alter table tabela1 modify column valor varchar(255) not null;
alter table tabela2 modify column nome varchar(255) not null default "Maria";

alter table tabela2 modify column nome int;
alter table tabela2 add column texto text unique;

truncate table tabela2;
INSERT INTO tabela1(produto) VALUES ("Carro");
INSERT INTO tabela1(produto) VALUES ("Moto");
INSERT INTO tabela1() VALUES ();
INSERT INTO tabela1() VALUES ();


INSERT INTO tabela2() VALUES ();
INSERT INTO tabela2() VALUES ();
INSERT INTO tabela2() VALUES ();
INSERT INTO tabela2() VALUES ();
