
class MinimaxAgent:
    def __init__(self, depth):
        self.depth = depth

    def evaluate(self, game, player):
        opp = -player
        
        b_score, w_score = game.score()
        our_pieces = b_score if player == 1 else w_score
        opp_pieces = w_score if player == 1 else b_score
        piece_diff = our_pieces - opp_pieces
        
        our_moves = len(game.get_valid_moves(player))
        opp_moves = len(game.get_valid_moves(opp))
        mobility_diff = our_moves - opp_moves
        
        position_score = 0
        size = game.size
        
        corners = [(0, 0), (0, size - 1), (size - 1, 0), (size - 1, size - 1)]
        
        for r in range(size):
            for c in range(size):
                if game.board[r][c] == 0:
                    continue
                
                weight = 1  
                
                is_row_edge = (r == 0 or r == size - 1)
                is_col_edge = (c == 0 or c == size - 1)
                is_row_near_edge = (r == 1 or r == size - 2)
                is_col_near_edge = (c == 1 or c == size - 2)
                
                if is_row_edge and is_col_edge:
                    weight = 100  
                elif is_row_near_edge and is_col_near_edge:
                    
                    corner_r = 0 if r == 1 else size - 1
                    corner_c = 0 if c == 1 else size - 1
                    if game.board[corner_r][corner_c] == 0:
                        weight = -25
                    else:
                        weight = 5
                elif (is_row_edge and is_col_near_edge) or (is_col_edge and is_row_near_edge):
                    
                    corner_r = 0 if r in (0, 1) else size - 1
                    corner_c = 0 if c in (0, 1) else size - 1
                    if game.board[corner_r][corner_c] == 0:
                        weight = -10
                    else:
                        weight = 5
                elif is_row_edge or is_col_edge:
                    weight = 8  
                
                if game.board[r][c] == player:
                    position_score += weight
                else:
                    position_score -= weight

        total_cells = size * size
        filled_cells = our_pieces + opp_pieces
        fill_percentage = filled_cells / total_cells
        
        if fill_percentage < 0.35:  
            w_piece = -5
            w_mobility = 20
            w_position = 15
            
        elif fill_percentage < 0.75:  
            w_piece = 2
            w_mobility = 12
            w_position = 30
            
        else:  
            w_piece = 50
            w_mobility = 5
            w_position = 8

        return (w_piece * piece_diff) + (w_mobility * mobility_diff) + (w_position * position_score)
        

    def minimax(self, game, depth, maximizing, root_player):
        
        if depth == 0 or game.game_over():
            return self.evaluate(game, root_player), None
        
        current_player = root_player if maximizing else -root_player
        
        valid_moves = game.get_valid_moves(current_player)
        
        if not valid_moves:
            next_maximizing = not maximizing
            return self.minimax(game, depth - 1, next_maximizing, root_player)[0], None
        
        best_move = None
        
        if maximizing:
            max_eval = float('-inf')
            
            for move in valid_moves:
                next_game = game.copy()
                
                next_game.make_move(current_player, *move)
                
                evaluation, _ = self.minimax(next_game, depth - 1, False, root_player)
                
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
            
            return max_eval, best_move
        
        else:
            min_eval = float('inf')
            
            for move in valid_moves:
                next_game = game.copy()
                
                next_game.make_move(current_player, *move)
                
                evaluation, _ = self.minimax(next_game, depth - 1, True, root_player)
                
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
            
            return min_eval, best_move

    def choose_move(self, game, player):
        value, move = self.minimax(game, self.depth, True, player)
        return move
