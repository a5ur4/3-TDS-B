CREATE DATABASE Faz_Tudo;

USE Faz_Tudo;

CREATE TABLE Endereço(
	Id int auto_increment,
    Rua varchar (255) not null,
    Numero int not null,
    Bairro varchar (255), 
    Cidade varchar (255),
    Complemento varchar (255),
    Primary Key (Id)
);

CREATE TABLE Prestador(
	Id int auto_increment,
    Nome varchar (255),
    Horário_inicio varchar(255) not null,
    Horario_fim varchar(255) not null,
    Tipo_Serviço varchar (255),
    Telefone varchar (255),
    Fk_Id_end int, 
    primary key (Id),
    Foreign key (Fk_Id_end) references Endereço(Id)
);

CREATE TABLE Beneficiario(
	Cod int auto_increment,
    Nome varchar (255),
    Telefone varchar (255),
    FK_ID_end int,
    primary key (Cod),
    foreign key (FK_ID_end) references Endereço(Id)
);

CREATE TABLE Atendimento(
	id int auto_increment,
    Data_ date,
    Local_ varchar (255),
    FK_Cod_Ben int,
    FK_Id_Pres int,
	Primary key (id),
    foreign key (FK_Cod_Ben) references Beneficiario(Cod),
	foreign key (FK_Id_Pres) references Prestador(Id)
);

CREATE TABLE Servico_Aten(
	Id int auto_increment,
    Descricao varchar (255),
    Valor varchar (255) not null,
    FK_id_Aten int,
    primary key (Id),
    foreign key (FK_id_Aten) references Atendimento(id) 
);

CREATE TABLE Material_Serv(
	Id int auto_increment,
    Descricao varchar (255),
    Valor varchar (255) not null,
    FK_Id_Servi int,
    primary key (Id),
    foreign key (FK_Id_Servi) references Servico_Aten(ID)
);

INSERT INTO Endereço (Rua, Numero, Bairro, Cidade, Complemento)
VALUES ("MARIA BEZERRA", 46, "SALGADO", "CARUARU", "PROXIMO A PRAÇA");
INSERT INTO Endereço (Rua, Numero, Bairro, Cidade, Complemento)
VALUES ("THEODORO BANDEIRANTE", 23, "BOA VIAGEM", "RECIFE", "PROXIMO A BARBEARIA");
INSERT INTO Endereço (Rua, Numero, Bairro, Cidade, Complemento)
VALUES ("PARANAUE DOS SANTOS", 78, "LIBERDADE", "SÃO PAULO", "PROXIMO AO POSTO");
INSERT INTO Endereço (Rua, Numero, Bairro, Cidade, Complemento)
VALUES ("PEIXONAUTA DA SILVA", 39, "JACARE PAGUARA", "RIO DE JANEIRO", "PROXIMO AO TEATRO");
INSERT INTO Endereço (Rua, Numero, Bairro, Cidade, Complemento)
VALUES ("LOURO JOSE", 76, "LOURO PRETO", "MACEIO", "PROXIMO AO MAGAZINE LUIZA");

INSERT INTO Prestador (Nome, Horário_inicio, Horario_fim, Tipo_serviço, Telefone, Fk_Id_end)
VALUES ("Jefferson", "8:00 Horas", "16:00 Horas", "Construção civil", 992850481, 1);
INSERT INTO Prestador (Nome, Horário_inicio, Horario_fim, Tipo_serviço, Telefone, Fk_Id_end)
VALUES ("Jonas", "9:00 Horas", "17:00 Horas", "Vendedor de Dudu", 997812414, 2);
INSERT INTO Prestador (Nome, Horário_inicio, Horario_fim, Tipo_serviço, Telefone, Fk_Id_end)
VALUES ("Jorge", "7:00 Horas", "18:00 Horas", "Zelador", 993497501, 3);
INSERT INTO Prestador (Nome, Horário_inicio, Horario_fim, Tipo_serviço, Telefone, Fk_Id_end)
VALUES ("Jairo", "5:00 Horas", "20:00 Horas", "Segurança", 994822233, 4);
INSERT INTO Prestador (Nome, Horário_inicio, Horario_fim, Tipo_serviço, Telefone, Fk_Id_end)
VALUES ("Jonanthan", "10:00 Horas", "19:00 Horas", "Açougueiro", 997829022, 5);

