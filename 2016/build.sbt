import Dependencies._

lazy val advent2016 = (project in file(".")).
  settings(
    inThisBuild(List(
      scalaVersion := "2.13.7"
    )),
    name := "advent2016",
    libraryDependencies += scalaTest % Test
  )
