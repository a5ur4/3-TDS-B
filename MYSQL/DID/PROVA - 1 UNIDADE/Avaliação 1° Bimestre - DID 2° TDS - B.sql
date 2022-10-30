CREATE DATABASE clinica_medica;

USE clinica_medica;

CREATE TABLE Pessoa(
	id int auto_increment,
    nome varchar(50) not null,
    data_nascimento date not null,
    Primary Key (id)
);

CREATE TABLE Medico(
	id int auto_increment,
    nome varchar(50) not null,
    especialidade varchar(50) not null unique,
    Primary Key (id)
);

CREATE TABLE Agenda(
	data_hora datetime not null unique,
    FK_id_Pessoa int,
    Foreign key (Fk_id_Pessoa) references Pessoa (id),
    FK_id_Medico int,
    Foreign key (Fk_id_Medico) references Medico (id),
	Primary key (data_hora, FK_id_Pessoa, FK_id_Medico)
);

INSERT INTO Pessoa (nome, data_nascimento)
VALUES ("Zezinho", "2001/01/01");
INSERT INTO Pessoa (nome, data_nascimento)
VALUES ("Faustogildo", "2018/05/05");
INSERT INTO Pessoa (nome, data_nascimento)
VALUES ("Mariazinha", "1991/10/26");

INSERT INTO Medico (nome, especialidade)
VALUES ("Drauzio", "Pediatra");
INSERT INTO Medico (nome, especialidade)
VALUES ("Elizeu", "Otorrinolaringologista");

INSERT INTO Agenda (data_hora, FK_id_Pessoa, FK_id_Medico)
VALUES ("2022-04-08 08:00:00", "1", "1");
INSERT INTO Agenda (data_hora, FK_id_Pessoa, FK_id_Medico)
VALUES ("2022-04-08 09:30:00", "3", "1");
INSERT INTO Agenda (data_hora, FK_id_Pessoa, FK_id_Medico)
VALUES ("2022-04-08 11:30:00", "2", "2");

SELECT * FROM Pessoa;
SELECT * FROM Medico;
SELECT * FROM Agenda;

DELETE FROM Agenda WHERE FK_id_Pessoa= 1;
DELETE FROM Agenda WHERE FK_id_Medico= 2;

DELETE FROM Pessoa WHERE id= 1;
DELETE FROM Medico WHERE id= 2;

DROP TABLE Agenda;
DROP TABLE Medico;
DROP TABLE Pessoa;

DROP DATABASE clinica_medica;