INSERT INTO Beneficiario (Nome, FK_Id_end)
VALUES ("Carlos", 1);
INSERT INTO Beneficiario (Nome, FK_ID_end)
VALUES ("Celsio", 2);
INSERT INTO Beneficiario (Nome, FK_ID_end)
VALUES ("Cibele", 3);
INSERT INTO Beneficiario (Nome, FK_ID_end)
VALUES ("Cleiton", 4);
INSERT INTO Beneficiario (Nome, FK_ID_end)
VALUES ("Capixaba", 5);

INSERT INTO Atendimento (Data_, Local_, FK_Cod_Ben, FK_Id_Pres)
VALUES ("2020-03-19", "Avenida Rui Barbosa", 2, 2);
INSERT INTO Atendimento (Data_, Local_, FK_Cod_Ben, FK_Id_Pres)
VALUES ("2019-05-20", "Avenida Agamenom Magalhães", 3, 3);
INSERT INTO Atendimento (Data_, Local_, FK_Cod_Ben, FK_Id_Pres)
VALUES ("2021-07-21", "Avenida Brasil", 4, 4);
INSERT INTO Atendimento (Data_, Local_, FK_Cod_Ben, FK_Id_Pres)
VALUES ("2012-09-30", "Rua Nossa senhora das Dores", 5, 5);
INSERT INTO Atendimento (Data_, Local_, FK_Cod_Ben, FK_Id_Pres)
VALUES ("2013-12-05", "Rua Bahia", 1, 1);

INSERT INTO Servico_Aten (Descricao, Valor, FK_id_Aten)
VALUES ("Reconstrução do muro", "92 Reais", 1);
INSERT INTO Servico_Aten (Descricao, Valor, FK_id_Aten)
VALUES ("Reconstrução da bancada", "45 Reais", 2);
INSERT INTO Servico_Aten (Descricao, Valor, FK_id_Aten)
VALUES ("Construção da pratelheira", "50 Reais", 3);
INSERT INTO Servico_Aten (Descricao, Valor, FK_id_Aten)
VALUES ("Remendo do casaco", "60 Reais", 4);
INSERT INTO Servico_Aten (Descricao, Valor, FK_id_Aten)
VALUES ("Montagem do computador", "70 Reais", 5);

INSERT INTO Material_Serv (Descricao, Valor, FK_Id_Servi)
VALUES ("Cimento", "15 Reais", 1);
INSERT INTO Material_Serv (Descricao, Valor, FK_Id_Servi)
VALUES ("Brita", "20 Reais", 2);
INSERT INTO Material_Serv (Descricao, Valor, FK_Id_Servi)
VALUES ("Areia fina", "12 Reais", 3);
INSERT INTO Material_Serv (Descricao, Valor, FK_Id_Servi)
VALUES ("Marmore", "50 reais", 4);
INSERT INTO Material_Serv (Descricao, Valor, FK_Id_Servi)
VALUES ("Granito", "40 reais", 5);

SELECT*FROM Endereço;
SELECT*FROM Prestador;
SELECT*FROM Beneficiario;
SELECT*FROM Atendimento;
SELECT*FROM Servico_Aten;
SELECT*FROM Material_Serv;

DROP TABLE Material_Serv;
DROP TABLE Servico_Aten;
DROP TABLE Atendimento;
DROP TABLE Beneficiario;
DROP TABLE Prestador;
DROP TABLE Endereço;

DROP DATABASE Faz_Tudo;