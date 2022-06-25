<?
$fio = $_REQUEST['fio'];
$message = $_REQUEST['message'];

header("Content-type: text/html; charset=utf-8");

echo "<p>$fio";
echo "<p>$message";
?>