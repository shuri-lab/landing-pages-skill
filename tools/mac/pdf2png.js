ObjC.import('PDFKit'); ObjC.import('AppKit');
function run(argv){
  var doc = $.PDFDocument.alloc.initWithURL($.NSURL.fileURLWithPath(argv[0]));
  var out = argv[1], W = parseFloat(argv[2]||'1400'), txt='';
  for (var i=0;i<doc.pageCount;i++){
    var p = doc.pageAtIndex(i), b = p.boundsForBox(0), s = W/b.size.width;
    var img = p.thumbnailOfSizeForBox($.NSMakeSize(b.size.width*s, b.size.height*s), 0);
    var rep = $.NSBitmapImageRep.imageRepWithData(img.TIFFRepresentation);
    var png = rep.representationUsingTypeProperties(4, $());
    var n = ('0'+(i+1)).slice(-2);
    png.writeToFileAtomically(out+'/page-'+n+'.png', true);
    txt += '=== page '+n+'\n'+ (p.string.js||'') + '\n';
  }
  return txt;
}
