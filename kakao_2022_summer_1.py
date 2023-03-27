'''

kakao 2022 summer intern test

https://tech.kakao.com/2022/07/13/2022-coding-test-summer-internship/

Problem 1

Build a personality test according to four different indicators:

indicator 1: Ryan-type or Tube-type
indicator 2: Con-type or Frodo-type
indicator 3: Jay-G-type or Muzi-type
indicator 4: Apeach-type or Neo-type

Combinations of these indicators leads to 16 possible personality types (2 x 2 x 2 x 2), such as RCJA, TCJA, RFMN or TFJA. 

Each survey question will ask if they are NOT like the personality indicator, for example:

"Are you NOT a Ryan-type personality?"

Survey choices are given by a number between 1 to 7 depending on responses.

1 - Strongly disagree  -> 3
2 - Disagree           -> 2
3 - Partly disagree    -> 1
4 - Don't know         -> 0
5 - Partly agree       -> 1
6 - Agree              -> 2
7 - Strongly agree     -> 3

Survey responses are converted to personality scores by assigning a value between 1 to 3 to one of the indicator pairs depending on survey responses. As questions are worded in the negative, responses that disagree with personality indicator in the question are assigned personality scores to the current indicator and responses that agree are assigned personality scores to the opposite indicator according to the scale above. Final personality types are determined by the higher score between indicators pairs and if scores are a tie then the first indicator of the pair is given as the personality indicator. The first indicator of the pair of indicators is used in the personality type if personality scores are zero.

Examples:
R: 0    T: 2 -> T
C: 1    F: 1 -> C
J: 3    M: 0 -> J
A: 0    N: 0 -> A

Answer: TCJA

'''

survey_1 = ['AN', 'CF', 'MJ', 'RT', 'NA']
survey_2 = ['TR', 'RT', 'TR']
choice_1 = [5, 3, 2, 7, 5]
choice_2 = [7, 1, 3]

check = {
'R':0,
'T':0,
'C':0,
'F':0,
'J':0,
'M':0,
'A':0,
'N':0
}

def solution(survey, choice):
    answer = ''
    count = 0
    for personality in survey:
        if choice[count] < 4:
            check[personality[0]] = abs(choice[count]-4)
        elif choice[count] > 4:
            check[personality[1]] = choice[count]%4
        else:
            check[personality[0]] = 0
        count += 1
    
    if check['R'] >= check['T'] or (check['R'] and check['T'] == 0):
        answer += 'R'
    elif check['R'] < check['T']:
        answer += 'T'
    if check['C'] >= check['F'] or (check['C'] and check['F'] == 0):
        answer += 'C'
    elif check['C'] < check['F']:
        answer += 'F'
    if check['J'] >= check['M'] or (check['J'] and check['M'] == 0):
        answer += 'J'
    elif check['J'] < check['M']:
        answer += 'M'
    if check['A'] >= check['N'] or (check['A'] and check['N'] == 0):
        answer += 'A'
    elif check['A'] < check['N']:
        answer += 'N'
    
    return answer

print("\n***** kakao_2022_1_summer *****\n")
solution = solution(survey_1, choice_1)
print(solution)