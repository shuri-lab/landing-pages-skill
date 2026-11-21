import sys, zlib, struct
def read_png(p):
    d=open(p,'rb').read(); assert d[:8]==b'\x89PNG\r\n\x1a\n'
    i=8; idat=b''; 
    while i<len(d):
        ln,=struct.unpack('>I',d[i:i+4]); t=d[i+4:i+8]; c=d[i+8:i+8+ln]; i+=12+ln
        if t==b'IHDR': w,h,bd,ct=struct.unpack('>IIBB',c[:10])
        elif t==b'IDAT': idat+=c
    assert bd==8 and ct in (2,6), (bd,ct)
    bpp=4 if ct==6 else 3; raw=zlib.decompress(idat); stride=w*bpp
    rows=[]; prev=bytearray(stride); o=0
    for y in range(h):
        f=raw[o]; o+=1; cur=bytearray(raw[o:o+stride]); o+=stride
        for x in range(stride):
            a=cur[x-bpp] if x>=bpp else 0; b=prev[x]; c=prev[x-bpp] if x>=bpp else 0
            if f==1: cur[x]=(cur[x]+a)&255
            elif f==2: cur[x]=(cur[x]+b)&255
            elif f==3: cur[x]=(cur[x]+((a+b)>>1))&255
            elif f==4:
                pp=a+b-c; pa=abs(pp-a); pb=abs(pp-b); pc=abs(pp-c)
                cur[x]=(cur[x]+(a if pa<=pb and pa<=pc else b if pb<=pc else c))&255
        rows.append(cur); prev=cur
    return w,h,bpp,rows
w,h,bpp,rows=read_png(sys.argv[1])
x0,y0,x1,y1=w,h,-1,-1
for y,r in enumerate(rows):
    for x in range(w):
        on = r[x*4+3]>16 if bpp==4 else min(r[x*3:x*3+3])<240
        if on:
            if x<x0:x0=x
            if x>x1:x1=x
            if y<y0:y0=y
            y1=y
pad=int(sys.argv[2]) if len(sys.argv)>2 else 0
x0=max(0,x0-pad);y0=max(0,y0-pad);x1=min(w-1,x1+pad);y1=min(h-1,y1+pad)
print(y1-y0+1, x1-x0+1, y0, x0)
