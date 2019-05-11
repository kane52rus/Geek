<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css">
	<script type="text/javascript">
			var answer = parseInt(Math.random() * 100);


			function readInt(player){
				if(player == 1) {
					return document.getElementById("userAnswer1").value;
				} else if(player == 2) {
					return document.getElementById("userAnswer2").value;
				}
			}
			function write(player, text) {
				if(player == 1) {
					document.getElementById("info1").innerHTML = text;
				} else if(player == 2){
					document.getElementById("info2").innerHTML = text;

				}

			}
			function hide(id) {
				document.getElementById(id).style.display = "none";
			}

			function guess(player) {
						var userAnswer = readInt(player);
						if(userAnswer == answer) {
							write(player, "Игрок - You win");
							hide("button");
							hide("userAnswer" + player);
						} else if(userAnswer == "GG") {
							write(player, "Игрок " + player + " вышел. Правильный ответ: " + answer);
							hide("button");
							hide("userAnswer1");
							hide("userAnswer2");
						} else if(userAnswer > answer) {
							write(player,"Игрок " + player + ", больше, чем нужно ");
						} else if(userAnswer < answer) {
							write(player,"Игрок " + player + ", меньше, чем нужно ");
						}
					return player;
			}
			function multi() {
				var players = 2;

				for(var i = 1; i <= players; i++){
					if(i < players) {
						guess(i);
					} else if(i == players){
						guess(i);
					} else {

					alert("error");
					}
				}
			}

	</script>
</head>
<body>
	<div class="content">

		<div class="contentWrap">
			<div class="content">
				<div class="center">

					<h1>Игра угадайка</h1>
					<div class="box">
						<h3>Угадайте число от 0 до 100</h3>
						<p id="info1">Игрок 1</p>
						<input type="text" id="userAnswer1"><br>
						<br><br><br>
						<p id="info2">Игрок 2</p>
						<input type="text" id="userAnswer2"><br>
						<a href="#" onclick="multi();" id="button">Начать</a>

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