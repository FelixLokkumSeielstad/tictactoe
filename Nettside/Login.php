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

    <!--Her er manyen-->
    <nav class="nav">
        <!-- Liste over navigasjonslenker -->
        <ul class="nav-links">
            <li><a href="index.php" id="activenav">Home</a></li>
            <li><a href="About.php">About</a></li>
            <li><a href="Download.php">Download</a></li>
            <li><a href="faq.php">FAQ</a></li>
            <li><a href="Login.php">Log in</a></li>
        </ul>
        <!-- "Burger"-ikon for mobilvisning -->
        <div class="burger">
            <div class="line1"></div>
            <div class="line2"></div>
            <div class="line3"></div>
        </div>
    </nav>

    <!--Her starter loginsiden-->
    <section class="Login">

        <div class="loginstyle">
            <!--Her er formen som snakker med redirectpage-->
            <form action="redirectpage.php" method="post">
                <label for="username">Username:</label><br>
                <input id="username" type="text" name="username" required>
                <br>
                <label for="password">Password:</label><br>
                <input id="password" type="password" name="password" required>
                <br>
                <div id="epostplacemen"></div>
                <input id="loginbutton" type="submit" value="Login">
            </form><br>
            <!--her er knappen som sender informaskjonen til redirectpage-->
            <button onclick="changeloginsite()">Oppret bruker</button>
        </div>

    </section>

    <script src="script.js"></script>
</body>

</html>
