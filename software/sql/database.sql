SET NAMES utf8;
SET time_zone = '+00:00';
SET foreign_key_checks = 0;
SET sql_mode = 'NO_AUTO_VALUE_ON_ZERO';

SET NAMES utf8mb4;

DROP TABLE IF EXISTS `categorias`;
CREATE TABLE `categorias` (
  `id_categoria` int NOT NULL AUTO_INCREMENT,
  `nombre_categoria` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `categorias` (`id_categoria`, `nombre_categoria`) VALUES
(1,	'Electrónica'),
(2,	'Ropa');

DROP TABLE IF EXISTS `clientes`;
CREATE TABLE `clientes` (
  `id_cliente` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(100) DEFAULT NULL,
  `correo` varchar(100) DEFAULT NULL,
  `fecha_registro` date DEFAULT NULL,
  PRIMARY KEY (`id_cliente`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `clientes` (`id_cliente`, `nombre`, `correo`, `fecha_registro`) VALUES
(1,	'Juan Pérez',	'juan.perez@example.com',	'2023-01-15'),
(2,	'Ana Gómez',	'ana.gomez@example.com',	'2023-03-20'),
(3,	'Luis García',	'luis.garcia@example.com',	'2023-05-10'),
(4,	'Marta Díaz',	'marta.diaz@example.com',	'2023-07-05');

DROP TABLE IF EXISTS `productos`;
CREATE TABLE `productos` (
  `id_producto` int NOT NULL AUTO_INCREMENT,
  `nombre_producto` varchar(100) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `productos` (`id_producto`, `nombre_producto`, `precio`) VALUES
(1,	'Laptop',	800.00),
(2,	'Smartphone',	400.00),
(3,	'Camiseta',	20.00),
(4,	'Auriculares',	50.00);

DROP TABLE IF EXISTS `productos_categorias`;
CREATE TABLE `productos_categorias` (
  `id_producto` int DEFAULT NULL,
  `id_categoria` int DEFAULT NULL,
  KEY `id_producto` (`id_producto`),
  KEY `id_categoria` (`id_categoria`),
  CONSTRAINT `productos_categorias_ibfk_1` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`),
  CONSTRAINT `productos_categorias_ibfk_2` FOREIGN KEY (`id_categoria`) REFERENCES `categorias` (`id_categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `productos_categorias` (`id_producto`, `id_categoria`) VALUES
(1,	1),
(2,	1),
(3,	2),
(4,	1);

DROP TABLE IF EXISTS `ventas`;
CREATE TABLE `ventas` (
  `id_venta` int NOT NULL AUTO_INCREMENT,
  `id_cliente` int DEFAULT NULL,
  `id_producto` int DEFAULT NULL,
  `fecha_venta` date DEFAULT NULL,
  `cantidad` int DEFAULT NULL,
  `total` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`id_venta`),
  KEY `id_cliente` (`id_cliente`),
  KEY `id_producto` (`id_producto`),
  CONSTRAINT `ventas_ibfk_1` FOREIGN KEY (`id_cliente`) REFERENCES `clientes` (`id_cliente`),
  CONSTRAINT `ventas_ibfk_2` FOREIGN KEY (`id_producto`) REFERENCES `productos` (`id_producto`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `ventas` (`id_venta`, `id_cliente`, `id_producto`, `fecha_venta`, `cantidad`, `total`) VALUES
(1,	1,	1,	'2023-04-15',	1,	800.00),
(2,	2,	2,	'2023-05-20',	2,	800.00),
(3,	3,	3,	'2023-06-25',	3,	60.00),
(4,	4,	4,	'2023-07-10',	1,	50.00),
(5,	1,	2,	'2023-08-12',	1,	400.00);