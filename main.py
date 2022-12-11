# -------------------------------    NESNE YÖNELİMLİ TASARIM VE ANALİZ PROJE ÖDEVİ    ---------------------------------------#
# --------------------------------------------    GIZEM TUNCER    -----------------------------------------------------------#
# --------------------------------------------    Y210240060    -------------------------------------------------------------#






from question_model import Question,MultiChoice



# print("-------------------------")

# text = input("Soru Yazınız!")
# cevap = input("Cevap Yazınız!")
# score = input("Scorunu belirleyiniz!")
# level = input("Level Yazınız!")

# q5 = Question(text, level, score, level)
# new = list.append(q5)
# print("EklendiYeni!")
# print("İndex :{list[index]}")


# -------------------------------    START    ---------------------------------------#

q1 = Question("İnternet üzerinden görüntülü konuşma amacıyla kullanılan bilgisayar donanımı aşağıdakilerden hangisidir?",
              "Cevap Cevap ", "10", "3")
q2 = Question("Soru",   "Cevap Cevap", "10", "3")
q3 = Question("Soru",   "Cevap3", "10", "3")
q4 = Question("Soru3",   "Cevap3", "10", "3")
q5 = Question("Soru3",   "Cevap", "10", "3")
q6 = Question("Soru3",   "Cevap3", "10", "3")
q7 = Question("Soru3",   "Cevap3", "10", "3")
q8 = Question("Soru3",   "Cevap3", "10", "3")
q9 = Question("Soru3",   "Cevap3", "10", "3")
q10 = Question("Soru3",   "Cevap3", "10", "3")

list_2 = [q1, q2, q3, q4, q5, q6, q7, q7, q8, q9, q10]
print(list_2.index)
# =============== Çoktan Seçmeli Soru Tipleri için===========================================================================#

q1 = MultiChoice("İnternet üzerinden görüntülü konuşma amacıyla kullanılan bilgisayar donanımı aşağıdakilerden hangisidir?",
                 "b", "10", "2", "a-Tarayıcı b-Web Kamerası c-Yazıcı d-Ekran")

q2 = MultiChoice("Bilgisayarın elle tutulabilen ve gözle görülebilen kısımlarına ne ad verilir?",
                 "a", "5", "1", "a-Donanım b-Sistem Yazılımı c-Uygulama Yazılımı d-Donatım")

q3 = MultiChoice("Aşağıdaki yazılımlardan hangisi sistem yazılımıdır?",
                 "d", "10", "2", "a- Google Chrome b-Paint c-Avira Antivirüs d-Windows 8")

q4 = MultiChoice("Bilgisayardaki tüm işlemlerin yapıldığı dahili donanım birimi hangisidir?",
                 "c", "5", "1", "a- Anakart b-Ram c-İşlemci d-Sabit Disk")

q5 = MultiChoice("Bilgisayarın çalışma hızını belirleyen donanım birimleri hangileridir? I. Anakart II. Ram III. İşlemci IV. Güç Kaynağı",
                 "c", "20", "3", "a-I-II b-I-III c-II-III d-III-IV")

q6 = MultiChoice("Aşağıdakilerden hangisi dahili donanım birimidir?",
                 "b", "10", "2", "a-Kasa b-Anakart c-Ekran d-Tarayıcı")

q7 = MultiChoice("Aşağıdaki uygulama yazılımlarından hangisi yanlış eşleştirilmiştir?",
                 "d", "5", "1", "a-Eset Nod 32 - Antivirüs Yazılımı b-Mozilla Firefox - İnternet Tarayıcısı c-Paint - Resim Programı d-Microsoft Word - Sunum Programı")

q8 = MultiChoice("İnternete bağlanmamızı sağlayan donanım birimi aşağıdakilerden hangisidir?",
                 "a", "5", "1", "a-Modem b-Anakart c-İşlemci d-Ses Kartı")

q9 = MultiChoice("Müzik dinlemek için kullandığımız uygulama yazılımı aşağıdakilerden hangisidir?",
                 "d", "10", "2", "a-Paint b-Microsoft Powerpaint c-Avira d-Winamp")

q10 = MultiChoice("Aşağıdakilerden hangisi bir sistem yazılımıdır?",
                  "c", "10", "2", "a-Google Chrome b-İnternet Explorer c-Windows XP d-Adobe Photoshop")

list_1 = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]


q1 = Question("Bilgisayardaki tüm bilgilerimizin kalıcı olarak depolandığı donanım birimi hangisidir?",
              "Sabit Disk", "20", "3")
