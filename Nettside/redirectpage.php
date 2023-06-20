<?php
require 'connect.php';

//Denne if statmenten sjekker om bruker er info er puttet in.
if (isset($_POST['makeusername']) && isset($_POST['makepassword']) && isset($_POST['makeepost'])) {
    //lager variabler får å putte informaskjonen in i databasen
    $usernameInput = $_POST['makeusername'];
    $passwordInput = password_hash($_POST['makepassword'], PASSWORD_DEFAULT);
    $epostInput = $_POST['makeepost'];

    // Setter verdiene inn i databasen og endrer dem senere for å hindre SQL-injeksjoner.
    $lagbruker = $connect->prepare("INSERT INTO login (name, password, epost) VALUES (?, ?, ?)");
    $lagbruker->bind_param("sss", $usernameInput, $passwordInput, $epostInput);

    // her utfører jeg coden over
    if ($lagbruker->execute()) {
        echo "Data inserted successfully.";
    } else {
        echo "Error: " . $lagbruker->error;
    }
}

// i denne if statmenten bruker jeg 
if (isset($_POST['username']) && isset($_POST['password'])) {
    $usernameOutput = $_POST['username'];
    $passwordOutput = $_POST['password'];

    // Oppretter SQL-spørringen ved hjelp av prepared statement.
    $loggerinbruker = $connect->prepare("SELECT * FROM login WHERE name = ?");
    $loggerinbruker->bind_param("s", $usernameOutput);

    //her utfører jeg koden over 
    $loggerinbruker->execute();
    $result = $loggerinbruker->get_result();

    //her henter jeg passordet fra databsen og sjekker om det et i databasen
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $hashedPassword = $row['password'];

        // hvis bruker er riktig eller feil
        if (password_verify($passwordOutput, $hashedPassword)) {
            echo "Du har logget in";
        } else {
            echo "ugyldig Brukernavn Eller passord";
        }
    } else {
        echo "ugyldig Brukernavn Eller passord";
    }
}

////////////////////////////////////////////////////////

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['reviewinput'])) {
    // Retrieve the selected option from the form
    $selectedOption = $_POST['selectOption'];
    $reviewinput = $_POST['reviewinput'];

    // Oppretter SQL-spørringen ved hjelp av prepared statement.
    $lagreview = $connect->prepare("INSERT INTO webrating (review, rating) VALUES (?, ?)");
    $lagreview->bind_param("ss", $reviewinput, $selectedOption);

    //kjører lagreview variabelen
    $lagreview->execute();
}



// stenger alle tilkoblingene
$lagbruker->close();
$loggerinbruker->close();
$lagreview->close();
$connect->close();

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
?>
