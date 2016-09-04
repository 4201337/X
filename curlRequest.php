<?php

function curlRequest($url)
{
	$ch = curl_init($url);
	$options = [
		CURLOPT_CUSTOMREQUEST  => 'POST',
		CURLOPT_POST           => true,
		CURLOPT_USERAGENT      => 'Mozilla/5.0 (Windows NT 6.1; rv:8.0) Gecko/20100101 Firefox/8.0',
		CURLOPT_COOKIEFILE     => 'Cookie.txt',
		CURLOPT_COOKIEJAR      => 'Cookie.txt',
		CURLOPT_COOKIESESSION  => true,
		CURLOPT_RETURNTRANSFER => true,
		CURLOPT_HEADER         => false,
		CURLOPT_FOLLOWLOCATION => true,
		CURLOPT_ENCODING       => '',
		CURLOPT_AUTOREFERER    => true,
		CURLOPT_CONNECTTIMEOUT => 120,
		CURLOPT_TIMEOUT        => 120,
		CURLOPT_MAXREDIRS      => 10,
		CURLOPT_SSL_VERIFYPEER => false,
		CURLOPT_SSL_VERIFYHOST => false
	];
	curl_setopt_array($ch, $options);
	$return = [];
	$return['content'] = curl_exec($ch);
	$return['status'] = curl_errno($ch);
	$return['error'] = curl_error($ch);
	$return['information'] = curl_getinfo($ch);
	curl_close( $ch );
	return $return;
}
