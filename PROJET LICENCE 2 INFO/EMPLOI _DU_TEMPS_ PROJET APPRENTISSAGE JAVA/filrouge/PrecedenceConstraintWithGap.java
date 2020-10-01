package filrouge;
import java.util.HashMap;
public class PrecedenceConstraintWithGap extends PrecedenceConstraint implements Constraint {

	private int gap;


	public PrecedenceConstraintWithGap(Activity first, Activity second, int tmps){

		super(first,second);
		this.gap = tmps;
	}

	public boolean isSatisfied(int date1, int date2){

		int tmpsRestnt = (date2*60)-(date1*60)-this.gap;
		if (tmpsRestnt>= this.getFirstAct().getTimeInMinutes()) {
			
			return true;
	}
		
		else{
			
			return false;
		}


}
	
	public boolean isSatisfiedBySchedule(HashMap<Activity, Integer> prog){
		return this.isSatisfied(prog.get(this.first), prog.get(this.second));
	}

}