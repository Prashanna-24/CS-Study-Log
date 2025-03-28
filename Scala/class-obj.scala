// 1.Companion Object for Factory Pattern 
// oCreate a Person class with name and age attributes.
// oUse a companion object with a apply() method that: 
// Accepts a string in the format name,age.
// Splits the string and returns a Person instance.
// Write a test case where you create multiple Person objects using both new and apply() methods.

class Person(name: String, age: Int){
   def show(): Unit = {
      println(s"Name: $name Age: $age")
   }
}
object Person{
   def apply(info: String): Person = {
      val x = info.split(",")
      new Person(x(0).trim, x(1).trim.toInt)
   } 
}

object Main {
   def main(args: Array[String]): Unit = {
      val person1 = new Person("name1",11)
      person1.show()
      val person2 = Person("name2,22")
      person2.show()
   }
}


// 2. Temperature Converter using Singleton
import scala.io.StdIn._

object TemperatureConverter{
   def celsiusToFaren(c: Double): Double = (9.0/5)*c + 32
   def farenToCelsius(f:Double): Double = (f-32)*5.0/9
}


object Main{
   def main(args: Array[String]): Unit = {
      println("1. Celsius to Fahrenheit")
      println("2. Fahrenheit to Celsius")
      var flag = true
      while(flag){
         
         println("Choose an option:")
         var choice = readInt()
         choice match{
         case 1 =>
            val celsius = readDouble()
            val fahrenheit = TemperatureConverter.celsiusToFaren(celsius)
            println(f"celsuis: $celsius -> faren: $fahrenheit%.2f")
         case 2 =>
            val faren = readDouble()
            val cels = TemperatureConverter.farenToCelsius(faren)
            println(f"faren: $faren -> celsuis: $cels%.2f")
            
         case 3 =>
            println("exiting")
            flag = false
         case _ =>
            println("invalid")
         }
         
      }
      
      
   }
}


object InventoryManager{
  private var stock: Map[String, Int] = Map()
  
  def addStock(product: String, count: Int):Unit = {
    stock += product -> (stock.getOrElse(product, 0)+count)
    println("added!!")
  }
  def removeStock(product: String, count: Int):Boolean = {
    if (stock.getOrElse(product, 0)<count){
      println("LOW!!")
      false
    } else{
      stock += product -> (stock(product)-count)
      println("removed!!")
      true
    }
  }
  def viewstock():Unit = {
    for ((k,v) <- stock){
      println(k,v)
    }
  }
}


object Main{
  def main(args: Array[String]): Unit = {
    InventoryManager.addStock("Laptop", 10)
    InventoryManager.addStock("Mouse", 20)
    InventoryManager.addStock("Keyboard", 15)
    
    InventoryManager.viewstock()
    InventoryManager.addStock("Mouse", 10)
    InventoryManager.viewstock()
    InventoryManager.addStock("abc", 10)
    InventoryManager.viewstock()
    InventoryManager.removeStock("Mouse", 10)
    InventoryManager.viewstock()
    
    
  }
}