q2 = Question("2-Yazılım nedir?",
              "Donanım ile kullanıcı arasındaki iletişimi kuran ve donanımı kontrol eden programlar", "10", "2")
q3 = Question(""" ………………… bilgisayardaki tüm donanım elemanları arasındaki iletişimi sağlar, bazı donanım elemanları ..................üzerinde yer alır; bazı donanım elemanları ise...................... kablolarla bağlıdır.
              İfadesinde noktalı olan yerlere aşağıdakilerden hangisi gelmelidir?""",   "Anakart", "10", "2")
q4 = Question("Tarayıcının işlevi nedir?",
              "Kâğıttaki bilgileri bilgisayara aktarmak", "10", "2")
q5 = Question("Derleme nedir",
              "Bilgisayarda bir programlama dili kullanılarak program yazılması", "20", "3")
q6 = Question("Geniş alan ağı (WAN) nedir?",
              "Aralarında ağ kurulu bir grup bilgisayarın fiziksel görünümü", "10", "3")
q7 = Question(
    "Python bir programlama dilidir. Lütfen doğru veya yanlış yazınız?", "Doğru", "10", "3")
q8 = Question(
    "2 GB kaç 2048 MB eder. Lütfen doğru veya yanlış yazınız?",   "Doğru", "5", "1")
q9 = Question("Veri iletmek ve bilgisayar kaynaklarını ortak kullanmak amacıyla birden fazla bilgisayarın birbirine bağlanmasına ……………………. denir.İfadesinde noktalı olan yerlere aşağıdakilerden hangisi gelmelidir?",   "Ağ", "10", "3")
q10 = Question(
    "Kızdırma Virüsleri bir virüs türüdür. Lütfen doğru veya yanlış yazınız?",   "Yanlış", "5", "1")

list_2 = [q1, q2, q3, q4, q5, q6, q7, q7, q8, q9, q10]

# # -------------------   SORU EKLEME START  -----------------------------------------------------------------------#
# question_type = input("Eklemek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! 1-Çoktan Seçmeli 2-Klasik 3-Dogru Yanlış 4-Boşluk Doldurma")
# if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
#     num = int(input('Kaç adet soru eklemek istiyorsunuz: '))
#     i = 0
#     while(i<num):
#         if question_type == "1":
#             text = input("Soru Textinizi Yazınız!")
#             answer = input("Cevap Textinizi Yazınız!")
#             score = input("Lütfen bu soru için puan belirleyiniz!")
#             level = input("Lütfen bu soru için 1'den 3'e kadar seviye belirleyiniz.Örneğin; 1")
#             choice = input("Lütfen seçeneklerinizi belirleyin. Örnek olarak; a-Soru Şıkkı b-Soru Şıkkı c-Soru Şıkkı d-Soru Şıkkı")
#             new = MultiChoice(text,answer,score,level,choice )
#             list_1.append(new)
#             i += 1
#         elif question_type == "1" or "2" or "3":
#             text = input("Soru Textinizi Yazınız!")
#             answer = input("Cevap Textinizi Yazınız!")
#             score = input("Lütfen bu soru için puan belirleyiniz!")
#             level = input("Lütfen bu soru için 1'den 3'e kadar seviye belirleyiniz.Örneğin; 1")
#             new = Question(text,answer, score,level )
#             list_2.append(new)
#             i += 1

#         print("EklendiYeni!")
#         print("--------------")
# else:
#     print("Lütfen belirtilen şıklardan birinin numarasını yazınız!")


# # -------------------   SORU EKLEME END -----------------------------------------------------------------------#


# for i in range(len(list)):
#     print("list listesinde")
#     print(list[i].text , list[i].answer, list[i].score, list[i].level)
# print("--------------")


# q1 = Question("Soru1",   "Cevap1", "10" ,"3"   )
# q2 = Question("Soru2",   "Cevap2", "10" ,"3"   )
# q3 = Question("Soru3",   "Cevap3", "10" ,"3"   )

# ----------------------------------------      Start    -------------------------------------#


