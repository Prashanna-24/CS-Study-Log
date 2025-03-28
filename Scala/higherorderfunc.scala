object SumNumbersInString {
   def main(args: Array[String]): Unit = {
      
      var l1 = List(1,2,3,4,5,6)
      var l1_map = l1.map(x=> x*2)
      var l1_filter = l1.filter(_>3)
      val l1_fold = l1.fold(10)(_ + _)
      val l1_grouped = l1.groupBy(_ % 2)
      val hasEven = nums.exists(_ % 2 == 0)
      val allEven = nums.forall(_ % 2 == 0)

      println(l1_map)
      println(l1_filter)
      println(l1_grouped)

      val l1 = List(1, 2, 3)
      val l2 = List("a", "b", "c")

      val zipped = l1.zip(l2)
      println(zipped)

      val arr = Array(1,2,-3,2,4,-6,-7,2)
      arr.filter((x)=> x<0).reduce(_*_)
      
   }
}



object ArmstrongNumberChecker {
   def isArmstrong(num: Int): Boolean = {
      val digits = num.toString.map(_.asDigit) // Extract digits
      val power = digits.length // Number of digits
      val sum = digits.map(d => math.pow(d, power).toInt).sum // Sum of each digit raised to power
      sum == num
   }

   def main(args: Array[String]): Unit = {
      val testNumbers = List(153, 9474, 9475, 371, 407, 9475)
      testNumbers.foreach(num => 
         println(s"$num is ${if (isArmstrong(num)) "an Armstrong" else "not an Armstrong"} number")
      )
   }
}