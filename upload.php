<?php
$target_dir = "uploads/";
if (!file_exists($target_dir)) {
    mkdir($target_dir, 0777, true);
}

if ($_SERVER['REQUEST_METHOD'] === 'POST' && isset($_FILES['file'])) {
    $target_file = $target_dir . basename($_FILES["file"]["name"]);
    if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
        echo "File uploaded successfully: " . basename($_FILES["file"]["name"]);
    } else {
        echo "Sorry, there was an error uploading your file.";
    }
} else {
    echo "Send POST request with file field 'file'.";
}
?>
