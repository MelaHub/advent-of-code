package day03

case class Shape(lengths: Seq[Int]) {

  lazy val is_a_valid_triangle: Boolean = lengths match {
    case a :: b :: c :: Nil => a + b > c && a + c > b && b + c > a
    case _ => false
  }

}

