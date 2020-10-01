package init;

import java.util.ArrayList;

public class State {

	protected int n; // nombre de lignes
	protected int m; // nombre de colonnes
	protected int player; // défini le joueur qui joue
	protected int[][] board;

	public State(int m, int n) {
		this.n = n;
		this.m = m;
		this.player = 1;
		this.board = new int[this.m][this.n];
	}

	public State(State state) {
		this(state.m, state.n);
		for (int i = 0; i < this.m; i++) {
			for (int j = 0; j < this.n; j++) {
				this.board[i][j] = state.board[i][j];
			}
		}
	}

	public void afficherGrille() {
		for (int i = 0; i < this.m; i++) {
			// System.out.print("__");
			// System.out.print("|");
			for (int j = 0; j < this.n; j++) {
				// System.out.print("__");
				System.out.print(this.board[i][j] + " ");
				// System.out.print("__");
			}
			System.out.print("\n");
		}
	}

	public void initializePosition() {
		this.board[0][0] = 1;
		this.board[this.m - 1][this.n - 1] = 2;
	}

	public int getPlayer(){
		return this.player;
	}

	public float getScore(int joueur) {
		float pionJ = 0;
		float pionT = 0;
		for (int i = 0; i < this.m; i++) {
			for (int j = 0; j < this.n; j++) {
				if (this.board[i][j] != 0) {
					if (this.board[i][j] == joueur) {
						pionJ = pionJ + 1;
					}
					pionT++;
				}
			}
		}
		return pionJ / pionT;
	}

	/**
	 * Si le jeu est terminé, il n'y a plus de mouvements possibles pour un des deux
	 * joueurs.
	 */
	public boolean isFinished() {
		if (this.getMoves(1).isEmpty() || this.getMoves(2).isEmpty()) {
			System.out.println("plus de mouvement possible");
			return true;
		} else {
			return false;
		}
	}

	public ArrayList<Move> getMoves(int joueur) {
		ArrayList<Move> move = new ArrayList<Move>();
		for (int i = 0; i < this.m; i++) {
			for (int j = 0; j < this.n; j++) {
				if (this.board[i][j] == joueur) {
					// bas 2 cases
					if (i < this.m - 2 && this.board[i + 2][j] == 0) {
						move.add(new Move(i, j, i + 2, j, true));
					}
					// droite 2 cases
					if (j < this.n - 2 && this.board[i][j + 2] == 0) {
						move.add(new Move(i, j, i, j + 2, true));
					}
					// haut 2 cases
					if (i > 2 && this.board[i - 2][j] == 0) {
						move.add(new Move(i, j, i - 2, j, true));
					}
					// gauche 2 cases
					if (j > 2 && this.board[i][j - 2] == 0) {
						move.add(new Move(i, j, i, j - 2, true));

					}

					// DUPLICATION
					// bas 1 case
					if (i < this.m - 1 && this.board[i + 1][j] == 0) {
						move.add(new Move(i, j, i + 1, j, false));
					}
					// droite 1 case
					if (j < this.n - 1 && this.board[i][j + 1] == 0) {
						move.add(new Move(i, j, i, j + 1, false));
					}
					// haut 1 case
					if (i > 1 && this.board[i - 1][j] == 0) {
						move.add(new Move(i, j, i - 1, j, false));
					}
					// gauche 1 case
					if (j > 1 && this.board[i][j - 1] == 0) {
						move.add(new Move(i, j, i, j - 1, false));
					}
				}
			}
		}
		return move;
	}

	public State play(Move mv) {
		// int xdebut,int ydebut,int xfin,int yfin,boolean action

		State nv = new State(this);
		int couleurE = this.player == 1 ? 2 : 1;
		nv.board[mv.xfin][mv.yfin] = this.player;
		nv.player = couleurE;

		// DEPLACEMENT
		if (mv.action == true) {
			nv.board[mv.xdebut][mv.ydebut] = 0;
		} else {
			// bas
			if (mv.xfin < this.m - 1 && this.board[mv.xfin + 1][mv.yfin] == couleurE) {
				nv.board[mv.xfin + 1][mv.yfin] = this.player;
			}
			// droite
			else if (mv.yfin < this.n - 1 && this.board[mv.xfin][mv.yfin + 1] == couleurE) {
				nv.board[mv.xfin][mv.yfin + 1] = this.player;
			}
			// haut
			else if (mv.xfin > 1 && this.board[mv.xfin - 1][mv.yfin] == couleurE) {
				nv.board[mv.xfin - 1][mv.yfin] = this.player;
			}
			// gauche
			else if (mv.yfin > 1 && this.board[mv.xfin][mv.yfin - 1] == couleurE) {
				nv.board[mv.xfin][mv.yfin - 1] = this.player;
			}
		}
		return nv;
	}
	
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

}