setwd("/home/so/languages")

languages = c('java','c','c++','python','.net', 'c#', 'javascript', 'sql','php','assembly',
              'objective-c', 'delphi', 'perl','matlab','ruby','vba','groovy','swift','go','r',
              'sas','abap','fortran', 'dart','scala', 'prolog', 'lisp', 'lua', 'rust', 'ada',
              'f#', 'apex', 'kotlin', 'scheme', 'labview', 'typescript', 'julia', 'awk', 'haskell',
              'clojure', 'erlang', 'bash', 'elixir', 'html', 'vhdl', 'verilog', 
              'actionscript-3', 'cobol', 'coffeescript', 'common-lisp', 'd', 'netlogo',
              'plsql', 'powershell', 'vb.net', 'vbscript')

for (language in languages){
  df <- 0
  filename <- paste(language, ".csv", sep = "", collapse = NULL)
  lang = read.csv(filename)
  
  i <- 0
  for (language2 in languages) {
    if (language2 == language){
      next
    }
    filename2 <- paste(language2, ".csv", sep = "", collapse = NULL)
    lang2 <- read.csv((filename2))
    total = merge(lang,lang2, by='date')
    count = cor(total['count.x'], total['count.y'])
    normviews = cor(total['normalized.viewcount.x'], total['normalized.viewcount.y'])
    positive = cor(total['positive.x'], total['positive.y'])
    negative = cor(total['negative.x'], total['negative.y'])
    if (i == 0){
      df <- data.frame(language2, count[1], positive[1], negative[1], normviews[1])
      names(df) <- c("Language", "Questions", "Positive", "Negative", "Views")
    }
    else {
      de <- data.frame(language2, count[1], positive[1], negative[1], normviews[1])
      names(de) <- c("Language", "Questions", "Positive", "Negative", "Views")
      df <- rbind(df, de)
    }
    i <- 1
  }
  dz <- data.frame(df[,1],round(df[,2],4),round(df[,3],4),round(df[,4],4), round(df[,5],4))
  names(dz) <- names(df)
  outfile <- paste("/home/so/languagecorrelations/", language, ".csv", sep = "", collapse = NULL)
  write.csv(format(dz[order(-dz$Questions),],digits=4), outfile, quote=FALSE,row.names=FALSE)
}
