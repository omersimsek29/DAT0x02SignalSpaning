package sample.model;
import java.awt.*;
import java.lang.Math;
import java.util.HashMap;
import java.util.Map;


// this class is responsible of signal strength algorithm calculation
public class RssAlgorithm {

    private int frequency;
    private  Point ab1;
    private Point ab2 ;
    private  Point ab3 ;
    int p1dbm=0;
    int p2dbm=0;
    int p3dbm=0;

 public RssAlgorithm(int frequency, Point ab1 ,Point ab2 ,Point ab3){

    this.frequency=frequency;
    this.ab1=ab1;
    this.ab2=ab2;
    this.ab3=ab3;

}

    public void setP1dbm(int p1dbm) {
        this.p1dbm = p1dbm;
    }

    public void setP2dbm(int p2dbm) {
        this.p2dbm = p2dbm;
    }

    public void setP3dbm(int p3dbm) {
        this.p3dbm = p3dbm;
    }

    /**
     * This method is to give the predicted distance between a node and transmitter.
     * @FSPL is free space path loss which depend most on the AP.
     */
   public int  distanceBetweenNodeAndSource( int dbm){
    double FSPL = 27.55;

    double d =  Math.pow(10 , (((FSPL-(20*Math.log10(frequency)))+Math.abs(dbm))/20));

        d=  Math.round(d);

        return (int) d;

    }

    /**
     * This method tage a point which should be between point a or b
     * and return a point to the predicted location of a TI
     * @param a
     * @return Point of an (x,Y)
     */

   public Point targetPosition(Point a ){
       int d1 = distanceBetweenNodeAndSource(p1dbm);
       int d2 = distanceBetweenNodeAndSource(p2dbm);
       int d3 = distanceBetweenNodeAndSource(p3dbm);
       int y=0;
       int x = 0;
if (a==ab1){
    y = (int) (ab1.getY()+(d1*10));


}else if (a==ab2){
     y = (int) (ab2.getY()-(d2*10));

}
  //     System.out.println("y"+y);

        x = (int) (ab3.getX()-(d3*10));
//       System.out.println("x"+x);

       return new Point(x,y);
    }

}
