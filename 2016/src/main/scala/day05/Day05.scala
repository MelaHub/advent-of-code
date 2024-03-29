package day05

import java.security.MessageDigest
import scala.annotation.tailrec
import scala.util.Random

case class Hash(doorId: String, index: Long, hash: String)

trait Password {
  def password: Array[Option[Char]]
  def +=(hash: String): Unit
  def isPasswordCompleted(): Boolean = password.forall(_.isDefined)
  def getPassword: String = password.flatten.mkString

}

class SequentialPassword private(val password: Array[Option[Char]]) extends Password {

  private def getPasswordDigit(hash: String, position: Int): Char = hash.charAt(position)

  override def +=(hash: String) = {
    val currHashChar = getPasswordDigit(hash, 5)
    password.update(password.count(_.isDefined), Some(currHashChar))
  }

}

object SequentialPassword {
  def apply(passLength: Int): SequentialPassword = new SequentialPassword(Array.fill(passLength)(Option.empty[Char]))
}

class BetterPassword private(val password: Array[Option[Char]]) extends Password {

  private def getPasswordDigit(hash: String, position: Int): Char = hash.charAt(position)
  private def getPasswordPosition(hash: String, position: Int): Char = hash.charAt(position)

  override def +=(hash: String): Unit = {
    val currHashPos = getPasswordPosition(hash, 5).asDigit
    if (currHashPos >= password.length) this
    else {
      if (password(currHashPos).isEmpty) password.update(currHashPos, Some(getPasswordDigit(hash, 6)))
    }
  }
}

object BetterPassword {

  def apply(passLength: Int): BetterPassword = new BetterPassword(Array.fill(passLength)(Option.empty[Char]))
}


object Day05 extends App {

  private val doorId = "wtnhxymk"

  private val passLength = 8

  private[day05] def md5(doorId: String, index: Long): Hash =
    Hash(doorId, index, MessageDigest.getInstance("MD5").digest(s"$doorId${index.toString}".getBytes("UTF-8")).map("%02x".format(_)).mkString)

  private def printPass(currPassword: Password) =
    print(s"${currPassword.password.map {
      case None => Random.alphanumeric.take(1).mkString.charAt(0)
      case Some(c) => c
    }.mkString}\r")

  @tailrec
  private[day05] def findHashWithLeadingZeroes(doorId: String, startingIndex: Long, currPassword: Password): Hash = {
      if (startingIndex % 10000 == 0) printPass(currPassword)
      md5(doorId, startingIndex) match {
        case hash@Hash(_, _, h) if h.startsWith("00000") => hash
        case _ => findHashWithLeadingZeroes(doorId, startingIndex + 1, currPassword)
      }
  }

  @tailrec
  private[day05] def getPasswordRe(doorId: String, startingIndex: Long, currPassword: Password): String =
    if (currPassword.isPasswordCompleted()) {
      currPassword.getPassword
    } else {
      val hashWithLeadingZeroes = findHashWithLeadingZeroes(doorId, startingIndex, currPassword)
      currPassword += hashWithLeadingZeroes.hash
      getPasswordRe(doorId, hashWithLeadingZeroes.index + 1, currPassword)
    }

  private[day05] def getSequencePassword(doorId: String): String = getPasswordRe(doorId, 0, SequentialPassword(passLength))

  private[day05] def getBetterPassword(doorId: String): String = getPasswordRe(doorId, 0, BetterPassword(passLength))

  println(s"Getting the password in sequence:")
  println(s"${getSequencePassword(doorId)}")
  println(s"Getting the better password:")
  println(s"${getBetterPassword(doorId)}")

}
