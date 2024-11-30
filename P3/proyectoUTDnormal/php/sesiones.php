<?php
session_start();

// Verificar si el usuario está logueado
if (!isset($_SESSION['user'])) {
    header("Location: index.php");
    exit();
}

// Verificar si la ruta es válida (si la página existe físicamente)
$ruta = $_GET['pagina'] ?? '';

// Si la ruta está vacía, se carga la página principal (index.php)
if ($ruta == '') {
    include '../index.php';
    exit();
}

// Verificar si el archivo solicitado existe en el servidor
$archivo = $ruta . '.php';

// Si el archivo no existe, redirigir a index.php
if (!file_exists($archivo)) {
    header("Location: ../index.php");
    exit();
}

// Si el archivo existe, incluirlo
include $archivo;
?>