# question_type = input("Silmek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! 1-Çoktan Seçmeli 2-Klasik 3-Dogru Yanlış 4-Boşluk Doldurma")
# if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
#     if question_type == "1":
#         text = input("Soru Textinizi Yazınız!")
#         aranan=[]
#         for ogr in list_1:
#             if(ogr.text==text):
#                 aranan=[ogr]
#                 text = ogr.text
#                 index =list_1.index(ogr)
#                 print("Soru Sırası  {index}".format(index=index)+ "  {text}".format(text=text))
#         if(len(aranan) == 0):
#             print("Soru bulunamadı")
#         elif len(aranan) > 1:
#             del_index= input("Lütfen silmek istediğiniz sorunun yanındaki soru sırasını  yazınız!")
#             # for ogrenci in aranan:
#             #     print(str(ogrenci.text))
#     elif question_type == "1" or "2" or "3":
#         text = input("Soru Textinizi Yazınız!")

#         print("EklendiYeni!")
#         print("--------------")
# else:
#     print("Lütfen belirtilen şıklardan birinin numarasını yazınız!")

# # ----------------------------------------   END    -------------------------------------#


# # ----------------------------------------   START FOR LIST    -------------------------------------#


# question_type = input("Silmek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! \n 1-Çoktan Seçmeli \n 2-Klasik \n 3-Dogru Yanlış \n 4-Boşluk Doldurma")
# if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
#     if question_type == "1":
#         lst_choice = input("Lütfen arama yapmak istediğiniz şıkkı seçiniz! \n a.Soru metninde arama  \n b.Soru şıklarında arama \n c.Dogru şıklar üzerinde arama \n d.Puan üzerinde arama \n e.Zorluk derecesi üzerinde arama")
#         text = input("Lütfen arama yapmak istediğiniz kelimeyi Yazınız!")
#         aranan=[]
#         x =[]
#         if lst_choice == "a":
#             for ogr in list_1:
#                 for i in ogr.text.split(" "):
#                     if i== text:
#                             a = ogr.text
#                             b=ogr.choice
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_1.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"  Soru Şıkları : {b}".format(b=b) +"Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#             if(len(aranan) == 0):
#                 print("Soru bulunamadı!")
#         elif lst_choice == "b":
#             for ogr in list_1:
#                 for i in ogr.choice.split(" "):
#                     if i == text :
#                             a = ogr.text
#                             b=ogr.choice
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_1.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index} ".format(index=index) + "  Soru Metni : {a} ".format(a=a) +"  Soru Şıkları : {b} ".format(b=b) +" Doğru Cevap {c} ".format(c=c)+ " Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#             if(len(aranan) == 0):
#                 print("Soru bulunamadı!")
#         elif lst_choice == "c":
#             for ogr in list_1:
#                 for i in ogr.answer.split(" "):
#                     if i == text :
#                             a = ogr.text
#                             b=ogr.choice
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_1.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"  Soru Şıkları : {b}".format(b=b) +"Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#             if(len(aranan) == 0):
#                 print("Soru bulunamadı!")
#         elif lst_choice == "d":
#                     for ogr in list_1:
#                         if ogr.score == text:
#                             a=ogr.text
#                             b=ogr.choice
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_1.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"  Soru Şıkları : {b}".format(b=b) +"Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#                     if(len(aranan) == 0):
#                         print("Soru bulunamadı!")
#         elif lst_choice == "e":
#                     for ogr in list_1:
#                         if ogr.level == text:
#                             a = ogr.text
#                             b=ogr.choice
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_1.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"  Soru Şıkları : {b}".format(b=b) +"  Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#                     if(len(aranan) == 0):
#                         print("Soru bulunamadı!")


