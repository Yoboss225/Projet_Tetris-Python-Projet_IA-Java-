package filrouge;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.random;
import java.util.Calendar;

public class RandomScheduler
{

protected Set<Activity> activities;
protected List<Constraint> constraints;
protected Random randomGenerator; 

	public RandomScheduler(/*Set<Activity> activities,List<Constraint> constraints,java.util.Random randomGenerator)*/)
	{

		this.activities = new HashSet<>();//activities;
		this.constraints = new ArrayList<>(); //constraints;
		this.randomGenerator = new Random();//INITIALISATION ???
	}

	public void add(Activity act)
	{

		this.activities.add(act);

	}

	

	public void add(Constraint ct)
	{

		this.constraints.add(ct);
	}

	


	public Map<Activity,Calendar> generateur()  //""""""""""
	{
		
		Random x = new Random();
		int heure = valeurMin + x.nextInt(25)

		Random y = new Random();
		int minute = valeurMin + y.nextInt(60)

		Random z = new Random();
		
		int seconde = valeurMin + z.nextInt(60)
		
		Map<Activity, Calendar> hm = new HashMap<>();
		
		GregorianCalendar date = new GregorianCalendar(2019,1,1,heure,minute,seconde);
		
		for(Activity i: this.activities)
		{
			for (Calendar x : date ) 
			{
				hm.put(i,x);	
			}
			
		}

		
		return hm;		

		
		
		
		
		

	}

	
//on compte le nombre de contrainte dans une liste de contraintes 
	public int comptConstraint(Map<Activity,Calendar> ept)
	{
		int cpt = 0;
		for(Constraint ct : this.listConst)
		{
			if (!ct.isSatisfiedBySchedule(ept))
			{
				return false;
				cpt = cpt;
				System.out.println("aucune des contraintes n'est satisfaite");

			}
		
		}
		return true;
		cpt = cpt+1;
		return System.out.println("il y'a "+ct+"contraintes qui sont satisfaite(s)");

		return cpt;
	}
	
/*	
	public Map<Activity,Calendar> choixEpt(int n)
	{
		int max= 0;
		

		Scanner nbr = new Scanner(System.in);
    	System.out.println("combien d'emploi du temps voulez vous tirer ? ");
    	n = nbr.nextInt();
		
		//Map<Activity, Calendar> ept = new HashMap<>();	
		Map<Activity,Calendar> ept = ept.generateur();

		Map<Activity,Calendar> ens = n*ept;
		int cmptr = 0;

    	/*for(int j = 0;j<=n;j++)
    	{
    	
    	//Map<Activity,Calendar> ept = j*generateur();
    	
    	}
    	//int compteur = this.constraints.comptConstraint(ept);

		*/
		//for(int i=0;i>=max;i++)
		//{
			
/*
			for (Map<Activity,Calendar> v : ens )
			{
				if (v.isSatisfiedBySchedule()) 
				{
						cmptr=cmptr+1;
				}	
			
				if (comptConstraint(v)>compteur) 
				{
					v=compteur;

					return ept(v);
				}

				return ept;
		//}
			}
	}
*/
}