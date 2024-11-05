USE `classicmodels`;

DROP TABLE IF EXISTS `philipshue`;
DROP TABLE IF EXISTS `nanoleaf`;

CREATE TABLE philipsHue(
    id int AUTO_INCREMENT not null,
    name varchar(255) not null,
    ip varchar(255) not null,
    port int not null,
    farbe varchar(255) not null,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE Nanoleaf(
    id int AUTO_INCREMENT not null,
    name varchar(255) not null,
    ip varchar(255) not null,
    port int not null,
    panelCount int,
    PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;