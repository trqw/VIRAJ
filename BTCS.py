




import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

match_data=pd.read_csv("C:/Users/Dell/Downloads/deliveries/matches.csv")

match_data.head(10)

match_data.isnull().sum()

match_data['season'].unique()

max(match_data['win_by_runs'])

print('Match won by the maximum margin of runs',match_data.iloc[match_data['win_by_runs'].idxmax()])

print('Matches won by maximum no. of wickets:',match_data.iloc[match_data['win_by_wickets'].idxmax()])

print("Matches won by maximum margin of runs",match_data.iloc[match_data[match_data['win_by_runs'].ge(1)].win_by_runs.idxmin()])

print('Number of matches win by minimum wickets',match_data.iloc[match_data[match_data['win_by_wickets'].ge(1)].win_by_wickets.idxmin()])

print('Matches where D/L method was and wasn\'t applied:', match_data['dl_applied'].value_counts())

print( '% of matches with and without D/L method (0 for no D/L and 1 for D/L method applied',round(match_data['dl_applied'].value_counts()/match_data['dl_applied'].count()*100, 2))


plt.figure(figsize=(10, 8)) 
sns.set(style="whitegrid")  
ax = sns.countplot(y='city', data=match_data, palette="coolwarm")
plt.title('No. of Matches Held in Each City\n', fontsize=16, fontweight='bold')
plt.xlabel('\nNo. of Matches Held', fontsize=14)
plt.ylabel('Cities\n', fontsize=14)
plt.xlim([0, 120])
for container in ax.containers:
    ax.bar_label(container, padding=5, fmt='%d', fontsize=10, color='black')
plt.tight_layout()  
plt.show()



print('Number of Matches won by each team:',match_data['winner'].value_counts())



data = match_data['winner'].value_counts()
plt.figure(figsize=(12, 8))
sns.set(style="whitegrid")
ax = sns.barplot(y=data.index, x=data, palette="viridis", orient='h')
plt.title('No. of Matches Won by Each Team\n', fontsize=16, fontweight='bold')
plt.xlabel("\nNo. of Matches Won", fontsize=14)
plt.ylabel('Teams\n', fontsize=14)
ax.set_xlim([0, 120])
for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=5, fontsize=12, color='black')
plt.tight_layout()
plt.show()



plt.figure(figsize=(10, 6))
sns.set(style="whitegrid")
ax = sns.countplot(x='season', data=match_data, palette="coolwarm")
plt.title('No. of Matches Held Every Season\n', fontsize=16, fontweight='bold')
plt.xlabel('\nSeason', fontsize=14)
plt.ylabel('No. of Matches Held\n', fontsize=14)
for container in ax.containers:
    ax.bar_label(container, fmt='%d', padding=3, fontsize=10, color='black')
ax.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()



print('Picking the top 10 players based on the number of Man of the Match (MOM) awards won')
mom= match_data['player_of_match'].value_counts()[:10]
print(mom)


sns.set_theme(style="whitegrid")
fig, ax = plt.subplots(figsize=(10, 6))  
ax.set_ylim([0, 28])  # Set y-axis limit
ax.set_title("Top 10 players based on no. of MOM awards won\n", fontsize=16)  
sns.barplot(x=mom.index, y=mom, orient='v', palette="Blues_d", ax=ax)  
plt.ylabel("No. of MOM awards won\n", fontsize=14)
plt.xlabel("\nPlayers", fontsize=14)
plt.tight_layout()  
plt.show()



print(' Does winning the toss mean winning the match?')
winnerwinner=match_data['toss_winner']== match_data['winner']
winnerwinner.groupby(winnerwinner).size()




round(winnerwinner.groupby(winnerwinner).size() / winnerwinner.count() * 100,2)


print('How many times did the captain choose fielding and batting after winning the toss?',match_data['toss_decision'].value_counts())

print('Different results for games',match_data['result'].value_counts())

print(' How many times did each team win the toss?',match_data['toss_winner'].value_counts())



# Plot to visualise the no. of tosses won by each team
toss = match_data['toss_winner'].value_counts()
plt.figure(figsize=(12, 8))  
sns.set_theme(style="whitegrid")
sns.barplot(y=toss.index, x=toss, palette="magma")  
plt.title("Number of Tosses Won by Each Team", fontsize=16, weight='bold', pad=20)
plt.xlabel("Number of Tosses Won", fontsize=14)
plt.ylabel("Teams", fontsize=14)
sns.barplot(y=toss.index, x=toss, orient='h', palette="magma", ax=ax)
for p in ax.patches:
    ax.annotate(f"{p.get_width()}", (p.get_width(), p.get_y() + p.get_height() / 2),
                ha='left', va='center', fontsize=12, color="black", xytext=(5, 0),
                textcoords="offset points")
sns.despine(left=True, bottom=True)
plt.tight_layout()  
plt.show()




print(' Best venue for defending your total',match_data.venue[match_data.win_by_runs!=0].mode())


print(' Best venue to chase a total',match_data.venue[match_data.win_by_wickets!=0].mode())


print(' Best defending team',match_data.winner[match_data.win_by_runs!=0].mode())



print(' Best chasing team',match_data.winner[match_data.win_by_wickets!=0].mode())



# No. of matches played in different stadiums
plt.figure(figsize=(10, 14))  
sns.set_theme(style="whitegrid")
sns.countplot(y="venue", data=match_data, palette="viridis", order=match_data['venue'].value_counts().index)
plt.title("Number of Matches Played in Different Stadiums", fontsize=16, weight='bold')
plt.xlabel("Number of Matches Played", fontsize=14)
plt.ylabel("Stadiums", fontsize=14)
plt.xticks(fontsize=12)
plt.yticks(fontsize=10)
plt.tight_layout()
plt.show()
