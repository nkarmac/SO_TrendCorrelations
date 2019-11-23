// modified from Daniel German's script found at https://github.com/dmgerman/stackOverflowParsing

import scala.io.Source
import scala.xml.pull._
import scala.collection.mutable.ArrayBuffer
import java.io.File
import java.io.FileOutputStream
import scala.xml.XML
import scala.xml._
 

val xml = new XMLEventReader(Source.stdin)

def clean(at:Seq[Node]):String = {
  if (at == null) {
    ""
  } else {
    at.mkString.replaceAll(";", "<SEMICOLON>")
  }
}

def clean2(at:Seq[Node]):Array[String] = {
  if (at == null) {
    Array()
  } else {
    at.mkString.replaceAll("&lt;", "").replaceAll("&gt;", ";").split(";").filter(_ != "")
  }
}

xml.filter{ event =>
  event match {
    case EvElemStart(_, "row", attrs, _) => true
    case _ => false
  }
}.map { event => 
  event match {
    case EvElemStart(_, _, attrs, _) => {

      (
        clean(attrs("Id")),
        clean(attrs("PostTypeId")),
        clean(attrs("ViewCount")),
        clean2(attrs("Tags"))
      )
    }
  }
}.foreach{ case(id, posttype, views, tags) =>
    tags.foreach{ t =>
      println(s"${id}|${posttype}|${views}|${t}")
    }
}
 

