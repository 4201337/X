<?php

//
$dbHost = 'localhost';
$dbName = 'z';
$dbUsername = 'root';
$dbPassword = '';
$dbCharset = 'utf8';
try {
	$db = new PDO("mysql:host=$dbHost;dbname=$dbName;charset=$dbCharset", $dbUsername, $dbPassword);
	$db->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	$db->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
	$db->setAttribute(PDO::ATTR_EMULATE_PREPARES, false);
} catch (PDOException $e) {
	die('Error: ' . $e->getMessage());
	die('...');
}
