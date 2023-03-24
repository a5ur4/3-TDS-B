<!DOCTYPE html>
<html>
<head>
	<title>Verificar se é possível colocar duas fotos na página</title>
</head>
<body>
	<h1>Verificar se é possível colocar duas fotos na página</h1>
	<form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
		<label for="pageWidth">Largura da página:</label>
		<input type="number" id="pageWidth" name="pageWidth" required><br>
		<label for="pageHeight">Altura da página:</label>
		<input type="number" id="pageHeight" name="pageHeight" required><br>
		<label for="photoWidth">Largura da foto:</label>
		<input type="number" id="photoWidth" name="photoWidth" required><br>
		<label for="photoHeight">Altura da foto:</label>
		<input type="number" id="photoHeight" name="photoHeight" required><br>
		<input type="submit" value="Verificar">
	</form>

	<?php
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		// Recebe os valores de entrada
		$pageWidth = intval($_POST["pageWidth"]);
		$pageHeight = intval($_POST["pageHeight"]);
		$photoWidth = intval($_POST["photoWidth"]);
		$photoHeight = intval($_POST["photoHeight"]);

		// Verifica se é possível colocar as duas fotos na página
		if (($photoWidth + $photoHeight <= $pageWidth && max($photoWidth, $photoHeight) <= $pageHeight) || 
		    ($photoWidth + $photoHeight <= $pageHeight && max($photoWidth, $photoHeight) <= $pageWidth)) {
		    echo "<p>É possível colocar as duas fotos na página.</p>"; // Exibe mensagem de sucesso
		} else {
		    echo "<p>Não é possível colocar as duas fotos na página.</p>"; // Exibe mensagem de erro
		}
	}
	?>
</body>
</html>
