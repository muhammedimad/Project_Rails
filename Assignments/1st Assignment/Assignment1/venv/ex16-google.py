import re
def extract_year(filename):
    f = open(filename, 'r')
    text=f.read()
    index = text.find("<h3 align=\"center\">",0)
    l=text[(index+4):(index+40)]
    year = re.findall("\d+", l)

    if(year==[]):
        return ("no year assigned")
    else:
        year=re.findall("\d+",l)
        # print(year)
    year=year[0].strip("[]")
    return year





def extract_names(filename):
    f= open(filename,'r')
    page = f.read()
    c = []
    male_regex='</td><td>(.*)</td><td>'
    # female_regex = '<[^>]*>'
    rank_regex = "<td>(\d+)</td>"
    males = re.findall(male_regex,page)
    # females = re.sub('<[^>]*>'," ")
    # females = re.findall(female_regex,page)

    rank = re.findall(rank_regex, page)
    index = page.find("</td><td>",0)
    l=page[(index+500):(index+700)]
    # print(females)
    for i in range(len(rank)):
        c.append(males[i]+':'+rank[i])

    return c

    # print(index)
    # print(l)
    # print(results)
    # print(results2)
    # print(temp)


y=extract_year("baby2006.html")
# print(y)
names_and_rank=extract_names("baby2006.html")
# print(names_and_rank)
names_and_rank.insert(0,y)
sorted_names=sorted(names_and_rank)
print(names_and_rank)
print(sorted_names)





