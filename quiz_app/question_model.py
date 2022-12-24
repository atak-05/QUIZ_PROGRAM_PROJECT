

# ==============================Question ================================================================================================================#
# 

class Question:
    question_list = []
    def __init__(self, text, answer, score, level):
        self.text = text
        self.answer = answer
        self.score = score
        self.level = level
    def checkAnswer(self, answer):
        return self.answer == answer
   
                
class MultiChoice(Question):
    def __init__(self, text, answer, score, level,choice):
        super().__init__(text, answer, score, level)
        self.choice = choice

# =============== Çoktan Seçmeli Soru Tipleri için===========================================================================#

class TrueFalse(Question):
    pass
        

class Classic(Question):
    pass


class GapFilling(Question):
    pass

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
                 "d", "5", "1", "a-Eset Nod 32 - Antivirüs Yazılımı b-Mozilla Firefox - İnternet Tarayıcısıactua c-Paint - Resim Programı d-Microsoft Word - Sunum Programı")

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






class Transaction:
         
     # -------------------   START FOR ADD  -------------------------------------------------------------------------#
    def Add_Question(self):
        question_type = input("Eklemek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! 1-Çoktan Seçmeli 2-Klasik 3-Dogru Yanlış 4-Boşluk Doldurma")
        if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
            num =input('Kaç adet soru eklemek istiyorsunuz: ')
            num = int(num)
            i = 0
            while(i<num):
                if question_type == "1":
                    text = input("Soru Textinizi Yazınız!")
                    answer = input("Cevap Textinizi Yazınız!")
                    score = input("Lütfen bu soru için puan belirleyiniz!")
                    level = input("Lütfen bu soru için 1'den 3'e kadar seviye belirleyiniz.Örneğin; 1")
                    choice = input("Lütfen seçeneklerinizi belirleyin. Örnek olarak; a-Soru Şıkkı b-Soru Şıkkı c-Soru Şıkkı d-Soru Şıkkı")
                    new = MultiChoice(text,answer,score,level,choice )
                    self.list_1.append(new)
                    i += 1
                elif question_type == "1" or "2" or "3":
                    text = input("Soru Textinizi Yazınız!")
                    answer = input("Cevap Textinizi Yazınız!")
                    score = input("Lütfen bu soru için puan belirleyiniz!")
                    level = input("Lütfen bu soru için 1'den 3'e kadar seviye belirleyiniz.Örneğin; 1")
                    new = Question(text,answer, score,level )
                    self.list_2.append(new)
                    i += 1
                                
                    print("EklendiYeni!")
                    print("--------------")
        else:
            print("Lütfen belirtilen şıklardan birinin numarasını yazınız!")
               
        
    

    # -------------------   END FOR ADD ------------------------------------------------------------------------#    
    #----------------------------------------------------------------------------------------------------------------#
  

        
    def Del_Question(self):	
        # # ----------------------------------------   START FOR DELETE    -------------------------------------#
        question_type = input("Silmek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! 1-Çoktan Seçmeli 2-Klasik 3-Dogru Yanlış 4-Boşluk Doldurma")
        if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
            if question_type == "1":
                text = input("Soru Textinizi Yazınız!")
                aranan=[]
                x =[]
                for ogr in self.list_1:
                    for i in ogr.text.split(" "):
                        if i== text: 
                            a = ogr.text
                            index = self.list_1.index(ogr)
                            aranan.append(i)
                            print("Soru Numarası : {index}".format(index=index) +"  Soru Metni :  {a}   ".format(a=a))
                            print("---------------------------------------------------------------------------------")

                if(len(aranan) == 0):
                        print("Soru bulunamadı!")
                elif len(aranan) >= 1:
                            del_index= int(input("Lütfen silmek istediğiniz sorunun yanındaki soru numarısını yazınız!"))
                            self.list_1.pop(del_index)
                            print(" Sorunuz listeden silindi! ")
                            print(" {del_index} ".format(del_index=del_index) +" nolu sorunuz listeden silindi! ")
                            # for ogrenci in aranan:
                            #     print(str(ogrenci.text))
            elif question_type ==  "2" or "3"or "4":
                text = input("Soru Textinizi Yazınız!")
                aranan=[]
                x =[]
                for ogr in self.list_2:
                    for i in ogr.text.split(" "):
                        if i== text: 
                            a = ogr.text
                            index = list_2.index(ogr)
                            aranan.append(i)
                            print("Soru Numarası : {index}".format(index=index) +"  Soru Metni :  {a}   ".format(a=a))
                            print("---------------------------------------------------------------------------------")
                if(len(aranan) == 0):
                    print("Soru bulunamadı!")
                elif len(aranan) >= 1:
                    del_index= int(input("Lütfen silmek istediğiniz sorunun yanındaki soru numarısını yazınız!"))
                    self.list_2.pop(del_index)
                    print(" {del_index}".format(del_index=del_index) +" Sorunuz listeden silindi! ")

        else:
            print("Lütfen belirtilen şıklardan birinin numarasını yazınız!")
            
        # # ----------------------------------------   END FOR DELETE    -------------------------------------#
        #-----------------------------------------------------------------------------------------------------#   
        
         
        # # ----------------------------------------   START FOR LIST    -------------------------------------#

        
    def List_Question(self):
        question_type = input("Silmek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! 1-Çoktan Seçmeli 2-Klasik 3-Dogru Yanlış 4-Boşluk Doldurma")
        if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
                if question_type == "1":
                    text = input("Soru Textinizi Yazınız!")
                    aranan=[]
                    x =[]
                    for ogr in list_1:
                        for i in ogr.text.split(" "):
                            if i== text: 
                                a = ogr.text
                                index = list_1.index(ogr)
                                aranan.append(i)
                                print("Soru Numarası : {index}".format(index=index) +"  Soru Metni :  {a}   ".format(a=a))
                                print("---------------------------------------------------------------------------------")

                    if(len(aranan) == 0):
                            print("Soru bulunamadı!")
                    elif len(aranan) >= 1:
                                del_index= int(input("Lütfen silmek istediğiniz sorunun yanındaki soru numarısını yazınız!"))
                                list_1.pop(del_index)
                                print(" Sorunuz listeden silindi! ")
                                print(" {del_index} ".format(del_index=del_index) +" nolu sorunuz listeden silindi! ")
                                # for ogrenci in aranan:
                                #     print(str(ogrenci.text))
                elif question_type ==  "2" or "3"or "4":
                    text = input("Soru Textinizi Yazınız!")
                    aranan=[]
                    x =[]
                    for ogr in list_2:
                        for i in ogr.text.split(" "):
                            if i== text: 
                                a = ogr.text
                                index = list_2.index(ogr)
                                aranan.append(i)
                                print("Soru Numarası : {index}".format(index=index) +"  Soru Metni :  {a}   ".format(a=a))
                                print("---------------------------------------------------------------------------------")
                    if(len(aranan) == 0):
                        print("Soru bulunamadı!")
                    elif len(aranan) >= 1:
                        del_index= int(input("Lütfen silmek istediğiniz sorunun yanındaki soru numarısını yazınız!"))
                        list_2.pop(del_index)
                        print(" {del_index}".format(del_index=del_index) +" Sorunuz listeden silindi! ")

        else:
            print("Lütfen belirtilen şıklardan birinin numarasını yazınız!")
            
            
         # # ----------------------------------------   END FOR LIST    -------------------------------------#
         #---------------------------------------------------------------------------------------------------#    
         
        
        


