package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import sample.model.RssAlgorithm;

import javax.swing.*;
import java.awt.*;

public class Main extends Canvas {

    Point point1 = new Point(150,0);
    Point point2 = new Point(150,280);
    Point point3 = new Point(280,150);
    RssAlgorithm rssAlgorithm = new RssAlgorithm(2417,point1,point2,point3);

    /**
     * In the main method we created a cnvans to present a room as test subject
     * @param args
     */

    public static void main(String[] args) {

        JFrame frame = new JFrame("Room");
        Canvas canvas = new Main();
        canvas.setSize(300,300);
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
        rssAlgorithm.setP1dbm(55);
        rssAlgorithm.setP2dbm(66);
        rssAlgorithm.setP3dbm(67);
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
                x =(int) rssAlgorithm.targetPosition(point2).getX();
                y=(int) rssAlgorithm.targetPosition(point2).getY();
*/
                System.out.print(" The Cheater is in position between  " +"("+x+","+y+")" );
            }
            if (m==0){
                /*
                x =(int) rssAlgorithm.targetPosition(point1).getX();
                y=(int) rssAlgorithm.targetPosition(point1).getY();

                 */
                x =(int) rssAlgorithm.targetPosition3().getX();
                y=(int) rssAlgorithm.targetPosition3().getY();
                System.out.println(" And   " +"("+x+","+y+")" );
            }


            g.fillOval(x, y, 15, 15);
            m--;

        }

    }

}
