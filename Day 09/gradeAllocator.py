scores = {
    'adarsh' : 89,
    'amul' : 98,
    'mangesh' : 20,
    'vidya' :55,
    'shree' :68,
    'ganesh' : 78
}

for key in scores.keys():
    if scores[key] > 90:
        scores[key] = "Outstanding"
    elif scores[key] > 80:
        scores[key] = "Exceeds expectations"
    elif scores[key] > 70:
        scores[key] = "Acceptable"
    elif scores[key] <= 70:
        scores[key] = "Fail"
    else:
        print("invalid value in found")
print(scores)
