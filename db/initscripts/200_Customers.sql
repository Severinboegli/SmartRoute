USE `classicmodels`;

DROP TABLE IF EXISTS `customers`;

CREATE TABLE `customers` (
  `firstname` varchar(20) NOT NULL,
  `name` varchar(20) NOT NULL,
  `plz` int NOT NULL,
  `city` varchar(15) NOT NULL,
  `phonenumber` varchar(15) NOT NULL,
  `customerSince` date NOT NULL,
  `customerId` int not null AUTO_INCREMENT,
  PRIMARY KEY (`customerId`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