#     elif question_type ==  "2" or "3"or "4":
#         lst_choice = input("Lütfen arama yapmak istediğiniz şıkkı seçiniz! \n a.Soru metninde arama \n b.Cevaplar üzerinde arama \n c.Puan üzerinde arama \n d.Zorluk derecesi üzerinde arama")
#         if lst_choice == "a" or lst_choice == "b" or lst_choice == "c" or lst_choice == "d":
#             text = input("Lütfen arama yapmak istediğiniz kelimeyi Yazınız!")
#             x =[]
#             aranan= []
#             if lst_choice == "a":
#                 for ogr in list_2:
#                     for i in ogr.text.split(" "):
#                         if i== text:
#                             a=ogr.text
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_2.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#                 if(len(aranan) == 0):
#                     print("Soru bulunamadı!")
#             elif lst_choice == "b" :
#                 for ogr in list_2:
#                     for i in ogr.answer.split(" "):
#                         if i == text:
#                             a=ogr.text
#                             c=ogr.answer
#                             d=ogr.score
#                             e=ogr.level
#                             index = list_2.index(ogr)
#                             aranan.append(ogr)
#                             print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +" Doğru Cevap :{c} ".format(c=c)+ " Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                             print("---------------------------------------------------------------------------------")
#                 if(len(aranan) == 0):
#                     print("Soru bulunamadı!")
#             elif lst_choice == "c" :
#                 for ogr in list_2:
#                     if ogr.score == text:
#                         a=ogr.text
#                         c=ogr.answer
#                         d=ogr.score
#                         e=ogr.level
#                         index = list_2.index(ogr)
#                         aranan.append(ogr)
#                         print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                         print("---------------------------------------------------------------------------------")
#                 if(len(aranan) == 0):
#                     print("Soru bulunamadı!")
#             elif lst_choice == "d" :
#                 for ogr in list_2:
#                     if ogr.level == text:
#                         a = ogr.text
#                         c = ogr.answer
#                         d=ogr.score
#                         e=ogr.level
#                         index =list_2.index(ogr)
#                         aranan.append(ogr)
#                         print("Soru Numarası : {index}".format(index=index) + "  Soru Metni : {a}".format(a=a) +"Doğru Cevap {c} ".format(c=c)+ "Soru Puanları : {d}".format(d=d) +" Soru Zorluk Derecesi : {e} ".format(e=e) )
#                         print("---------------------------------------------------------------------------------")
#                 if(len(aranan) == 0):
#                     print("Soru bulunamadı!")
#         else :
#             print("OOPSS!Lütfen belirtilen şıklardan birini seçiniz!")


# # ----------------------------------------   END FOR LIST    -------------------------------------#


# # ----------------------------------------   START FOR QUIZ    -------------------------------------#


#type = input("Lütfen yapmak istediğiniz işlemi seçiniz? 1-Soru Ekleme 2-Test Yap 3-Soru Sil 4-Soru Listeleme")
# if type == "1":
#     question_bank = []
# question_data = type1.question_data()
# for q in question_data:
#     question_text = q["question"]
#     question_answer = q["answer"]
#     new_question = Question1(question_text, question_answer)
#     question_bank.append(new_question)
# ================================================================#

# quiz = Quiz(list_1)#sadece parametreyi yaz
# ================================================================#

# while quiz.still_has_question():
#     quiz.next_question()

# print("You have completed the quiz.")
# print(f"Your final score is {quiz.score}/100")

# if type=="2":
#     question_bank2 = []
#     question_data = type2.question_data()
#     for q in question_data:
#         question_text = q["question"]
#         question_answer = q["answer"]
#         question_choice =q["choice"]
#         new_question = Question2(question_text, question_answer,question_choice)
#         question_bank.append(new_question)
#     #================================================================#
#     quiz = Quiz(question_bank2)#sadece parametreyi yaz
#     #================================================================#

#     while quiz.still_has_question():
#         quiz.next_question()


#     print("You have completed the quiz.")
#     print(f"Your final score is {quiz.score}/100")


#     print("You have completed the quiz.")
#     print(f"Your final score is {quiz.score}/100")

# class Quiz:
#     def __init__(self, q_list):
#         self.question_number = 0
#         self.score = 0
#         self.question_list = q_list


#     def still_has_question(self):
#         return self.question_number < len(self.question_list)


#     def next_question(self):
#         current_question = self.question_list[self.question_number]
#         self.question_number += 1
#         user_answer = input(f"Q.{self.question_number}:{current_question.text}:(True|False)")
#         self.check_answer(user_answer, current_question.answer)

#     def check_answer(self, user_answer, answer):
#         if user_answer.lower() == answer.lower():
#             self.score += 10
#             print("Awesome!, You got it right!")
#         else:
#             self.score += 0
#             print("Oops! You got it wrong!")
#         print(f"The correct answer was {answer}.")
#         print(f"Your current_score is {self.score}/100.\n")
#         print("\n")

# class Quiz1:
#     def __init__(self, list):
#          self.question_index = 0
#          self.score = 0
#          list = list

#     def still_has_question(self):
#         return self.question_index < len(self.list)

#     def next_question(self):
#         current_question = self.list[self.question_index]
#         self.question_index += 1
#         user_answer = input("Soru Cevaplayınız!")
#         self.score +=10

#     def next_question1(self):
#         current_question = self.list[self.question_index]


q1 = MultiChoice("İnternet üzerinden görüntülü konuşma amacıyla kullanılan bilgisayar donanımı aşağıdakilerden hangisidir?",
                 "b", "10", "2", "a-Tarayıcı b-Web Kamerası c-Yazıcı d-Ekran")

