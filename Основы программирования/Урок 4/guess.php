<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css">
	<script type="text/javascript">
			var answer = parseInt(Math.random() * 100);
			var tryCount = 0;
			var maxTryCount = 3;

			function readInt(){
				return +document.getElementById("userAnswer").value;
			}
			function write(text) {
				document.getElementById("info").innerHTML = text;
			}
			function hide(id) {
				document.getElementById(id).style.display = "none";
			}


			function guess() {
					tryCount++
					var userAnswer = readInt();
					if(userAnswer == answer) {
						write("You win");
						hide("button");
						hide("userAnswer");
					} else if(tryCount >= maxTryCount) {
						write("You lost. Right answer: " + answer);
						hide("button");
						hide("userAnswer");
					} else if(userAnswer > answer) {
						write("More, than need. ");
					} else if(userAnswer < answer) {
						write("Lower, than need");
					}
			}

	</script>
</head>
<body>
	<div class="content">
		<?php
	    include "menu.php";
		?>

		<div class="contentWrap">
			<div class="content">
				<div class="center">

					<h1>Игра угадайка</h1>
					<div class="box">
						<p id="info">Угадайте число от 0 до 100</p>
						<input type="text" id="userAnswer"><br>
						<a href="#" onclick="guess();" id="button">Начать</a>

					</div>

				</div>
			</div>
		</div>
	</div>

<div class="footer">
	Copyright &copy; Andrey Tabunkin
</div>


</body>
</html>