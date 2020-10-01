package init;
import java.util.ArrayList;

public class Ia {



protected boolean cut;
protected int player;
protected State state;
protected ArrayList<Move> action; 		
protected int profondeur; 
protected double compteur;

	public Ia(boolean cut,int player,int profondeur){

	this.cut = cut;
	this.player = 1;
	this.profondeur = profondeur;
	this.state = state;
	this.action = this.state.getMoves(this.player);
	this.compteur = compteur;
	}

/*


	public Couple  minMax(State state1,int profondeur){

	float best = 0;
	ArrayList<Move> coup = new ArrayList<Move>();
	Couple jouer = new Couple(best,coup);
	for (Move coups : this.action ) {
		state1 = this.state.play(coups);
		minMax(state1,profondeur-1);
		float m = this.state.getScore(this.player);
		if (m>best) {
			best=m;
			coup.add(coups);
			jouer.bestVal = best;
			jouer.coup = coup;
			
		}

		
		
	}

	return jouer;

	}
*/

	public double minMax(State state,int profondeur){
		
		State nvState = null;
		double b,m;
		if (profondeur ==0) {
			state.afficherGrille();
			return state.getScore(this.player);
		}

		else{
			if (state.getPlayer()==this.player) {
				b=Double.NEGATIVE_INFINITY;
				for (Move coups : state.getMoves(state.getPlayer())) {
					m=minMax(nvState,profondeur-1);
					//nvState = state.play(coups);
					b = b < m ? m: b;
				}
			}
			else{
				b= Double.POSITIVE_INFINITY;
				for (Move coups : state.getMoves(state.getPlayer())) {
					//nvState = state.play(coups);
					m=minMax(nvState,profondeur-1);
					b = b < m ? m: b;

			}
				
		}
			return b;
		}
			
	}
		
		/*

		public ArrayList<Move> decide(State state){

			float best = 0;
			ArrayList<Move> coup = new ArrayList<Move>();
			for (Move coups : this.action ) {
				state = state.play(coups);
				minMax(state,this.profondeur-1);
				float m = this.state.getScore(this.player);
				if (m>best) {
					best = m;
					coup.add(coups);
				}



			}

			return coup;

		}

	*/

		
	}


	






























