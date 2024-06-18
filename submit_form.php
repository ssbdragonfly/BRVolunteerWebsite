<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = $_POST['name'];
    $email = $_POST['email'];
    $phone = $_POST['phone'];
    $message = $_POST['message'];

    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email format";
        exit;
    }

    $data = [
        'name' => $name,
        'email' => $email,
        'phone' => $phone,
        'message' => $message
    ];

    file_put_contents('form_data.json', json_encode($data));
    exec('python3 send_email.py');
    
    echo "Thank you! Sent!";
} else {
    echo "Method not allowed.";
}
?>
