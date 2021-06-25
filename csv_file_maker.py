import pandas as pd

########################## creating assignment Dataframe ##############################

assignment = {'user_name': [],
              'assignment_no': [],
              'no_of_problems': [],
              'no_of_solved_problems': [],
              'score': [],
              'total_score': [],
              'remarks': []
              }
assignment_df = pd.DataFrame(assignment)
assignment_df.to_csv('assignments.csv', index=False)


########################## creating coding challenge dataframe ##############################

coding = {'user_name': [],
          'coding_challenge_no': [],
          'no_of_problems': [],
          'no_of_solved_problems': [],
          'score': [],
          'total_score': [],
          'remarks': []
          }
coding_challenges = pd.DataFrame(coding)
coding_challenges.to_csv('coding_challenges.csv', index=False)

########################## creating coding challenge dataframe ##############################

usernames = {'user_name': ['grohit0303']}
usernames_df = pd.DataFrame(usernames)
usernames_df.to_csv('usernames_data.csv', index=False)