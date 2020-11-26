-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: localhost    Database: techshop
-- ------------------------------------------------------
-- Server version	8.0.18

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
-- Table structure for table `buyers`
--

DROP TABLE IF EXISTS `buyers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buyers` (
  `Name` varchar(50) DEFAULT NULL,
  `Email` varchar(100) NOT NULL,
  `Password` varchar(225) DEFAULT NULL,
  `Product_ID` int(11) DEFAULT NULL,
  `Units_Purchased` int(11) DEFAULT NULL,
  `Total` int(11) DEFAULT NULL,
  `Advance` int(11) DEFAULT NULL,
  `Due` int(11) GENERATED ALWAYS AS ((`Total` - `Advance`)) VIRTUAL,
  PRIMARY KEY (`Email`),
  KEY `Product_ID` (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buyers`
--

LOCK TABLES `buyers` WRITE;
/*!40000 ALTER TABLE `buyers` DISABLE KEYS */;
INSERT INTO `buyers` (`Name`, `Email`, `Password`, `Product_ID`, `Units_Purchased`, `Total`, `Advance`) VALUES ('Suhas Ghosh','15fri10@gmail.com','24@86',1,1,59990,10000),('Soham Pramanik','22042002soham@gmail.com','12*34',8,1,1999,1999),('Homodeep Maity','SME@gmail.com','86',4,1,43511,2879);
/*!40000 ALTER TABLE `buyers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `ID` int(11) NOT NULL,
  `Product_Name` varchar(225) DEFAULT NULL,
  `Stock` int(225) DEFAULT NULL,
  `Price_Per_Unit` int(225) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (0,'WD My Passport Go 1TB(External)',25,11999),(1,'Asus ROG Strix XG32VQ Curved Gaming Monitor 32 inch',48,59990),(2,'Samsung 970 PRO 1TB PCIe NVMe Internal SSD',36,27000),(3,'AMD Ryzen 7 3700X 4.4GHz 8/16 AM4 Socket 36MB Cache',50,29449),(4,'GALAX GeForce RTX Super 2070 8GB GDDR6 DP*3/HDMI',49,43511),(5,'GIGABYTE X570 UD Motherboard',36,15229),(6,'Ant Esports RGB Cabinet: ATX,Micro-ATX,Mini-ITX Mobos',21,2879),(7,'Thermaltake 850W Fully Modular Power Supply',21,11499),(8,'Cooler Master Devastator Gaming 3 Keyboard and Mouse Combo',21,1999),(9,'ASUS AREZ RX550-2G GDDR5 DP HDMI DVI',20,4974),(10,'Ant Esports H500 Stereo Gaming Over Ear Headphones with Mic',38,1149),(11,'Intel Core i3-9100F 4/4 LGA1151 300 Series',46,7094),(12,'Intel Core i5 9600K 6/6 Turbo Unlocked LGA1151',40,21490),(13,'MSI Z390-A PRO LGA1151 HDMI DP ATX Gaming Motherboard',47,12099),(14,'ASUS Prime H310M-E LGA1151(300 Series) HDMI VGA mATX Motherboard',47,4899),(15,'GIGABYTE B450M DS3H (AMD Ryzen AM4/M.2/HMDI/DVI/USB 3.1/DDR4/Micro ATX)',36,6875);
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-12 13:49:12
