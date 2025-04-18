-- Create an index on the tables names and the first letter of name and score
CREATE INDEX idx_name_first_score ON names (name (1), score)