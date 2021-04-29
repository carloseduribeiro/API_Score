CREATE DATABASE IF NOT EXISTS score_db;
USE score_db;

CREATE TABLE IF NOT EXISTS pessoa (
	cpf VARCHAR(11) PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	data_nascimento DATE NOT NULL,
	divida DECIMAL(65, 2) NOT NULL,
	score SMALLINT NOT NULL DEFAULT 0
) ENGINE=InnoDB;

INSERT INTO pessoa VALUES ('98465715652', 'Olinda Gadelha Lustosa', '1999-06-25', 6000.00, 127);
INSERT INTO pessoa VALUES ('14556576518', 'Ana Frajuca Ávila', '2002-12-29', 650.00, 580);
INSERT INTO pessoa VALUES ('06548245658', 'Anaísa Garrau Resende', '2004-04-28', 0.00, 500);
INSERT INTO pessoa VALUES ('07415682345', 'Bella Carvalhal Marmou', '1996-06-03', 0.00, 929);
INSERT INTO pessoa VALUES ('30218956548', 'Rui Protásio Lameira', '2005-03-27', 0.00, 500);
INSERT INTO pessoa VALUES ('25389453302', 'Eden Toste Toledo', '1985-11-05', 270.5, 584);
INSERT INTO pessoa VALUES ('06548913548', 'Tatiana Ximenes Covilhã', '1968-06-20', 15862.98, 80);
INSERT INTO pessoa VALUES ('65481265002', 'Ayesha Malta Campos', '1963-12-15', 0.00, 950);
INSERT INTO pessoa VALUES ('65100250812', 'James Lage Corte-Real', '2020-07-01', 0.00, 500);
INSERT INTO pessoa VALUES ('95103512305', 'Andressa Leiria Quintais', '2003-01-26', 0.00, 1000);
INSERT INTO pessoa VALUES ('65109199502', 'Weza Félix Rosado', '1992-10-17', 0.00, 500);
INSERT INTO pessoa VALUES ('12305595108', 'Milan Domingues Rebimbas', '1963-06-07', 1250.12, 462);
INSERT INTO pessoa VALUES ('09510265518', 'Aya Fortunato Lamenha', '2000-10-26', 0.00, 852);
INSERT INTO pessoa VALUES ('65106510505', 'Kaio Zarco Bandeira', '1990-02-01', 260.00, 345);
INSERT INTO pessoa VALUES ('01565480518', 'Rogério Valim Charneca', '1996-03-06', 0.00, 984);
INSERT INTO pessoa VALUES ('65162000825', 'Samaritana Rebimbas Teodoro', '2003-04-01', 29.90, 716);
INSERT INTO pessoa VALUES ('06516513215', 'Rita Adarga Caetano', '1998-05-16', 520.28, 402);
INSERT INTO pessoa VALUES ('65208102251', 'Rodrigo Cancela Silva', '2004-02-03', 0.00, 500);
INSERT INTO pessoa VALUES ('91029810205', 'Iris Couceiro Bugalho', '1999-02-25', 0.00, 302);
