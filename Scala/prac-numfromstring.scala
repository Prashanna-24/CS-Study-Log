// Write a Scala program to calculate the sum of the numbers appear in a given string.
// The given string is: it 15 is25 a 20string
// The sum of the numbers in the said string is: 60


object SumNumbersInString {
   def func(x: String): Int = {
      var num = ""
      var sum = 0
      for (ch <- x){
         if (ch.isDigit){
         num += ch
         } else if (num.nonEmpty){
         sum += num.toInt
         num = ""
         }
      }
      if (num.nonEmpty) sum += num.toInt
      sum
   } 
   
   
   def main(args: Array[String]): Unit = {
      println(func("it 15 is25 a 20string"))
   }
}
