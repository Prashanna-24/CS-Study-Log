object PalindromeCheck {
   def isPalindrome(n: Int): Boolean = {
      val str = n.toString
      str == str.reverse
   }

   def main(args: Array[String]): Unit = {
      val num = 121
      println(s"$num is a palindrome: ${isPalindrome(num)}")
   }
}
