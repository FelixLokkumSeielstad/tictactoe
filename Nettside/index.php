<?php
require 'connect.php';

$stmt4 = $connect->prepare("SELECT review, rating FROM webrating ORDER BY rating DESC LIMIT 3");
$stmt4->execute();
$stmt4->bind_result($review, $rating);
$data = array();
while ($stmt4->fetch()) {
    $data[] = array(
        'review' => $review,
        'rating' => $rating
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
    <title>prøve e</title>
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


    <section class="homesite">
        <div class="homenoe">
            <div class="displaybox" id="box1">
                <div class="review-section">
                    <h2>Top Review</h2>
                    <?php if (!empty($data)): ?>
                        <?php foreach ($data as $review): ?>
                            <h3>Review Header</h3>
                            <div class="review-item">
                                <p>Review:
                                    <?php echo $review['review']; ?>
                                </p>
                                <p>Rating:
                                    <?php echo $review['rating']; ?>
                                </p>
                            </div>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </div>
            </div>
            <div class="displaybox" id="box2">
                <h1>Innhold</h1><br>
                <p>I Denne nettsiden kan du laste ned spill og gi dem en review.</p>

            </div>
        </div>

        <br><br>

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