
# 1)შექმენით 2 ცვლადი number1 და number2 , ამ ცვლადებში შეინახეთ შესაბამისი მნიშვნელობები და ამ ორი ცვლადის გამოყენებით გააკეთეთ მათემატიკური ოპერაციები, დღევანდელ გკვეთილზე ნასწავლი მათემატიკური ოპერატორებით.

# 2)შექმენით ორი ცვლადი birth_year(დაბადების წელი) და current_year(ახლანდელი წელი) შიგნით შეინახე შესაბამისი მნიშვნლობები შენი დაბადების წელი და ახლანდელი წელი, შემდეგ შექმნი მე3 ცვლადი age-სადაც გამოითვლი შენს ასაკს , ზემოთხსენებული ცვლადბის დახმარებით 

# 3)შექმენი 5 ცვლადი , number1 number2 ...number5 შეინახე შიგნით შესაბამისი მნიშვნელობები და გამოითვალე მათი საშუალო არითმეტიკული ,საბოლოო, მიღებული შედეგი გამოიტანეთ ტერმინალში (საშუალო არითმეტიკული => მონაცემების ჯამი გაყოფილი მონაცემების რაოდენობაზე).

# 4)კომენტარების გამოყენებით, თქვენი სიტყვებით ახსენით რას ნიშნავს დეკლარაცია , ინიციალიზება  და რეინიციალიზება , ასევე მოიყვანეთ მაგალითები

# 5)კომენტარების გამოყენებით ახსენით თქვენი სიტყვებით რას ნიშნავს კონკატენაცია(concatenation)

# 6)აუცილებლად უყურეთ ჩანაწერს ხელმეორედ ,ყურადღებით

# 7)ახსენით თქვენი სიტყვებით რას ნიშნავს debugging
number1 = 30
number2 = 50

print(number1 + number2)
print(number1 - number2)
print(number1 * number2)
print(number1 % number2)
print(number1 / number2)
print(number1 // number2)


#hw02

birth_year = 2014
current_year = 2026
age = current_year - birth_year
print(age)


#hw03
#sasualo aritmetikuli aris yvela ricxvi unda seikribos da am yvela ricxvis jami unda gaiyos tu ramdeni cali ricxvi gvaqvs anu mat raodenobaze
number1 = 10
number2 = 20
number3 = 30
number4 = 50
number5 = 100
jami = number1 + number2 + number3 + number4 + number5
print(jami/5)


#hw04

#declaracia nisnavs cvladis seqmnas
#inicilarecia nisnavs cvladsi raimes senaxvas 
#reincilarizeba cvladis mnisvnelobis secvla sxva mnismnelobiut
name = "gabo"
name = "gabi"
name = "nika"
print(name)


#hw5

#konkatinacia aris stringebis damateba
print("gabi"+ "oqropiridze")
print("5"+"10")

#hw07

#debadingi aris kodis secdomebisgan anu errorebisgan ganwmenda 