q2 = MultiChoice("Bilgisayarın elle tutulabilen ve gözle görülebilen kısımlarına ne ad verilir?",
                 "a", "5", "1", "a-Donanım b-Sistem Yazılımı c-Uygulama Yazılımı d-Donatım")

q3 = MultiChoice("Aşağıdaki yazılımlardan hangisi sistem yazılımıdır?",
                 "d", "10", "2", "a- Google Chrome b-Paint c-Avira Antivirüs d-Windows8")

q4 = MultiChoice("Bilgisayardaki tüm işlemlerin yapıldığı dahili donanım birimi hangisidir?",
                 "c", "5", "1", "a- Anakart b-Ram c-İşlemci d-Sabit Disk")

q5 = MultiChoice("Bilgisayarın çalışma hızını belirleyen donanım birimleri hangileridir? I. Anakart II. Ram III. İşlemci IV. Güç Kaynağı",
                 "c", "20", "3", "a-I-II b-I-III c-II-III d-III-IV")

q6 = MultiChoice("Aşağıdakilerden hangisi dahili donanım birimidir?",
                 "b", "10", "2", "a-Kasa b-Anakart c-Ekran d-Tarayıcı")

q7 = MultiChoice("Aşağıdaki uygulama yazılımlarından hangisi yanlış eşleştirilmiştir?",
                 "d", "5", "1", "a-Eset Nod 32 - Antivirüs Yazılımı b-Mozilla Firefox - İnternet Tarayıcısı c-Paint - Resim Programı d-Microsoft Word - Sunum Programı")

q8 = MultiChoice("İnternete bağlanmamızı sağlayan donanım birimi aşağıdakilerden hangisidir?",
                 "a", "5", "1", "a-Modem b-Anakart c-İşlemci d-Ses Kartı")

q9 = MultiChoice("Müzik dinlemek için kullandığımız uygulama yazılımı aşağıdakilerden hangisidir?",
                 "d", "10", "2", "a-Paint b-Microsoft Powerpaint c-Avira d-Winamp")

q10 = MultiChoice("Aşağıdakilerden hangisi bir sistem yazılımıdır?",
                  "c", "10", "2", "a-Google Chrome b-İnternet Explorer c-Windows XP d-Adobe Photoshop")

list_1 = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

# ======================================================================================================================================= #

q1 = Question("Bilgisayardaki tüm bilgilerimizin kalıcı olarak depolandığı donanım birimi hangisidir?",
              "Sabit Disk", "20", "3")
q2 = Question("2-Yazılım nedir?",
              "Donanım ile kullanıcı arasındaki iletişimi kuran ve donanımı kontrol eden programlar", "10", "2")
q3 = Question(""" ………………… bilgisayardaki tüm donanım elemanları arasındaki iletişimi sağlar, bazı donanım elemanları ..................üzerinde yer alır; bazı donanım elemanları ise...................... kablolarla bağlıdır.
              İfadesinde noktalı olan yerlere aşağıdakilerden hangisi gelmelidir?""",   "Anakart", "10", "2")
q4 = Question("Tarayıcının işlevi nedir?",
              "Kâğıttaki bilgileri bilgisayara aktarmak", "10", "2")
q5 = Question("Derleme nedir",
              "Bilgisayarda bir programlama dili kullanılarak program yazılması", "20", "3")
q6 = Question("Geniş alan ağı (WAN) nedir?",
              "Aralarında ağ kurulu bir grup bilgisayarın fiziksel görünümü", "10", "3")
q7 = Question(
    "Python bir programlama dilidir. Lütfen doğru veya yanlış yazınız?", "Doğru", "10", "3")
q8 = Question(
    "2 GB kaç 2048 MB eder. Lütfen doğru veya yanlış yazınız?",   "Doğru", "5", "1")
q9 = Question("Veri iletmek ve bilgisayar kaynaklarını ortak kullanmak amacıyla birden fazla bilgisayarın birbirine bağlanmasına ……………………. denir.İfadesinde noktalı olan yerlere aşağıdakilerden hangisi gelmelidir?",   "Ağ", "10", "3")
q10 = Question(
    "Kızdırma Virüsleri bir virüs türüdür. Lütfen doğru veya yanlış yazınız?",   "Yanlış", "5", "1")

list_2 = [q1, q2, q3, q4, q5, q6, q7, q7, q8, q9, q10]

