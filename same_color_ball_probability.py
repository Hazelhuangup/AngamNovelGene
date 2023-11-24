
# Total number of black balls
total_black_balls = 1000

# Total number of white balls
total_white_balls = 500

# Total number of balls in the pool
total_balls = total_black_balls + total_white_balls

# Probability of drawing a black ball
probability_black = total_black_balls / total_balls

# Probability of drawing a white ball
probability_white = total_white_balls / total_balls

# Probability of drawing two black balls
probability_two_black = probability_black * (total_black_balls - 1) / (total_balls - 1)

# Probability of drawing two white balls
probability_two_white = probability_white * (total_white_balls - 1) / (total_balls - 1)

# Probability of drawing two balls of the same color
probability_same_color = probability_two_black + probability_two_white

print("Probability of drawing two balls of the same color:", probability_same_color)
