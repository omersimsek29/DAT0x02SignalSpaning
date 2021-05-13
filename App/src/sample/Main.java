package sample;


import sample.model.RssAlgorithm;

import javax.swing.*;
import java.awt.*;

public class Main extends Canvas {

    Point point1 = new Point(0,0);
    Point point2 = new Point(3,7);
    Point point3 = new Point(6,0);
    RssAlgorithm rssAlgorithm = new RssAlgorithm(2417,point1,point2,point3);
    int[]dbm1 = {-56, -56, -56,55 ,55 ,55 ,52 ,52 ,52 , 54 };
    int[]dbm2={-42,-42, 42, 42,42 ,42 ,41 ,41 ,41 ,41 };
    int []dbm3 = {-53,-53,53 , 55,55 ,55 ,53 ,53 , 53, 54};

    /**
     * In the main method we created a canvas to present a room as test subject
     * @param args
     */

    public static void main(String[] args) {

        JFrame frame = new JFrame("Room");
        Canvas canvas = new Main();
        canvas.setSize(700,700);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);


    }

    /**
     * In this method we paint 5 points in the room that we made 3 of them
     * are the main points as AP point and the other 2 are the predicted one
     * @param g
     */
    public void paint(Graphics g) {
        //rssAlgorithm.setP1dbm(50);
        //rssAlgorithm.setP2dbm(75);
        //rssAlgorithm.setP3dbm(44);
      /*
        int m=4;
        int x  =(int) point1.getX();
        int y=(int) point1.getY();
        while (m>=0) {

                if (m==3){
                x =(int) point2.getX();
                y=(int) point2.getY();

            }
            if (m==2){
                x =(int) point3.getX();
                y=(int) point3.getY();
            } if (m==1){
                /*
                x =(int) rssAlgorithm.targetPosition().getX();
                y=(int) rssAlgorithm.targetPosition().getY();

               // System.out.print(" The Cheater is in position between  " +"("+x+","+y+")" );
            }
            if (m==0){
                /*
                x =(int) rssAlgorithm.targetPosition(point1).getX();
                y=(int) rssAlgorithm.targetPosition(point1).getY();


            //    x =(int) rssAlgorithm.targetPosition2().getX();
              //  y=(int) rssAlgorithm.targetPosition2().getY();

            }
            */
test1();
/*
            g.fillOval(x, y, 15, 15);
            m--;

        }
*/
    }

    void test1  (){
        int a = 0;
        while (a<dbm1.length){
            rssAlgorithm.setP1dbm(dbm1[a]);
            rssAlgorithm.setP2dbm(dbm2[a]);
            rssAlgorithm.setP3dbm(dbm3[a]);
      //System.out.println(rssAlgorithm.targetPosition(1)+"between"+rssAlgorithm.targetPosition(2)+""+a);
            System.out.println(rssAlgorithm.targetPosition2() +""+a);

            a++;
        }

    }

}
