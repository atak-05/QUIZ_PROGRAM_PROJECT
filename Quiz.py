# -------------------------------    NESNE YÖNELİMLİ TASARIM VE ANALİZ PROJE ÖDEVİ    ---------------------------------------#
# --------------------------------------------    GIZEM TUNCER    -----------------------------------------------------------#
# --------------------------------------------    Y210240060    -------------------------------------------------------------#



#Quiz uygulamasına ilişkin sınıflar ve metotlar p
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
    def exit(self):
        exit()
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
            ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" +
                      " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
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
            ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n" +" Doğru cevap: {q_answer}".format(q_answer=q_answer)+
                      " Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
            ths.write("\n")
            print("\n")
            
            print("---------------------------------------------------------------------------------")
        
        print(f"Sınavınız Bitti!")
        ths.write("****************" +f" Sınav Sonucu daha açıklanamadı!"+"*************************")
        self.close_txt()  
       
            
        