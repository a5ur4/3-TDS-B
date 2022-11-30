create database atividade;

use atividade;

create table classe(
Nome varchar(255),
Turma varchar(100),
Curso varchar(100),
Mensalidade float,
primary key (Nome)
);

create table Professor(
Nome varchar(100),
Salario float
);

select * from classe;


drop table Classe;