# ====================================================   FOR QUIZ    =================================================================================== #

# user_name = input(
#     "Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
# question_type = input(
#     "Listelemek istediğiniz soru tipini belirtiniz? Sadece numarasını yazınız! \n 1-Çoktan Seçmeli \n 2-Klasik \n 3-Dogru Yanlış \n 4-Boşluk Doldurma")
# if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
#     sum = 0
#     aranan = []
#     x = []
#     if question_type == "1":
#         ths = open("CoktanSecmeliSoruQuiz.txt", "w")
#         ths.write(user_name + "\n" + "-"*len(user_name))
#         ths.write("\n")
#         ths.write("Coktan Secmeli Soru Quiz")
#         ths.write("\n")
#         for ogr in list_1:
#             q_text = ogr.text
#             q_choice = ogr.choice
#             q_answer = ogr.answer
#             # q_score=ogr.score
#             q_level = ogr.level
#             index = list_1.index(ogr)
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
#             print("\n")

#             if user_answer.lower() == q_answer.lower():
#                 sum = sum + int(ogr.score)
#                 print("Cevabınız Doğru")
#             else:
#                 sum = sum + 0
#                 print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(
#                     q_answer=q_answer))

#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n"+" {q_choice}".format(q_choice=q_choice) +
#                       "\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print(
#                 "---------------------------------------------------------------------------------")
#     print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
#     ths.write("****************" +
#               f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************")
#     ths.close()
# elif question_type == "2" | question_type == "3" | question_type == "4":
#     sum = 0
#     aranan = []
#     x = []
#     if question_type == "1":
#         ths = open("KlasikSoruQuiz.txt", "w")
#         ths.write(user_name + "\n" + "-"*len(user_name))
#         ths.write("\n")
#         ths.write("\n")
#         for ogr in list_2:
#             q_text = ogr.text
#             q_answer = ogr.answer
#             # q_score=ogr.score
#             q_level = ogr.level
#             index = list_2.index(ogr)
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text))
#             print("\n")

#             if user_answer.lower() == q_answer.lower():
#                 sum = sum + int(ogr.score)
#                 print("Cevabınız Doğru")
#             else:
#                 sum = sum + 0
#                 print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(
#                     q_answer=q_answer))

#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" + " Doğru cevap: {q_answer}".format(
#                 q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print(
#                 "---------------------------------------------------------------------------------")
#     print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
#     ths.write("****************" +
#               f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************")
#     ths.close()
# elif question_type == "2" :
#     sum = 0
#     aranan = []
#     x = []
#     if question_type == "1":
#         ths = open("Sinav.txt", "w")
#         ths.write(user_name + "\n" + "-"*len(user_name))
#         ths.write("\n")
#         ths.write("\n")
#         for ogr in list_2:
#             q_text = ogr.text
#             q_answer = ogr.answer
#             # q_score=ogr.score
#             q_level = ogr.level
#             index = list_2.index(ogr)
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text))
#             print("\n")

#             if user_answer.lower() == q_answer.lower():
#                 sum = sum + int(ogr.score)
#             else:
#                 sum = sum + 0
#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" + " Doğru cevap: {q_answer}".format(
#                 q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print("---------------------------------------------------------------------------------")
#     ths.close()
# elif question_type == "3" :
#     sum = 0
#     aranan = []
#     x = []
#     if question_type == "1":
#         ths = open("Sinav.txt", "w")
#         ths.write(user_name + "\n" + "-"*len(user_name))
#         ths.write("\n")
#         ths.write("\n")
#         for ogr in list_2:
#             q_text = ogr.text
#             q_answer = ogr.answer
#             # q_score=ogr.score
#             q_level = ogr.level
#             index = list_2.index(ogr)
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text))
#             print("\n")

#             if user_answer.lower() == q_answer.lower():
#                 sum = sum + int(ogr.score)
#             else:
#                 sum = sum + 0
#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" + " Doğru cevap: {q_answer}".format(
#                 q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print("---------------------------------------------------------------------------------")
#     ths.close()


class Quiz1:
    def __init__(self):
        sum = 0
        aranan=[]
        x=[]
    def open_txt(self,user_name,ths):
        self.user_name = user_name
        self.ths = open("sinav.txt", "w")
        ths.write("Kullanıcı Adı ve Soyadı: " +user_name + "\n" + "-"*len(user_name))
        ths.write("\n")
        
    def close_txt(self):
        ths = open("sinav.txt", "a")
        ths.close()     
    
