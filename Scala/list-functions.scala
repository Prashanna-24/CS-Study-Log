val emptyList = List()        // Empty list
val numList = List(1, 2, 3, 4)
val strList = List("Scala", "Python", "Go")

val repeated = List.fill(3)("Hello")  // List("Hello", "Hello", "Hello")
val range = List.range(1, 5)          // List(1, 2, 3, 4)

println(numList.head)   // 1 (First element)
println(numList.tail)   // List(2, 3, 4) (All except first)
println(numList.last)   // 4 (Last element)
println(numList.init)   // List(1, 2, 3) (All except last)
println(numList(2))     // 3 (Element at index 2)
println(numList.isEmpty) // false (Check if empty)

val newList1 = 0 :: numList     // List(0, 1, 2, 3, 4) (Prepend using `::`)
val newList2 = numList :+ 5     // List(1, 2, 3, 4, 5) (Append)
val newList3 = 0 +: numList     // List(0, 1, 2, 3, 4) (Prepend)
val mergedList = numList ++ List(5, 6)  // List(1, 2, 3, 4, 5, 6) (Concatenation)

val filtered = numList.filter(_ % 2 == 0)  // List(2, 4) (Only even numbers)
val dropped = numList.drop(2)  // List(3, 4) (Drop first 2 elements)
val taken = numList.take(3)    // List(1, 2, 3) (Take first 3 elements)


def checkList(lst: List[Int]): String = lst match {
  case Nil => "The list is empty"
  case _   => "The list is not empty"
}
println(checkList(List()))       // Output: The list is empty
println(checkList(List(1, 2)))   // Output: The list is not empty



def checkSingleElement(lst: List[Int]): String = lst match {
  case List(x) => s"Single element: $x"
  case _       => "Not a single-element list"
}
println(checkSingleElement(List(42)))  // Output: Single element: 42
println(checkSingleElement(List()))    // Output: Not a single-element list
println(checkSingleElement(List(1, 2))) // Output: Not a single-element list


def processList(lst: List[Int]): String = lst match {
  case head :: tail => s"Head: $head, Tail: $tail"
  case Nil => "Empty list"
}
println(processList(List(1, 2, 3)))  // Output: Head: 1, Tail: List(2, 3)
println(processList(List(42)))       // Output: Head: 42, Tail: List()
println(processList(List()))         // Output: Empty list


def matchWild(lst: List[Int]): String = lst match {
  case _ :: second :: _ => s"Second element is $second"
  case _ => "List too short"
}
println(matchWild(List(10, 20, 30)))  // Output: Second element is 20
println(matchWild(List(5)))           // Output: List too short


import scala.collection.mutable.ListBuffer

val nums = ListBuffer(1, 2, 3)
// Append a single element
nums += 4  
println(nums)  // ListBuffer(1, 2, 3, 4)
// Append multiple elements
nums ++= List(5, 6)
println(nums)  // ListBuffer(1, 2, 3, 4, 5, 6)
// Prepend a single element
1 +=: nums  
println(nums)  // ListBuffer(1, 2, 3, 4)
// Prepend multiple elements
List(-1, 0) ++=: nums
println(nums)  // ListBuffer(-1, 0, 1, 2, 3, 4)
