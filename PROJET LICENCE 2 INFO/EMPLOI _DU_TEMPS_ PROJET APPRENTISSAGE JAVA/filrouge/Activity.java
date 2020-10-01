package filrouge;

public class Activity {

	private String actName;
	private int time;


	public Activity(String actName, int time){

		this.actName = actName;

		this.time = time; 

	}

	public int getTimeInMinutes(){
		return this.time;
	}

	

}

