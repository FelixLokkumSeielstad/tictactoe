<?php
require 'connect.php';

$showscore = $connect->prepare("SELECT score, name  FROM gamepoints ORDER BY score DESC LIMIT 5");
$showscore->execute();
$showscore->bind_result($score, $name);
$data = array();
while ($showscore->fetch()) {
    $data[] = array(
        'score' => $score,
        'name' => $name,
    );
}

$connect->close();
?>


<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="Style.css">
    <title>Document</title>
</head>

<body>

    <nav class="nav">
        <ul class="nav-links">
            <li><a href="index.php" id="activenav">Home</a></li>
            <li><a href="About.php">About</a></li>
            <li><a href="Download.php">Download</a></li>
            <li><a href="faq.php">FAQ</a></li>
            <li><a href="Login.php">Log in</a></li>
        </ul>
        <div class="burger">
            <div class="line1"></div>
            <div class="line2"></div>
            <div class="line3"></div>
        </div>
    </nav>


    <section class="score">
        <div class="displaybox1">
            <div class="review-section">
                <h2>Top high score</h2>
                <?php if (!empty($data)): ?>
                    <?php foreach ($data as $score): ?>
                        <h3>Review Header</h3>
                        <div class="review-item">
                            <p>name:
                                <?php echo $score['name']; ?>
                            </p>
                            <p>score:
                                <?php echo $score['score']; ?>
                            </p>
                        </div>
                    <?php endforeach; ?>
                <?php endif; ?>
            </div>
        </div>

        <footer>
            <div class="footer-content">
                <div class="footer-section">
                    <h2>Contact Us</h2>
                    <ul>
                        <li>Email: falsk@email.com</li>
                        <li>Phone: +47 123-456-7890</li>
                    </ul>
                    <div class="footer-bottom">
                        <p>&copy; 2023 My Website. All rights reserved.</p>
                    </div>
                </div>
            
            </div>
        </footer>
    </section>

    <script src="script.js"></script>

</body>

</html>