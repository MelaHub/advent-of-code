package day05

import java.security.MessageDigest
import scala.annotation.tailrec

case class Hash(doorId: String, index: Long, hash: String)

trait Password {
  def passLength: Int
  def +(hash: String): Password
  def getPassword: Option[String]
}

class SequentialPassword(val passLength: Int, password: String) extends Password {

  private[day05] def getPasswordDigit(hash: String, position: Int): Char = hash.charAt(position)

  override def +(hash: String): SequentialPassword = new SequentialPassword(passLength, password + getPasswordDigit(hash, 5))

  override def getPassword: Option[String] = password.length match {
    case n if n == passLength => Some(password)
    case _ => None
  }
}


object Day05 extends App {

  private val doorId = "wtnhxymk"

  private val passLength = 8

  private[day05] def md5(doorId: String, index: Long): Hash =
    Hash(doorId, index, MessageDigest.getInstance("MD5").digest(s"$doorId${index.toString}".getBytes("UTF-8")).map("%02x".format(_)).mkString)

  @tailrec
  private[day05] def findHashWithLeadingZeroes(doorId: String, startingIndex: Long): Hash =
      md5(doorId, startingIndex) match {
        case hash@Hash(_, _, h) if h.startsWith("00000") => hash
        case _ => findHashWithLeadingZeroes(doorId, startingIndex + 1)
      }

  @tailrec
  private[day05] def getPasswordRe(doorId: String, startingIndex: Long, currPassword: Password): String =
    currPassword.getPassword match {
      case Some(pass) => pass
      case None => {
        val hashWithLeadingZeroes = findHashWithLeadingZeroes(doorId, startingIndex)
        getPasswordRe(doorId, hashWithLeadingZeroes.index + 1, currPassword + hashWithLeadingZeroes.hash)
      }
    }

  private[day05] def getSequencePassword(doorId: String): String = getPasswordRe(doorId, 0, new SequentialPassword(passLength, ""))

  println(s"The password in sequence is ${getSequencePassword(doorId)}")

}
