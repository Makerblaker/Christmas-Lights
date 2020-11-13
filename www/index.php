<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
	  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <script src="js/jquery-3.3.1.min.js"></script>
    <script src="js/popper.min.js"></script>
    <script src="js/bootstrap.min.js"></script>
    <title>Christmas Lights</title>
 </head>
 <body>
  <?php
  if(isset($_GET["relay"]))
  {
    if($_GET["relay"] == "PROGRAM")
    {
      switch ($_GET["status"])
      {
        case "ON":
          exec("python3 /home/pi/Projects/Christmas-Lights/on.py 2>&1");
          ?>
          <div class="alert alert-success" role="alert">
            Default Program Started!
          </div>
          <?php

        break;
        case "OFF":
          exec("python3 /home/pi/Projects/Christmas-Lights/off.py 2>&1");
          ?>
          <div class="alert alert-warning" role="alert">
            Default Program Stopped!
          </div>
          <?php
        break;
      }
    } elseif (is_numeric($_GET["relay"])) {
      switch ($_GET["status"])
      {
        case "ON":
          exec("python3 /home/pi/Projects/Christmas-Lights/relay.py ".$_GET["relay"]." ON 2>&1");
          ?>
          <div class="alert alert-success" role="alert">
            Relay <?php echo $_GET["relay"]; ?> ON.
          </div>
          <?php
        break;
        case "OFF":
          exec("python3 /home/pi/Projects/Christmas-Lights/relay.py ".$_GET["relay"]." OFF 2>&1");
          
          ?>
          <div class="alert alert-warning" role="alert">
            Relay <?php echo $_GET["relay"]; ?> OFF.
          </div>
          <?php
        break;
      }
    }
  }
  ?>
    <!-- Expanding nav bar -->
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <a class="navbar-brand" href="#">
        Christmas Lights
      </a>
    </nav>
    <!-- End of nav bar -->
    <!-- Main Content -->
    <div class="container">
      <div class="row">
        <div class="col-sm">
        <table class="table">
        <?php

        $relays = array(0, 1, 2, 3);
        echo "<tbody>";
        echo "<tr>";
        echo "<td>Program</td>";
        echo "<td><a href=\"index.php?relay=PROGRAM&status=ON\">ON</a>";
        echo "<td><a href=\"index.php?relay=PROGRAM&status=OFF\">OFF</a>";
        echo "</tr>";

        foreach($relays as $relay)
        {
          echo "<tr>";
          echo "<td>Relay ".$relay."</td>";
          echo "<td><a href=\"index.php?relay=".$relay."&status=ON\">ON</a>";
          echo "<td><a href=\"index.php?relay=".$relay."&status=OFF\">OFF</a>";
          echo "</tr>";
        }
        echo "</tbody>"

        ?>
        </div>
      </div>      
    </div>
    <!-- End of Main Content -->
  </body>
</html>
