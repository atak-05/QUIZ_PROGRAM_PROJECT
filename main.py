# -------------------------------    NESNE YÖNELİMLİ TASARIM VE ANALİZ PROJE ÖDEVİ    ---------------------------------------#
# --------------------------------------------    GIZEM TUNCER    -----------------------------------------------------------#
# --------------------------------------------    Y210240060    -------------------------------------------------------------#



from quiz_app.question_model import Question ,MultiChoice



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

# # ====================================================   FOR QUIZ    =================================================================================== #



# class Quiz1:
#     def __init__(self):
#         sum = 0
#         aranan=[]
#         x=[]
#     def open_txt(self,user_name,ths):
#         self.user_name = user_name
#         self.ths = open("sinav.txt", "w")
#         ths.write("Kullanıcı Adı ve Soyadı: " +user_name + "\n" + "-"*len(user_name))
#         ths.write("\n")
        
#     def close_txt(self):
#         ths = open("sinav.txt", "a")
#         ths.close()     
    
# class MultiChoiceQuiz(Quiz1):
#     def __init__(self,q_list):
#         self.q_list = q_list
#         sum = 0
#         aranan=[]
#         x=[]
#     def MultiQuiz(self,q_list,sum):
#         self.q_list = q_list
#         self.sum = sum
#         self.sum = 0
#         aranan=[]
#         index = 0
#         q= Quiz1()
#         ths = open("sinav.txt", "w")
#         q.open_txt(self.user_name,ths)
#         self.q_list = q_list
        
#         for ogr in self.q_list:
#             q_text = ogr.text
#             q_choice = ogr.choice
#             q_answer = ogr.answer
#             q_score=ogr.score
#             q_level = ogr.level
#             index = index + 1
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
#             print("\n")
#             if user_answer.lower() == q_answer.lower():
#                 sum = sum + int(q_score)
#                 print("Cevabınız Doğru")
#             else:
#                 sum = sum + 0
#                 print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
            
#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n"+" {q_choice}".format(q_choice=q_choice) +
#                       "\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
            
#             print("---------------------------------------------------------------------------------")
            
#         print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
#         ths.write("\n****************" +f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************\n")
#         self.close_txt()
        
# class ClassicQuiz(Quiz1):
#     def __init__(self,q_list):
#         self.q_list = q_list
#         sum = 0
#         aranan=[]
#         x=[]
#     def ClassQuiz(self,q_list):
#         self.q_list = q_list
#         q= Quiz1()
#         ths = open("sinav.txt", "w")
#         q.open_txt(self.user_name, ths)
#         self.q_list = q_list
#         ths = open("sinav.txt", "w")
#         aranan = []
#         index =0
#         for ogr in self.q_list:
#             q_text = ogr.text
#             q_answer = ogr.answer
#             #q_score=ogr.score
#             #q_level = ogr.level
#             index = index + 1
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text))
#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" +" Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print("\n")
            
#             print("---------------------------------------------------------------------------------")
            
#         print(f"Sınavınız Bitti!")
#         ths.write("****************" +f" Sınav Sonucu daha açıklanamadı!"+"*************************")
#         self.close_txt()    
    
# class MixQuiz(Quiz1):
#     def __init__(self,q_list1,q_list2):
#         self.q_list1 = q_list1
#         self.q_list2 = q_list2
#         sum = 0
#         aranan=[]
#         x=[]
#     def Mix_Ouiz(self):
#         q= Quiz1()
#         ths = open("yeni.txt", "w")
#         self.open_txt(self.user_name,ths)
#         sum = 0
#         index =0
#         aranan=[]
#         for ogr in self.q_list1:
#             q_text = ogr.text
#             q_choice = ogr.choice
#             q_answer = ogr.answer
#             q_score=ogr.score
#             q_level = ogr.level
#             index = index + 1
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(
#                 index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
#             print("\n")
#             if user_answer.lower() == q_answer.lower():
#                 sum = sum + int(q_score)
#                 print("Cevabınız Doğru")
#             else:
#                 sum = sum + 0
#                 print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
            
#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n"+" {q_choice}".format(q_choice=q_choice) +
#                       "\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print("---------------------------------------------------------------------------------")
#         for ogr in self.q_list2:
#             q_text = ogr.text
#             q_answer = ogr.answer
#             #q_score=ogr.score
#             #q_level = ogr.level
#             index = index + 1
#             aranan.append(ogr)
#             user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text))
#             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" +" Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
#             ths.write("\n")
#             print("\n")
            
#             print("---------------------------------------------------------------------------------")
        
#         print(f"Sınavınız Bitti!")
#         ths.write("****************" +f" Sınav Sonucu daha açıklanamadı!"+"*************************")
#         self.close_txt()  
       
from quiz_app.question_model import Transaction
from quiz_app.question_model import Question
from quiz_app.Quiz import Quiz1

mychoice = input("""Lütfen yapmak istediğiniz işlemin numarasını yazınız! \n ---------------\n 1-Soru bankasına soru ekleme
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
