// 8 max frequency finder
object ElementCounter {
  def main(args: Array[String]): Unit = {
    var l1 = List(1, 2, 2, 3, 3, 3, 4, 1)
    var l1_grouped = l1.groupBy(x => x)
    println(l1_grouped)
    
    for((k,v) <- l1_grouped){
      print(k, v.length)
    }
    println()
    val map2 = l1_grouped.mapValues(_.length).toMap
    print(map2.maxBy(_._2)._1)
  }
}

----------------

// 9
object HammingDistanceCalculator {

  def compute(strand1: String, strand2: String): Int = {
    require(strand1.length == strand2.length, "DNA strands must be of equal length")
    
    strand1.zip(strand2).count(pair => pair._1 != pair._2)
  }

  def main(args: Array[String]): Unit = {
    val dna1 = "GAGCCTACTAACGGGAT"
    val dna2 = "CATCGTAATGACGGCCT"
    
    val distance = compute(dna1, dna2)
    println(s"The Hamming Distance is: $distance")
  }
}

---------------

// 10
object DropTillTrueApp {

  def dropTillTrue(lst: List[Int], condition: Int => Boolean): List[Int] = {
    lst.dropWhile(condition)
  }

  def main(args: Array[String]): Unit = {
    val result = dropTillTrue(List(1, 2, 3), x => x < 2)
    println(result)  // Output: List(2, 3)
  }
}

-----------------

// 13
// l1.distinct
def compress[A](list: List[A]): List[A] = list match {
  case Nil => Nil
  case head :: Nil => List(head)
  case head :: next :: tail =>
    if (head == next) compress(next :: tail)
    else head :: compress(next :: tail)
}
