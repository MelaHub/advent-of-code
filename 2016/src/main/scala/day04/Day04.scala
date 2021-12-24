package day04

import java.io.InputStream
import scala.io.Source

class NoMatchingRoomException(roomString: String) extends Exception

object Day04 extends App {

  private val roomRegex = """^(.*)\-([\d]+)\[(.*)\]$""".r

  private def getInputRooms(): Iterator[Room] = {
    val resource: InputStream = this.getClass.getClassLoader.getResourceAsStream("day04_input")
    val source = Source.fromInputStream(resource)
    source
      .getLines()
      .map(
        row => row match {
          case roomRegex(encryptedName, sector, checksum) => Some(Room(encryptedName, sector.toInt, checksum))
          case _ => {
            println(s"Room $row doesn't look like a room description")
            None
          }
        }
      )
      .flatten
  }

  def getSectorIdsOfRealrooms(): Int = getInputRooms().filter(_.isReal).map(_.sectorId).sum

  def getSectorIdOfNorthPoleObjRoom() = getInputRooms().find(_.realName.contains("northpole")).map(_.sectorId)

  println(s"The sum of the sector IDs of the real rooms is ${getSectorIdsOfRealrooms()} ")
  println(s"The number of the north pole objects is ${getSectorIdOfNorthPoleObjRoom()}")

}
