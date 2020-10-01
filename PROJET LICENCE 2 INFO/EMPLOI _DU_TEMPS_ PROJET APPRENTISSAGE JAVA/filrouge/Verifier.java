package filrouge;
import java.util.ArrayList;
import java.util.HashMap;

public class Verifier{


	protected ArrayList<Constraint> listConst;

	public Verifier()
	{

		this.listConst = new ArrayList<>();
	}

	public void addObject(Constraint element)
	{

		this.listConst.add(element);
	}

	
	public boolean verify(HashMap<Activity, Integer> prog)

	{

		

		for(Constraint ct : this.listConst)
		{
			if (!ct.isSatisfiedBySchedule(prog))
			{
				return false;
			}
		
		}
		return true;
	}

}