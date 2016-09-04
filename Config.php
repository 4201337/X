<?php

//
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
date_default_timezone_set('Asia/Riyadh');

//
$myLog = [
	'date' => date('d/m/Y H:i A'),
	'jDate' => date('d/m/Y'),
	'jTime' => date('H:i'),
	'jPeriod' => date('A'),
	'visitorIP' => isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : 'None',
	'visitorCountry' => isset($_SERVER['REMOTE_COUNTRY']) ? $_SERVER['REMOTE_COUNTRY'] : 'None',
	'visitorUserAgent' => isset($_SERVER['HTTP_USER_AGENT']) ? $_SERVER['HTTP_USER_AGENT'] : 'None',
	'visitorReferer' => isset($_SERVER['HTTP_REFERER']) ? $_SERVER['HTTP_REFERER'] : 'None'
];
