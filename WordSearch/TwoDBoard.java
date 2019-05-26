/**
* The TwoDBoard program implements an application for 
* a given 2D board and a word, to find if the word exists in the grid.
*
* @author  Kalyani
* @version 1.0
* @since   2019-05-25 
*/

public class TwoDBoard {
	
	public boolean existWord(char[][] board, String word) {
		if (board.length == 0 || board[0].length == 0) 
			return false;
		int lenX = board.length;
    		int lenY = board[0].length;
    		boolean[][] visited = new boolean[lenX][lenY];

		for (int i = 0; i < lenX; i++) {
			for (int j = 0; j < lenY; j++) {
			if (searchWord(board, visited, word.toCharArray(), 0, i, j)) {
				return true;   				 
			}
			}
		}
		return false;
	}
	
	//to search word in the 2D Board 	
	private boolean searchWord(char[][] board, boolean[][] visited, char[] word, int wordIndex, int x, int y) {
		if (visited[x][y] == true) {
			return false;
		}
		if (board[x][y] != word[wordIndex]) {
			return false;
		}
		if (wordIndex == word.length - 1) {
			return true;
		}
		visited[x][y] = true;

		if (x > 0 && searchWord(board, visited, word, wordIndex + 1, x - 1, y)) {
			return true;
		}
		if (x < board.length - 1 && searchWord(board, visited, word, wordIndex + 1, x + 1, y)) {
			return true;
		}
		if (y > 0 && searchWord(board, visited, word, wordIndex + 1, x, y - 1)) {
			return true;
		}
		if (y < board[0].length - 1 && searchWord(board, visited, word, wordIndex + 1, x, y + 1)) {
			return true;
		}
		visited[x][y] = false;
		return false;
	}
	
	//to print a 2D Board
    	public String printBoard(char[][] board) {
		  int ROW = board.length, COL = board[0].length;
		  for (int i = 0; i < ROW; i++) {
			   System.out.println();
			   for (int j = 0; j < COL; j++) {
					System.out.print(board[i][j] + " ");
			   }
		  }
		  return "\n ROW=" + ROW + ", COL=" + COL;
    	}

	//main method 
   	public static void main(String[] args) {
		TwoDBoard tdb=new TwoDBoard();
		char[][] board = { 	{ 'A', 'B', 'C', 'E' },
					{ 'S', 'F', 'C', 'S' },
					{ 'A', 'D', 'E', 'E' } };
		String word = "SEE";
		
		System.out.println("The given TwoD Board is:");
		tdb.printBoard(board);
		
		System.out.println("\nThe word is: "+word+ "====>"+tdb.existWord(board,word));
	}
}

