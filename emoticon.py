"""
Given a text string message, complete the function that analyzes the text and reports the overall mood based on the emoticons it contains. :o

🙂 Happy Emoticons

:) → Classic smiley face
:p → Playful / Tongue out
XD → Laughing / Very happy
:3 → Cute / Mischievous (inspiration behind Codédex bot!)
<3 → Heart
\m/ → Rock on
🙁 Sad Emoticons

:( → Frown
:'( → Crying
t(-.-t) → Middle fingers (my personal favorite!)
Each happy emoticon → +1. Each sad emoticon → -1.

Return the final score.

"""
def emoticons_mood(message):
  # Write your code here 💖
  message = message.lower()

  happy = [':)', ':p', 'xd', ':3', '<3', '\\m/', ':o']
  sad = [':(', ":'(", 't(-.-t)']
  
  score = 0
  for emo in happy:
    score += message.count(emo)
  for emo in sad:
    score -= message.count(emo)

  return score

  
