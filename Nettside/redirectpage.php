<?php
require 'connect.php';

if (isset($_POST['makeusername']) && isset($_POST['makepassword']) && isset($_POST['makeepost'])) {
    $usernameInput = $_POST['makeusername'];
    $passwordInput = password_hash($_POST['makepassword'], PASSWORD_DEFAULT);
    $epostInput = $_POST['makeepost'];

    // Create the SQL insert statement using prepared statement
    $stmt1 = $connect->prepare("INSERT INTO login (name, password, epost) VALUES (?, ?, ?)");
    $stmt1->bind_param("sss", $usernameInput, $passwordInput, $epostInput);

    // Execute the insert statement
    if ($stmt1->execute()) {
        echo "Data inserted successfully.";
    } else {
        echo "Error: " . $stmt1->error;
    }
}

if (isset($_POST['username']) && isset($_POST['password'])) {
    $usernameOutput = $_POST['username'];
    $passwordOutput = $_POST['password'];

    // Create the SQL select statement using prepared statement
    $stmt2 = $connect->prepare("SELECT * FROM login WHERE name = ?");
    $stmt2->bind_param("s", $usernameOutput);

    $stmt2->execute();
    $result = $stmt2->get_result();

    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $hashedPassword = $row['password'];

        if (password_verify($passwordOutput, $hashedPassword)) {
            // Username and password combination is correct
            echo "Login successful.";
        } else {
            // Invalid password
            echo "Invalid username or password.";
        }
    } else {
        // Username not found
        echo "Invalid username or password.";
    }
}

////////////////////////////////////////////////////////

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_POST['reviewinput'])) {
    // Retrieve the selected option from the form
    $selectedOption = $_POST['selectOption'];
    $reviewinput = $_POST['reviewinput'];

    $stmt3 = $connect->prepare("INSERT INTO webrating (review, rating) VALUES (?, ?)");
    $stmt3->bind_param("ss", $reviewinput, $selectedOption);

    // Execute the insert statement
    if ($stmt3->execute()) {
        echo "Data inserted successfully.";
    } else {
        echo "Error: " . $stmt3->error;
    }
}



// Close the prepared statements
$stmt1->close();
$stmt2->close();
$stmt3->close();
$stmt4->close();

// Close the database connection
$connect->close();

ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
?>