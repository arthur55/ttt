score1 = int ( input ("請輸入第一次成績") )
score2 = int ( input ("請輸入第二次成績") )
score3 = int ( input ("請輸入第三次成績") )
score = [score1 , score2 , score3]
score.sort ()
print (score[0]*0.2+score[1]*0.3+score[2]*0.5)