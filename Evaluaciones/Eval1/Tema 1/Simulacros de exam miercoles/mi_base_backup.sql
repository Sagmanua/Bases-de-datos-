-- MySQL dump 10.13  Distrib 8.0.43, for Linux (x86_64)
--
-- Host: localhost    Database: portafolio
-- ------------------------------------------------------
-- Server version	8.0.43-0ubuntu0.24.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Temporary view structure for view `CatPIEz`
--

DROP TABLE IF EXISTS `CatPIEz`;
/*!50001 DROP VIEW IF EXISTS `CatPIEz`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `CatPIEz` AS SELECT 
 1 AS `id_pieza`,
 1 AS `titulo_p`,
 1 AS `descripcion_p`,
 1 AS `imagen`,
 1 AS `url`,
 1 AS `titilo_categoria`,
 1 AS `descripcion_categoria`*/;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `Categoria`
--

DROP TABLE IF EXISTS `Categoria`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Categoria` (
  `Id_cat` int NOT NULL,
  `titulo_c` varchar(255) DEFAULT NULL,
  `descripcion_c` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id_cat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Categoria`
--

LOCK TABLES `Categoria` WRITE;
/*!40000 ALTER TABLE `Categoria` DISABLE KEYS */;
INSERT INTO `Categoria` VALUES (1,'Escultura','Obras hechas en piedra, metal o madera'),(2,'Pintura','Cuadros en óleo o acrílico');
/*!40000 ALTER TABLE `Categoria` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pieza`
--

DROP TABLE IF EXISTS `Pieza`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `Pieza` (
  `id_pieza` int NOT NULL,
  `titulo_p` varchar(255) DEFAULT NULL,
  `descripcion_p` varchar(255) DEFAULT NULL,
  `imagen` varchar(255) DEFAULT NULL,
  `url` varchar(255) DEFAULT NULL,
  `id_categoria` int DEFAULT NULL,
  PRIMARY KEY (`id_pieza`),
  KEY `FK_catogaria` (`id_categoria`),
  CONSTRAINT `FK_catogaria` FOREIGN KEY (`id_categoria`) REFERENCES `Categoria` (`Id_cat`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pieza`
--

LOCK TABLES `Pieza` WRITE;
/*!40000 ALTER TABLE `Pieza` DISABLE KEYS */;
INSERT INTO `Pieza` VALUES (1,'El Pensador','Escultura de Rodin','pensador.jpg','http://ejemplo.com/pensador',1),(2,'La Noche Estrellada','Pintura de Van Gogh','noche.jpg','http://ejemplo.com/noche',2);
/*!40000 ALTER TABLE `Pieza` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `CatPIEz`
--

/*!50001 DROP VIEW IF EXISTS `CatPIEz`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8mb4 */;
/*!50001 SET character_set_results     = utf8mb4 */;
/*!50001 SET collation_connection      = utf8mb4_0900_ai_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `CatPIEz` AS select `p`.`id_pieza` AS `id_pieza`,`p`.`titulo_p` AS `titulo_p`,`p`.`descripcion_p` AS `descripcion_p`,`p`.`imagen` AS `imagen`,`p`.`url` AS `url`,`c`.`titulo_c` AS `titilo_categoria`,`c`.`descripcion_c` AS `descripcion_categoria` from (`Pieza` `p` left join `Categoria` `c` on((`p`.`id_categoria` = `c`.`Id_cat`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-05  9:42:01
