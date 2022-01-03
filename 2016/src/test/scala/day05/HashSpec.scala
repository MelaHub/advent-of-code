package day05

import org.scalatest._
import flatspec._
import matchers._

class HashSpec extends AnyFlatSpec with should.Matchers {

  "A doorId and an index" should "be transformed into a correct hash" in {
    Day05.md5("abc", 3231929) should be(Hash("abc", 3231929,"00000155f8105dff7f56ee10fa9b9abd"))
  }

  "Searching the hash with leading zeroes" should "return a hash starting with siz zeroes" in {
    Day05.findHashWithLeadingZeroes("abc", 0) should be(Hash("abc", 3231929,"00000155f8105dff7f56ee10fa9b9abd"))
  }

  "A password" should "be valid" in  {
    Day05.getSequencePassword("abd") should be("18f47a30")
  }

}