class MultiChoiceQuiz(Quiz1):
    def __init__(self,q_list):
        self.q_list = q_list
        sum = 0
        aranan=[]
        x=[]
    def MultiQuiz(self,q_list,sum):
        self.q_list = q_list
        self.sum = sum
        self.sum = 0
        aranan=[]
        index = 0
        q= Quiz1()
        ths = open("sinav.txt", "w")
        q.open_txt(self.user_name,ths)
        self.q_list = q_list
        
        for ogr in self.q_list:
            q_text = ogr.text
            q_choice = ogr.choice
            q_answer = ogr.answer
            q_score=ogr.score
            q_level = ogr.level
            index = index + 1
            aranan.append(ogr)
            user_answer = input("Soru {index}: ".format(
                index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
            print("\n")
            if user_answer.lower() == q_answer.lower():
                sum = sum + int(q_score)
                print("Cevabınız Doğru")
            else:
                sum = sum + 0
                print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
            
            ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n"+" {q_choice}".format(q_choice=q_choice) +
                      "\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
            ths.write("\n")
            
            print("---------------------------------------------------------------------------------")
            
        print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
        ths.write("\n****************" +f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************\n")
        self.close_txt()
        
class ClassicQuiz(Quiz1):
    def __init__(self,q_list):
        self.q_list = q_list
        sum = 0
        aranan=[]
        x=[]
    def ClassQuiz(self,q_list):
        self.q_list = q_list
        q= Quiz1()
        ths = open("sinav.txt", "w")
        q.open_txt(self.user_name, ths)
        self.q_list = q_list
        ths = open("sinav.txt", "w")
        aranan = []
        index =0
        for ogr in self.q_list:
            q_text = ogr.text
            q_answer = ogr.answer
            #q_score=ogr.score
            #q_level = ogr.level
            index = index + 1
            aranan.append(ogr)
            user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text))
            ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" +" Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
            ths.write("\n")
            print("\n")
            
            print("---------------------------------------------------------------------------------")
            
        print(f"Sınavınız Bitti!")
        ths.write("****************" +f" Sınav Sonucu daha açıklanamadı!"+"*************************")
        self.close_txt()    
    
class MixQuiz(Quiz1):
    def __init__(self,q_list1,q_list2):
        self.q_list1 = q_list1
        self.q_list2 = q_list2
        sum = 0
        aranan=[]
        x=[]
    def Mix_Ouiz(self):
        q= Quiz1()
        ths = open("yeni.txt", "w")
        self.open_txt(self.user_name,ths)
        sum = 0
        index =0
        aranan=[]
        for ogr in self.q_list1:
            q_text = ogr.text
            q_choice = ogr.choice
            q_answer = ogr.answer
            q_score=ogr.score
            q_level = ogr.level
            index = index + 1
            aranan.append(ogr)
            user_answer = input("Soru {index}: ".format(
                index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
            print("\n")
            if user_answer.lower() == q_answer.lower():
                sum = sum + int(q_score)
                print("Cevabınız Doğru")
            else:
                sum = sum + 0
                print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
            
            ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n"+" {q_choice}".format(q_choice=q_choice) +
                      "\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
            ths.write("\n")
            print("---------------------------------------------------------------------------------")
        for ogr in self.q_list2:
            q_text = ogr.text
            q_answer = ogr.answer
            #q_score=ogr.score
            #q_level = ogr.level
            index = index + 1
            aranan.append(ogr)
            user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text))
            ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" +" Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
            ths.write("\n")
            print("\n")
            
            print("---------------------------------------------------------------------------------")
        
        print(f"Sınavınız Bitti!")
        ths.write("****************" +f" Sınav Sonucu daha açıklanamadı!"+"*************************")
        self.close_txt()  
       
            
        
                   
        


# class Quiz:
#     def __init__(self,question_type,q_list):
#         self.question_type = question_type
#         self.q_list= q_list
#         sum = 0
#         aranan = []
#         x = []
#     def cls(self,q_list):
#         aranan = []
#         self.open_txt(user_name) #txt açmak için bir fonksiyon 
#         self.question_list(q_list) #soruları listelemek için fonksiyon
#         for ogr in q_list:
#             q_text = ogr.text
#             q_choice = ogr.choice
#             q_answer = ogr.answer
#             q_score=ogr.score
#             q_level = ogr.level
#             index = q_list.index(ogr)
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
#             print("\n")
            
#             self.check_answer(user_answer,q_answer,q_score) #Cevabı kontrol etmek için fonksiyon 
#             print("---------------------------------------------------------------------------------")
#             self.write_txt(user_answer,q_list,q_text,q_choice) #Txt sonuçları kaydetmek için fonksiyon
#             print("---------------------------------------------------------------------------------")
#         self.Result() #Sınav sonuçlarının hem txt de hem terminalda gösterimi için fonksiyon
#         self.close_txt() # txt dosyasının kapatılması için fonksiyon

#     def open_txt(self,user_name):
#         self.user_name = user_name
#         ths = open("CoktanSecmeliSoruQuiz.txt", "w")
#         ths.write(user_name + "\n" + "-"*len(user_name))
#         ths.write("\n")
#         ths.write("Coktan Secmeli Soru Quiz")
#         ths.write("\n")
    
#     def question_list(self,q_list):
#         q_list = q_list
#         aranan = []
#         for ogr in q_list:
#             q_text = ogr.text
#             q_choice = ogr.choice
#             q_answer = ogr.answer
#             q_score=ogr.score
#             q_level = ogr.level
#             index = q_list.index(ogr)
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
#             print("\n")    
#             self.check_answer(user_answer,q_answer)
               
#     def check_answer(self):
#         q_answer = self.ogr.answer
#         if user_answer.lower() == self.q_answer.lower():
#                 sum = self.sum + int(q_score)
#                 print("Cevabınız Doğru")
#         else:
#                 sum = sum + 0
#                 print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(
#                     q_answer=self.q_answer))

#     def write_txt(self):
 
#         q_answer = self.ogr.answer
#         ths = open("sinav.txt", 'w')
#         ths.write("Soru {index}: ".format(index=self.index) + "{q_text}".format(q_text=self.q_text) + "\n"+" {q_choice}".format(q_choice=self.q_choice) +
#                       "\n" " Doğru cevap: {q_answer}".format(q_answer=self.q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=self.user_answer))
#         ths.write("\n")
#         print("---------------------------------------------------------------------------------")
        
#     def close_txt(self):
#         self.ths.close()     
    
#     def result (self):
#         print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
#         self.ths.write("****************" +f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************")
from question_model import Transaction
from Quiz import MultiChoiceQuiz,ClassicQuiz,MixQuiz

mychoice = input("""Lütfen yapmak istediğiniz işlemin numarasını yazınız! \n ---------------\n 1-Soru bankasına soru ekleme \n
                 2-Soru bankasından soru çıkarma \n 3-Soru bankasındaki soruları listeleme \n 4-Sınav Oluşturma\n ---------------\n 5-Çıkış""")

if mychoice =="1":
    islem =Transaction()
    islem.Add_Question()
elif mychoice =="2":
    islem =Transaction()
    islem.Del_Question()
elif mychoice =="3":
     islem =Transaction()
     islem.List_Question        
elif mychoice == "4":
    question_type = input("Quiz için lütfen soru tipi seçiniz?Sadece numarasını yazınız! \n 1-Çoktan Seçmeli \n 2-Klasik \n 3-Karma ")
    if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":            
        if question_type=="1":
            user_name = input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
            quiz = MultiChoiceQuiz(list_1)
            ths = open("sinav.txt", "w")
            quiz.open_txt(user_name, ths)
            aranan = []
            sum=0
            quiz.MultiQuiz(list_1,0)
            print("---------------------------------------------------------------------------------")
            quiz.close_txt() # txt dosyasının kapatılması için fonksiyon
        elif question_type == "2":
            user_name = input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
            quiz = ClassicQuiz(list_2)
            ths = open("sinav.txt", "w")
            quiz.open_txt(user_name, ths)
            aranan = []
            sum=0
            quiz.ClassQuiz(list_2)
                
            print("---------------------------------------------------------------------------------")
            quiz.close_txt() # txt dosyasının kapatılması için fonksiyon
            
        elif question_type == "3":
            
            user_name = input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
            quiz = MixQuiz(list_1,list_2)
            ths = open("sinav.txt", "w")
            quiz.open_txt(user_name, ths)
            aranan = []
            sum=0
            quiz.Mix_Ouiz()
            print("---------------------------------------------------------------------------------")
            quiz.close_txt() # txt dosyasının kapatılması için fonksiyon
  
        else:
            print("Lütfen belirtilen seçeneklerden birini giriniz!")
elif mychoice =="5":
    exit()
          
else:
    print("Lütfen belirtilen seçeneklerden birini giriniz!")
