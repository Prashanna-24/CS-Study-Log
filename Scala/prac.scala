import scala.collection.mutable.ArrayBuffer

object blah{
  def main(args: Array[String]): Unit = {
    // for (i <- 1 until 3; j <- 3 to 5) {
    //   print(i + " ")
    //   println(j)
    // }
    
    // def func1(args: Int*): Int ={
    //   var sum1 = 0
    //   for(i <- args){
    //     sum1 += i
    //   }
    //   sum1
    // }
    // println(func1(1,2,3,4))
    
    // var arrbuf2 = ArrayBuffer(11,22,33,44,55)
    // var temp_arr = arrbuf2.filter(x => x>33)
    // println(temp_arr)
    
    // val x = 5
    // var arrbuf1 = ArrayBuffer[Int]()
    // arrbuf1 += x
    // println(arrbuf1)
    
    // lambda and partial function
    // val sum = (a: Int, b: Int, c: Int) => a + b + c
    // val f = sum(10, _: Int, 30)  
    // println(f(20)) 
    // println(2 max 3)
    // print(math.max(2,3))

    // def describe(x: Any) = x match {
    //   case 5 => "five"
    //   case true => "truth"
    //   case "hello" => "hi!"
    //   case Nil => "the empty list"
    //   case _ => "something else"
    // }

    // there is no patern matching for ArrayBuffer. so we convert it to list
    // val arrBuf = ArrayBuffer(1, 2, 3)
    // arrBuf.toList match {
    //   case Nil => println("Empty list")
    //   case head :: tail => println(s"Head: $head, Tail: $tail")
    // }

    // IO
    // println("Hello, Scala!")  // Prints with a newline
    // print("Hello, ")          // Prints without newline
    // printf("Pi: %.2f\n", 3.14159)  // Formatted output

    // import scala.io.StdIn
    // val name = StdIn.readLine() // also readInt()
    // println(s"Hello, $name!")

    import scala.util.control.Breaks._

    breakable {
      for (i <- 1 to 10) {
        if (i == 5) break()  // Breaks out of the loop when i == 5
        println(i)
      }
    }
    println("Loop exited")

  }
}