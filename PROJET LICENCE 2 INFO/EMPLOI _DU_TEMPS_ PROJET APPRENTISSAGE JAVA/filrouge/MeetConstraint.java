package filrouge;

import java.util.HashMap;
import java.util.GregorianCalendar;

public class MeetConstraint extends BinaryConstraint implements Constraint{

	public MeetConstraint(Activity first, Activity second){

		super(first,second);

	}

	public boolean isSatisfied(Calendar date1,Calendar date2){
		return (date2.getTimeInMillis())-(date1.getTimeInMillis()) == this.first.getTimeInMinutes()*60000;
	}
	public boolean isSatisfiedBySchedule(HashMap<Activity, Integer> prog){
		return this.isSatisfied(prog.get(this.first), prog.get(this.second));
	}
}