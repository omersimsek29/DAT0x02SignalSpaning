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



    public static void main(String[] args) {

        JFrame frame = new JFrame("Room");
        Canvas canvas = new Main();
        canvas.setSize(300,300);
        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);

    }
    public void paint(Graphics g) {
        rssAlgorithm.setP1dbm(61);
        rssAlgorithm.setP2dbm(41);
        rssAlgorithm.setP3dbm(61);
        int m=3;
        int x  =(int) point1.getX();
        int y=(int) point1.getY();
        while (m>=0) {
            if (m==2){
                x =(int) point2.getX();
                y=(int) point2.getY();

            }
            if (m==1){
                x =(int) point3.getX();
                y=(int) point3.getY();
            } if (m==0){

                x =(int) rssAlgorithm.targetPosition().getX();
                y=(int) rssAlgorithm.targetPosition().getY();


            }


            g.fillOval(x, y, 15, 15);
            m--;

        }

    }

}
