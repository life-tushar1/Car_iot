 <!doctype html>
    
 <?php
      $username = "root";
      $password = "";
      $host = "localhost";
      $db = "parking";

      $connect = new mysqli($host,$username,$password,$db);
          if($connect->connect_error)
            {
            die("connection failed");
            }
            else{
            echo "Connections are made successfully::";
            

      //execute the SQL query and return records
      $sql="SELECT SUM(taken) AS value_sum FROM par";
      $result = $connect->query($sql);
 
         $row = mysqli_fetch_assoc($result); 
            $sum = $row['value_sum'];
            }
         
        
     
        mysqli_close($connect); ?>
        
        
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>database connections</title>
    </head>
    <body>

    <h1 class="wrapper" align="center">Smart Car</h1>
    <h1 class="wrapper" align="center"> Parking Lot</h1>
      <table border="2" style= "background-color: #84ed86; color: #761a9b; margin: 0 auto;" >
      <thead>
        <tr>
          <th>Taken Parking</th>
          <th>Total Parking</th>

        </tr>
      </thead>
      <tbody>
        
        
            <tr>
              <td><?php echo $sum; ?></td>
              <td>8</td>

            </tr>
         
      </tbody>
    </table>
  
    </body>
    </html>