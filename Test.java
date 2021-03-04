//package tmp;

import java.sql.*;
public class Test
{
public static void main(String[] args) throws Exception
{
Connection con;
Statement stat;
Class.forName("com.mysql.jdbc.Driver");//Step 1: Loading Drivers

//con=DriverManager.getConnection("jdbc:mysql://192.168.245.160:3306/ip2location","debu","password");//Step 2: Making Connection

con=DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/ip2location?useUnicode=true&useJDBCCompliantTimezoneShift=true&useLegacyDatetimeCode=false&serverTimezone=UTC","debu","password");//Step 2: Making Connection


stat=con.createStatement();//Step 3: Creating JDBC Statement

String query = "select * from ip2location_db9 limit 10;";

ResultSet rset=stat.executeQuery(query);//Step 4: Execute the Ststement

while(rset.next())//Step 5: Looping through the ResultSet
{
    System.out.println(rset.getString(1));
}
stat.close();//step 6: Close the Connection and Statement
con.close();
}
}