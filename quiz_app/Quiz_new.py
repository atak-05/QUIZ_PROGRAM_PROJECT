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
        
    def level_choice(self,level_):
        self.level_ = level_
        if level_ == "1":
            print ("Seçtiğiniz Seviye : Kolay ")
        elif  level_ == "2":
            print ("Seçtiğiniz Seviye : Orta ")
        elif level_ == "3":
            print ("Seçtiğiniz Seviye : Zor ")
        else: 
            print ("Lütfen belirtilen şıklardan birini seçiniz!")
    def sort (self,nums):
        for i in range(0,len(nums)):
            for j in range(0,len(nums)-1):
                if nums[j]> nums[j+1]:
                    nums[j] , nums[j+1] = nums[j+1], nums[j]
                else:
                    continue
                 
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
        level_ = input("Lütfen quiz için seçmek istediğiniz zorluk seviyesini belirtiniz? 1-Kolay 2-Orta 3-Zor Not:Lütfen sadece sayı giriniz!")
        self.level_choice(level_)
        m=1
        k=[1]
        m=1
        for ogr in self.q_list:
            q_text = ogr.text
            q_choice = ogr.choice
            q_answer = ogr.answer
            q_score=ogr.score
            q_level = ogr.level
            for i in range(4):
                if int(q_level) == i:
                    print ("level {q_level}".format(q_level =q_level))
                else:
                    continue
                for j in range (4):
                    if int(q_level) == j:
                        print ("level {q_level}".format(q_level =q_level))
                    else:
                        for l in range (4):
                            if int(q_level) == l:
                                print ("level {q_level}".format(q_level =q_level))
                            else:
                                continue
                        
                    
            

                    
                # if q_level == int(i): 
                #         index = index + 1
                #         aranan.append(ogr)
                #         user_answer = input("Soru {index}: ".format(
                #             index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
                #         print("\n")
                #         if user_answer.lower() == q_answer.lower():
                #             sum = sum + int(q_score)
                #             print("Cevabınız Doğru")
                #         else:
                #             sum = sum + 0
                #             print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
                    
        #             ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + "\n"+" {q_choice}".format(q_choice=q_choice) +
        #                     "\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer))
        #             ths.write("\n")
                    
        #             print("---------------------------------------------------------------------------------")
                    
            
                    
            
        print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
        ths.write("\n****************" +f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************\n")
        self.close_txt()
        
        
        def quiz_list(self,q_list,sum):
            self.q_list = q_list
            index = index + 1
            aranan.append(ogr)
            user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) + " {q_choice}".format(q_choice=q_choice))
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
       
            
        