package filrouge;

import java.util.HashMap;

public class PrecedenceConstraint implements Constraint {

	protected Activity first;
	protected Activity second;

	public PrecedenceConstraint(Activity cr1, Activity cr2){

		this.first = cr1;
		this.second = cr2;
	}

	public boolean isSatisfied(int date1 , int date2){
		return (date2*60)-(date1*60) >= this.first.getTimeInMinutes();
	}

	public Activity getFirstAct(){

		return this.first;
	}

	public Activity getSecond(){

		return this.second;
	}


	public boolean isSatisfiedBySchedule(HashMap<Activity, Integer> prog){
		return this.isSatisfied(prog.get(this.first), prog.get(this.second));
	}
}