package init;

public class Move {

	protected int xdebut;
	protected int ydebut;
	protected int xfin;
	protected int yfin;
	protected boolean action;

	public Move(int xdebut, int ydebut, int xfin, int yfin, boolean action) {

		this.xdebut = xdebut;
		this.ydebut = ydebut;
		this.xfin = xfin;
		this.yfin = yfin;
		this.action = action;

	}
	
	@Override
	public String toString() {
		return "Move [xdebut=" + xdebut + ", ydebut=" + ydebut + ", xfin=" + xfin + ", yfin=" + yfin + ", action="
				+ action + "]";
	}
}
