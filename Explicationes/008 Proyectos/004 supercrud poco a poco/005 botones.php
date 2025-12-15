<nav>
    <a href="?tabla=cliente">cliente</a>
    <a href="?tabla=producto">producto</a>
    <a href="?tabla=pedido">pedido</a>
    <a href="?tabla=lineaspedido">lineaspedido</a>
</nav>
<main>
    <table>
    <?php
        $host = "localhost";
    $user = "tiendaonlinedamdaw";
    $pass = "Tiendaonlinedamdaw123$";
    $db   = "tiendaonlinedamdaw";

    $conexion = new mysqli($host, $user, $pass, $db);
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