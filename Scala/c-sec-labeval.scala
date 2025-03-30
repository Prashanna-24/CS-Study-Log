// dotproduct of 2 lists using higher order functions

object SumNumbersInString {
   def dotProduct(arr1: List[Int], arr2: List[Int]): Int = {
      var zipped = arr1.zip(arr2) // List((1,1), (2,2))
      var mapped = zipped.map(t=> t._1*t._2) // List(1,2)
      mapped.sum
   }
   
   def main(args: Array[String]): Unit = {
      
      var l1 = List(1,2,3)
      var l2 = List(3,2,1)
      print(dotProduct(l1, l2))
      
   }
}


// print list of m to n
object Mani{
   def func(m:Int, n:Int): List[Int] = {
      if (m>n) List()
      else m :: func(m+1, n)
   }
   
   def main(args:Array[String]) : Unit = {
      print(func(1,5))
   }
}

// recursive search
object Mani{
   def recSearch(arr: List[Int], target: Int, i:Int=0): Int = {
      if (arr.isEmpty) -1
      else if (arr.head==target) i
      else recSearch(arr.tail, target, i+1)
   }
   
   def main(args:Array[String]) : Unit = {
      val numbers = List(10, 20, 30, 40, 50)
      println(recSearch(numbers, 30))  // Output: 2
      println(recSearch(numbers, 100)) // Output: -1
   }
}