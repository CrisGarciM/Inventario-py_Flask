-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 28-09-2023 a las 23:00:32
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `inventario`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipo`
--

CREATE TABLE `equipo` (
  `ID_Equipo` int(11) NOT NULL,
  `N_Equipo` varchar(20) NOT NULL,
  `Equipo_Serial` varchar(20) NOT NULL,
  `Equipo_Marca` varchar(20) NOT NULL,
  `Equipo_Ram` varchar(50) NOT NULL,
  `Equipo_Procesador` varchar(30) NOT NULL,
  `Equipo_Disco` varchar(50) NOT NULL,
  `Equipo_FechaRegis` date NOT NULL,
  `Equipo_Estado` varchar(15) NOT NULL,
  `Equipo_Grafica` varchar(15) DEFAULT NULL,
  `Equipo_Descripcion` varchar(30) DEFAULT NULL,
  `Equipo_Ubicacion` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `correo` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `login`
--

INSERT INTO `login` (`id`, `correo`, `password`) VALUES
(1, 'inventario@iumafis.com', '123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `otros`
--

CREATE TABLE `otros` (
  `ID_Otros` int(11) NOT NULL,
  `Otros_Tipo` varchar(20) NOT NULL,
  `Otros_Serial` varchar(20) NOT NULL,
  `Otros_Marca` varchar(20) NOT NULL,
  `Otros_Descripcion` varchar(30) DEFAULT NULL,
  `Otros_Ubicacion` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pantalla`
--

CREATE TABLE `pantalla` (
  `ID_Pantalla` int(11) NOT NULL,
  `N_Equipo` varchar(20) NOT NULL,
  `Pantalla_Serial` varchar(20) NOT NULL,
  `Pantalla_Marca` varchar(20) NOT NULL,
  `Pantalla_Pulgadas` varchar(15) NOT NULL,
  `Pantalla_Resolucion` varchar(20) NOT NULL,
  `Pantalla_Estado` varchar(15) NOT NULL,
  `Pantalla_Descripcion` varchar(30) DEFAULT NULL,
  `Pantalla_Ubicacion` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `perifericos`
--

CREATE TABLE `perifericos` (
  `ID_Periferico` int(11) NOT NULL,
  `N_Equipo` varchar(20) NOT NULL,
  `Mouse_Serial` varchar(20) NOT NULL,
  `Mouse_Marca` varchar(20) NOT NULL,
  `Mouse_Estado` varchar(15) NOT NULL,
  `Mouse_Descripcion` varchar(30) DEFAULT NULL,
  `Teclado_Serial` varchar(20) NOT NULL,
  `Teclado_Marca` varchar(20) NOT NULL,
  `Teclado_Estado` varchar(15) NOT NULL,
  `Teclado_Descripcion` varchar(30) DEFAULT NULL,
  `Peri_Ubicacion` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipo`
--
ALTER TABLE `equipo`
  ADD PRIMARY KEY (`ID_Equipo`);

--
-- Indices de la tabla `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `otros`
--
ALTER TABLE `otros`
  ADD PRIMARY KEY (`ID_Otros`);

--
-- Indices de la tabla `pantalla`
--
ALTER TABLE `pantalla`
  ADD PRIMARY KEY (`ID_Pantalla`);

--
-- Indices de la tabla `perifericos`
--
ALTER TABLE `perifericos`
  ADD PRIMARY KEY (`ID_Periferico`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipo`
--
ALTER TABLE `equipo`
  MODIFY `ID_Equipo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `otros`
--
ALTER TABLE `otros`
  MODIFY `ID_Otros` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `pantalla`
--
ALTER TABLE `pantalla`
  MODIFY `ID_Pantalla` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `perifericos`
--
ALTER TABLE `perifericos`
  MODIFY `ID_Periferico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
