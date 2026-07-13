<?php
/* Code Viewer Challenge */
/* Access with ?source=1 to view source code */
if (isset($_GET['source'])) {
    highlight_file(__FILE__);
    die();
}
?>
<!DOCTYPE html>
<html>
<head><title>Code Viewer</title></head>
<body>
<h1>Welcome to Code Viewer</h1>
<p>View source code by adding <code>?source=1</code> to the URL.</p>
<?php
// FLAG is hidden in the source code comments
// [REDACTED]
?>
</body>
</html>