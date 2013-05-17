package lab5;
/**
 * Name: Adrienne Sands
 * Lab Section: A
 * Date: 10/10/10
 * Lab5.java
 * CSE 131 Lab 5
 * Purpose of class: to implement eyeballTool on a defined panel
 */

import nip.GraphicsPanel;
import nip.NIP;

public class Lab5 {
	public EyeballTool eyeballTool;
	public GraphicsPanel panel;

	public Lab5(GraphicsPanel panel) {
		this.panel = panel;
		this.eyeballTool = new EyeballTool(panel);

	}

	public static void main(String[] args) {
		NIP nip = new NIP(300, 300, 2, "", "ken.jpg");
		nip.setTool(new EyeballTool((nip.getTargetPanel())));
		nip.addTool(new CloningTool());
	}
}
