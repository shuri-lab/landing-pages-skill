ObjC.import('AppKit');
function run(argv){
  var dir=argv[0], out=argv[1], n=parseInt(argv[2]), cols=5, w=300, h=169, pad=6;
  var rows=Math.ceil(n/cols), W=cols*(w+pad), H=rows*(h+pad+16);
  var img=$.NSImage.alloc.initWithSize($.NSMakeSize(W,H)); img.lockFocus;
  $.NSColor.whiteColor.set; $.NSRectFill($.NSMakeRect(0,0,W,H));
  for(var i=0;i<n;i++){var nm=('0'+(i+1)).slice(-2);
    var t=$.NSImage.alloc.initWithContentsOfFile(dir+'/s-page-'+nm+'.png'); var c=i%cols, r=Math.floor(i/cols);
    var y=H-(r+1)*(h+pad+16);
    t.drawInRectFromRectOperationFraction($.NSMakeRect(c*(w+pad),y+16,w,h),$.NSZeroRect,2,1);
    $(nm).drawAtPointWithAttributes($.NSMakePoint(c*(w+pad)+2,y),$());}
  img.unlockFocus;
  var rep=$.NSBitmapImageRep.imageRepWithData(img.TIFFRepresentation);
  rep.representationUsingTypeProperties(3,$()).writeToFileAtomically(out,true); return 'ok';
}
