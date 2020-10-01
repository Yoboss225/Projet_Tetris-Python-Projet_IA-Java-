package filrouge;
import java.util.ArrayList;
import java.util.HashMap;

public class MaxSpanConstraint implements Constraint{

	protected ArrayList<Activity> listAct;
	protected int dureeMax;

	public MaxSpanConstraint(ArrayList<Activity> listAct,int dureeMax){

		this.listAct = listAct;
		this.dureeMax = dureeMax*60;
}


	public boolean isSatisfiedBySchedule(HashMap<Activity, Integer> prog){

		int minVal = 100000;
		int maxVal = 0;
		
		for(Activity act: this.listAct){
        	
        	if(prog.get(act)*60< minVal)
        		minVal = prog.get(act)*60;
       
			}

		
		for(Activity act: this.listAct){
        	
        	if(prog.get(act)*60> maxVal)
        		maxVal = prog.get(act)*60+act.getTimeInMinutes();
       
			}


		int totalT = maxVal - minVal;

		if (totalT>this.dureeMax){
			System.out.println("La contrainte n'est pas respectee"+totalT+">"+this.dureeMax); 
			return false;
			
		}

		else{

			System.out.println("La contrainte est respectee  "); 
			return true;
		}
		
	}


}


