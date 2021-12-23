package day04

case class Room(encryptedName: String, sectorId: Int, checksum: String) {

  lazy val isReal: Boolean = encryptedName
    .filterNot(_ == '-')
    .groupBy(identity)
    .mapValues(_.length)
    .toList
    .sortBy{ case (c, l) => (-l, c)}
    .take(5)
    .map(_._1)
    .mkString == checksum


}


