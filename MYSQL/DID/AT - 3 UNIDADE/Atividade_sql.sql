create database atividade;
use atividade;

create table pessoa(
	id int
);

create table telefone(
	id int,
    numero bigint
);

alter table pessoa
add column nome varchar(50) not null;

alter table pessoa add column sobre_nome varchar(50) default "Farias";

select*from pessoa;

alter table pessoa 
drop column id;

alter table pessoa
add column id int auto_increment primary key;

select*from telefone;

alter table telefone
modify column numero bigint not null;

alter table telefone
add column FK_Id_pessoa int;

alter table telefone
add constraint FK_Id_pessoa foreign key (FK_Id_pessoa) references pessoa(id)