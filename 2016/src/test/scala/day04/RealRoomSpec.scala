package day04

import org.scalatest._
import flatspec._
import matchers._

class RealRoomSpec extends AnyFlatSpec with should.Matchers {

  "The room object" should "recognize a real room" in {
    Room("aaaaa-bbb-z-y-x", 123, "abxyz").isReal shouldEqual true
    Room("a-b-c-d-e-f-g-h", 987, "abcde").isReal shouldEqual true
    Room("not-a-real-room", 404, "oarel").isReal shouldEqual true
    Room("totally-real-room", 200, "decoy").isReal shouldEqual false
  }

  "The room name decoder" should "retrieve the real name of the room" in {
    Room("a-b-c-d-e-f-g-h", 987, "abcde").realName shouldEqual "z-a-b-c-d-e-f-g"
  }
}