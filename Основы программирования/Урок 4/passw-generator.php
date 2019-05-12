<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css">
	<script type="text/javascript">

		function readInt(){
				return +document.getElementById("userAnswer").value;
			}

		function generatePassword() {
    		var length = readInt();
       		var alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
        	var genPassword = "";
        	if(length < 4 || length > 25){
        	    document.getElementById("passwords").innerHTML = "Ваш пароль не соответствует требованиям. Необходимо от 4 до 25 символов";
        	} else {
   			    for (var i = 0, n = alphabet.length; i < length; ++i) {
        		    genPassword += alphabet.charAt(Math.floor(Math.random() * n));
    		    }
    		document.getElementById("passwords").innerHTML = genPassword;
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

					<h1>Генератор паролей</h1>
					<div class="box">


						<form method="GET">

						   	<p>Введите длину желаемого пароля. Минимальная длина пароля - 4 символа, максимальная - 25</p>
							<p id="passwords"></p>
                           	<input type="text" id="userAnswer"><br>
							<a href="#" onclick="generatePassword()">Генерировать</a>
						</form>
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