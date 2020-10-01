package init;

import java.util.ArrayList;

public class Start {

	public static void main(String[] args) {

		State state = new State(5, 5);
		state.initializePosition();
		state.afficherGrille();
		//Ia iA = new Ia(false,1,5);
		while (!state.isFinished()) {

			System.out.println();

			int player = state.player;
			state.getScore(player);

			ArrayList<Move> listMove = state.getMoves(player);
					
			int n = (int) (Math.random() * (listMove.size()));
			int m =(int) state.minMax(state,10000);
					
			state = state.play(listMove.get(m));

			try {
				Thread.sleep(2200);
			} catch (InterruptedException e) {
			}

			state.afficherGrille();
		}
		System.out.println("Score, j1 : " + state.getScore(1) + ", j2: " + state.getScore(2));
	}

}