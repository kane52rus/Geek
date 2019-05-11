<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Личный сайт студента GeekBrains</title>
	<link rel="stylesheet" href="style.css">
	<script type="text/javascript">
		var totalScore = 0;
		var firstRiddle = "Зимой и летом - одним цветом. Что это?";
		var firstRightAnswer = ["Елка","елка","Ель","ель","Елочка","елочка", "userAnswer1"];
		var secondRiddle = "Сто одежек, все без застежек. Что это?";
		var secondRightAnswer = ["Капуста","капуста"];
		var thirdRiddle = "Летом серый, зимой белый. Что это?";
		var thirdRightAnswer = ["Заяц","заяц","Зайчик","зайчик","Зайка","зайка"];
       	function riddles(answer, rightAnswer){
       			var userAnswer = document.getElementById(answer).value;
                var searchAnswer = rightAnswer.filter(function(item){return item == userAnswer;});
                if(userAnswer == searchAnswer) {
                    totalScore++;
                }
            }

		function checkAnswers() {
			riddles("userAnswer1", firstRightAnswer);
			riddles("userAnswer2", secondRightAnswer);
			riddles("userAnswer3", thirdRightAnswer);

			alert("Game Over\nВаш общий счет: " + totalScore);

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

					<h1>Игра в загадки</h1>
					<div class="box">


					<?php
                        if(isset($_GET['userAnswer1']) && isset($_GET['userAnswer2']) && isset($_GET['userAnswer3'])){
                            $userAnswer = $_GET["userAnswer1"];
                            $totalScore = 0;
                            if($userAnswer == "елка") {
                                $totalScore++;
                            }
                            $userAnswer = $_GET["userAnswer2"];
                            if($userAnswer == "капуста") {
                                $totalScore++;
                            }
                            $userAnswer = $_GET["userAnswer3"];
                            if($userAnswer == "заяц") {
                                $totalScore++;
                            }
                            echo "Вы угадали " . $totalScore . " загадок";
                        }
					?>
                        <form method="GET">
                            <p>Зимой и летом - одним цветом. Что это?</p>
                            <input type="text" name="userAnswer1">

                            <p>Сто одежек, все без застежек. Что это?</p>
                            <input type="text" name="userAnswer2">

                            <p>Летом серый, зимой белый. Что это?</p>
                            <input type="text" name="userAnswer3">
                            <br>
                            <input type="submit" value="Ответить" name="">
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