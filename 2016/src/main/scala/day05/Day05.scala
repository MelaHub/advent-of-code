package day05

import java.security.MessageDigest
import scala.annotation.tailrec

case class Hash(doorId: String, index: Long, hash: String)


object Day05 extends App {

  private[day05] def md5(doorId: String, index: Long): Hash =
    Hash(doorId, index, MessageDigest.getInstance("MD5").digest(s"$doorId${index.toString}".getBytes("UTF-8")).map("%02x".format(_)).mkString)

  @tailrec
  private[day05] def findHashWithLeadingZeroes(doorId: String, startingIndex: Long): Hash =
      md5(doorId, startingIndex) match {
        case hash@Hash(_, _, h) if h.startsWith("00000") => hash
        case _ => findHashWithLeadingZeroes(doorId, startingIndex + 1)
      }

  private[day05] def getPasswordDigit(hash: Hash): Char = hash.hash.charAt(5)

  @tailrec
  private[day05] def getPasswordRe(doorId: String, startingIndex: Long, currPassword: String): String = {
    if (currPassword.length == 8)
      currPassword
    else {
      val hashWithLeadingZeroes = findHashWithLeadingZeroes(doorId, startingIndex)
      getPasswordRe(doorId, hashWithLeadingZeroes.index + 1, s"$currPassword${getPasswordDigit(hashWithLeadingZeroes)}")
    }
  }

  private[day05] def getPassword(doorId: String): String = getPasswordRe(doorId, 0, "")

  println(s"The password is ${getPassword("wtnhxymk")}")

}
