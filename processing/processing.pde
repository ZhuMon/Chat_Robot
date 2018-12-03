PGraphics gp;
void setup(){
  size(180, 180);
  
  gp = createGraphics(width, height);
  
 
  //noSmooth();
}
void draw(){
  char[] A1 = {'A', '1'};
  char[] A2 = {'A', '2'};
  char[] A3 = {'A', '3'};
  char[] B1 = {'B', '1'};
  char[] B2 = {'B', '2'};
  char[] B3 = {'B', '3'};
  char[] C1 = {'C', '1'};
  char[] C2 = {'C', '2'};
  char[] C3 = {'C', '3'};
  
  gp.beginDraw();
  gp.line(0, 60, 180, 60);
  gp.line(0, 120, 180, 120);
  gp.line(60, 0, 60, 180);
  gp.line(120, 0, 120, 180);
  
  my_x(A3);
  gp.endDraw();
  image(gp, 0, 0);
  gp.save("A3_x.png");
  
  
  
}
void my_o(char[] which) {
  int o_x = 0;
  int o_y = 0;
  if(which[0] == 'A'){
    o_x = 30;
  } else if(which[0] == 'B'){
    o_x = 90;
  } else if(which[0] == 'C'){
    o_x = 150;
  }
  
  if(which[1] == '1'){
    o_y = 30;
  } else if(which[1] == '2'){
    o_y = 90;
  } else if(which[1] == '3'){
    o_y = 150;
  }
  gp.ellipse(o_x, o_y, 30, 30);
}

void my_x(char[] which){
  int lx = 0;
  int hx = 0;
  int ly = 0;
  int hy = 0;
  if(which[0] == 'A'){
    lx = 15;
    hx = 45;
  } else if(which[0] == 'B'){
    lx = 75;
    hx = 105;
  } else if(which[0] == 'C'){
    lx = 135;
    hx = 165;
  }
  
  if(which[1] == '1'){
    ly = 15;
    hy = 45;
  } else if(which[1] == '2'){
    ly = 75;
    hy = 105;
  } else if(which[1] == '3'){
    ly = 135;
    hy = 165;
  }
  gp.line(lx, ly, hx, hy);
  gp.line(hx, ly, lx, hy);
  
}
