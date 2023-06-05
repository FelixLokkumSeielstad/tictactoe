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
        <div class="logo">
            <h4>The Nav</h4>
        </div>
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


    <section class="Download">

        <table class="downloadapps">
            <tr class="tableborder">
                <th>Type</th>
                <th>Reviews</th>
                <th>Version</th>
                <th>Download</th>
            </tr>
            <tr class="tableborder">
                <th>Website</th>
                <th></th>
                <th>Header 6</th>
                <th><a href="zipfiles/Nettsidezip.zip" download>Download Folder</a></th>
            </tr>
            <tr class="tableborder">
                <th>Game</th>
                <th></th>
                <th>1.0</th>
                <th><a href="zipfiles/tictactoezip.zip" download>Download Folder</a></th>
            </tr>
        </table>


        <div class="Reviewdivspit">
            <h1>Reviews</h1>
            <h2>Give a review on the game</h2>
            <form class="homeform" action="redirectpage.php" method="POST">
                <label for="selectOption">Select an option:</label>
                <input id="reviewinput" type="text" name="reviewinput" oninput="reviewcount()" maxlength="100"
                    placeholder="Write a review">
                <p id="wordCount">0/100</p>
                <select name="selectOption" id="selectOption">
                    <option value="1">1 star</option>
                    <option value="2">2 star</option>
                    <option value="3">3 star</option>
                    <option value="4">4 star</option>
                    <option value="5">5 star</option>
                </select>
                <button type="submit">Submit</button>
            </form>
        </div>
    </section>



    <script src="script.js"></script>
</body>

</html>