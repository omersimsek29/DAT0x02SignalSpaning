package sample.model;
import java.lang.Math;


// this class is responsible of signal strength algorithm calculation
public class RssAlgorithm {
   private int dbm ;
    private int frequency;

 public RssAlgorithm(int dbm ,int frequency){
    this.dbm=dbm;
    this.frequency=frequency;
}

    /**
     * This method is to give the predicted distance between a node and transmitter.
     * @FSPL is free space path loss
     */
   public void distanceBetweenNodeAndSource(){
    double FSPL = 27.55;

    double d = Math.pow(10 , (((FSPL-(20*Math.log10(frequency)))+Math.abs(dbm))/20));
        d= Math.round(d);


        System.out.println("The predicted distance is " +d+" m");

    }


}
