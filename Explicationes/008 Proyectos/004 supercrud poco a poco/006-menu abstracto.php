<?php

    $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db   = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);

?>

<nav>
<?php
    $resultado = $conexion->query("
        SHOW TABLES;
    ");
    while ($fila= $resultado->fetch_assoc()){
        echo '<a href="?tabla='.$fila['Tables_in_'.$db].'">'.$fila['Tables_in_'.$db].'</a>';
    }


    


?>
</nav>
<main>
  <table>
  <?php

    $resultado = $conexion->query("
      SELECT * FROM ".$_GET['tabla'].";
    ");
    while ($fila = $resultado->fetch_assoc()) {
      echo "<tr>";
      foreach($fila as $clave=>$valor){
        echo "<td>".$valor."</td>";
      }
      echo "</tr>";
     }
  ?>
  </table>
</main>