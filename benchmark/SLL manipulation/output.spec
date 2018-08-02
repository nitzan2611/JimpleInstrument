type SLL {
  d:int
  l:SLL
  r:SLL
}

SLLManipulation (mut r0:SLL,mut r1:SLL,mut r2:SLL,mut r3:SLL,mut r4:SLL,mut i4:int) -> (res:int){
	var loc_SLL:SLL
	var i0:int
	var i1:int
	var i2:int
	var i3:int
	var i5:int
	var r5:SLL

	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}
	example {[r0==o0 && o0.d==0 && o0.l==null && o0.r==null && r1==o1 && o1.d==2 && o1.l==null && o1.r==null && r2==o2 && o2.d==3 && o2.l==null && o2.r==null && r3==o3 && o3.d==4 && o3.l==null && o3.r==null && r4==o4 && o4.d==5 && o4.l==null && o4.r==null && i4==3]
	-> i5 = 33;//r0.d==0 && r0.l==null && r0.r==null && r1.d==2 && r1.l==null && r1.r==null && r2.d==3 && r2.l==null && r2.r==null && r3.d==4 && r3.l==null && r3.r==null && r4.d==5 && r4.l==null && r4.r==null && $i0==0 && $i1==0 && $i2==0 && $i3==0 && i4==3 && i5==33 && r5==null]
	-> loc_SLL = r1;
	-> loc_SLL.d = 13;//r1.d==13 && r1.l==null && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.d = 12;//r2.d==12 && r2.l==null && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.d = 11;//r3.d==11 && r3.l==null && r3.r==null && 
	-> loc_SLL = r4;
	-> loc_SLL.d = 10;//r4.d==10 && r4.l==null && r4.r==null && 
	-> loc_SLL = r1;
	-> loc_SLL.l = r2;//r1.d==13 && r1.l==r2 && r1.r==null && 
	-> loc_SLL = r2;
	-> loc_SLL.l = r3;//r2.d==12 && r2.l==r3 && r2.r==null && 
	-> loc_SLL = r3;
	-> loc_SLL.l = r4;//r3.d==11 && r3.l==r4 && r3.r==null && 
	-> r5 = r1;//r5.d==13 && r5.l==r2 && r5.r==null
	-> i5 = i5 + 1;//i5==34 && 
	-> i0 = r5.d;//$i0==13 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==12 && r5.l==r3 && r5.r==null
	-> i4 = i4 + -1;//i4==2 && 
	-> i5 = i5 + 1;//i5==35 && 
	-> i0 = r5.d;//$i0==12 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==11 && r5.l==r4 && r5.r==null
	-> i4 = i4 + -1;//i4==1 && 
	-> i5 = i5 + 1;//i5==36 && 
	-> i0 = r5.d;//$i0==11 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//r5.d==10 && r5.l==null && r5.r==null
	-> i4 = i4 + -1;//i4==0 && 
	-> i5 = i5 + 1;//i5==37 && 
	-> i0 = r5.d;//$i0==10 && 
	-> loc_SLL = r5;
	-> r5 = loc_SLL.l;//
	-> i4 = i4 + -1;//i4==-1 && 
	}

}