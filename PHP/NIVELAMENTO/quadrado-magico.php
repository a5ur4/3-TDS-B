<!DOCTYPE html>
<html>
<head>
	<title>Soma da Matriz Mágica</title>
</head>
<body>
	<h1>Soma da Matriz Mágica</h1>
	<form method="POST" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">
		<label for="n">Tamanho da matriz:</label>
		<input type="number" id="n" name="n" min="1" max="10" required><br><br>
		<label for="matriz">Valores da matriz:</label>
		<textarea id="matriz" name="matriz" rows="10" cols="30" required></textarea><br><br>
		<input type="submit" value="Calcular">
	</form>
	<?php
	if ($_SERVER["REQUEST_METHOD"] == "POST") {
		// Leitura da entrada
		$n = intval($_POST["n"]);
		$matriz = array();
		$linhas = explode("\n", $_POST["matriz"]);
		foreach ($linhas as $linha) {
			$matriz[] = array_map('intval', explode(' ', $linha));
		}

		// Soma da primeira linha
		$soma = array_sum($matriz[0]);

		// Verificação das linhas
		for ($i = 0; $i < $n; $i++) {
			if (array_sum($matriz[$i]) != $soma) {
				$soma = 0;
				break;
			}
		}

		// Verificação das colunas
		if ($soma != 0) {
			for ($j = 0; $j < $n; $j++) {
				$coluna = 0;
				for ($i = 0; $i < $n; $i++) {
					$coluna += $matriz[$i][$j];
				}
				if ($coluna != $soma) {
					$soma = 0;
					break;
				}
			}
		}

		// Verificação das diagonais
		if ($soma != 0) {
			$diagonal1 = 0;
			$diagonal2 = 0;
			for ($i = 0; $i < $n; $i++) {
				$diagonal1 += $matriz[$i][$i];
				$diagonal2 += $matriz[$i][$n - $i - 1];
			}
			if ($diagonal1 != $soma || $diagonal2 != $soma) {
				$soma = 0;
			}
		}

		// Exibição do resultado
		if ($soma != 0) {
			echo "<p>A soma da matriz é $soma.</p>";
		} else {
			echo "<p>A matriz não é mágica.</p>";
		}
	}
	?>
</body>
</html>
