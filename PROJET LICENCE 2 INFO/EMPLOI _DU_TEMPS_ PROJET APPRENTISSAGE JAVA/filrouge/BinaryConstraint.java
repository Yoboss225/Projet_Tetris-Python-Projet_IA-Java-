package filrouge;

public abstract class BinaryConstraint{

	protected Activity first;
	protected Activity second;

	public BinaryConstraint(Activity first, Activity second){

		this.first = first;
		this.second = second;
	}

	public abstract boolean isSatisfied(int date1, int date2);

	

}