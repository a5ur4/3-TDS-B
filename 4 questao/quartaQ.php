<?php
$pesquisa = $_POST["q"];

header("Location: https://www.google.com/search?q=".$pesquisa.'');
?>