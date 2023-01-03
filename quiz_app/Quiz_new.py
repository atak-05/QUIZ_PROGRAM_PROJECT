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
        self.ths = open("data/sinav.txt", "w")
        ths.write("Kullanıcı Adı ve Soyadı: " +user_name + "\n" + "-"*len(user_name))
        ths.write("\n")
        
    def close_txt(self):
        ths = open("data/sinav.txt", "a")
        ths.close()     
        
    def exit(self):
        exit()
    
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
class MultiChoiceQuiz(Quiz1):
    def __init__(self,q_list):
        self.q_list = q_list
        sum = 0
        aranan=[]
        x=[]
        
    # def level_choice(self,level_):
    #     self.level_ = level_
    #     if level_ == "1":
    #         print ("Seçtiğiniz Seviye : Kolay ")
    #     elif  level_ == "2":
    #         print ("Seçtiğiniz Seviye : Orta ")
    #     elif level_ == "3":
    #         print ("Seçtiğiniz Seviye : Zor ")
    #     else: 
    #         print ("Lütfen belirtilen şıklardan birini seçiniz!")

    def sort_question(self,aranan):
        self.aranan =aranan
        for a in self.aranan:
            q_text = a.text
            q_choice = a.choice
            q_answer = a.answer
            q_score=a.score
            q_level = a.level
            print(f"Seviye : {q_level}")
        print(f'\n{"-" * 16}\n')
        
    def append(self,q_list,aranan_list,aranan_1,aranan_2,aranan_3):
        self.q_list=q_list
        for ogr in self.q_list:
            q_level = ogr.level
            if q_level == "1": 
                aranan_1.append(ogr)
            elif q_level == "2":
                aranan_2.append(ogr)
            elif q_level == "3":
                aranan_3.append(ogr)  
        print(f'\n{"-"*50}\n')  
        aranan_list= [aranan_1,aranan_2,aranan_3]
        return aranan_list         
    
    def check_answer(self,aranan_list,ths):
        sum=0
        index = 0
        for i in aranan_list:
            for j in i:
                q_answer = j.answer
                q_score = j.score
                q_choice = j.choice
                q_text =j.text
                index= index+1
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
                    
                    print("---------------------------------------------------------------------------------")
        print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
        ths.write("\n****************" +f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************\n")
        self.close_txt()
            
        
    def MultiQuiz(self,q_list):
        self.q_list = q_list
        self.user_name = input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
        q= Quiz1()
        ths = open("data/sinav.txt", "w")
        q.open_txt(self.user_name,ths)
        self.q_list = q_list
        level_ = input("Lütfen quiz için seçmek istediğiniz zorluk seviyesini belirtiniz? 1-Kolay 2-Orta 3-Zor Not:Lütfen sadece sayı giriniz!")
        self.level_choice(level_)
        aranan_1=[]
        aranan_2=[]
        aranan_3=[]
        aranan_list =[aranan_1,aranan_2,aranan_3]
        
        self.append(q_list,aranan_list,aranan_1,aranan_2,aranan_3)
        for i in aranan_list:
            self.sort_question(i)
        self.check_answer(aranan_list,ths)
        
        
       
      

        
    def MultiQuiz(self,q_list):
        self.q_list = q_list
        self.user_name = input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
        q= Quiz1()
        ths = open("data/sinav.txt", "w")
        q.open_txt(self.user_name,ths)
        self.q_list = q_list
        level_ = input("Lütfen quiz için seçmek istediğiniz zorluk seviyesini belirtiniz? 1-Kolay 2-Orta 3-Zor Not:Lütfen sadece sayı giriniz!")
        self.level_choice(level_)
        aranan_1=[]
        aranan_2=[]
        aranan_3=[]
        aranan_list =[aranan_1,aranan_2,aranan_3]
        
        self.append(q_list,aranan_list,aranan_1,aranan_2,aranan_3)
        for i in aranan_list:
            self.sort_question(i)
        self.check_answer(aranan_list,ths)
            





class ClassicQuiz1(Quiz1):   
    
    def __init__(self,q_list):
        super().__init__()
        self.q_list = q_list
        sum = 0
        aranan=[]
        x=[]
    def sort_question(self,aranan):
        self.aranan =aranan
        for a in self.aranan:
            q_text = a.text
            q_answer = a.answer
            q_score=a.score
            q_level = a.level
            print(f"Seviye : {q_level}")
        print(f'\n{"-" * 16}\n')
        
    def append(self,q_list,aranan_list,aranan_1,aranan_2,aranan_3):
        self.q_list=q_list
        for ogr in self.q_list:
            q_level = ogr.level
            if q_level == "1": 
                aranan_1.append(ogr)
            elif q_level == "2":
                aranan_2.append(ogr)
            elif q_level == "3":
                aranan_3.append(ogr)  
        print(f'\n{"-"*50}\n')  
        aranan_list= [aranan_1,aranan_2,aranan_3]
        return aranan_list         
    
    def check_answer(self,aranan_list,ths):
        sum=0
        index = 0
        self.ths=ths
        for i in aranan_list:
            for j in i:
                q_answer = j.answer
                q_score = j.score
                q_text =j.text
                index= index+1
                user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text))
                # if user_answer.lower() == q_answer.lower():
                #     # sum = sum + int(q_score)
                #     # print("Cevabınız Doğru")
                # else:
                #     sum = sum + 0
                #     print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
                ths.write(f'Soru  {index} : {q_text} "/n" Doğru Cevap: {q_score} "/n" Kullanıcı Cevap: {user_answer}')  
                # self.ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) +"\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer)")
                ths.write("\n")
                    
                print("---------------------------------------------------------------------------------")
        print(f'Sınav sonucunuz en kısa zamanda bildirilecektir.')
        ths.write(f'\n{"*" * 16}\nSınav sonucunuz en kısa zamanda bildirilecektir!.\n{"*" * 16}\n')
        self.close_txt()
    
    def ClassQuiz(self,q_list):
        self.q_list = q_list
        self.user_name = input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
        q= Quiz1()
        ths = open("data/sinav.txt", "w")
        q.open_txt(self.user_name,ths)
        self.q_list = q_list
        level_ = input("Lütfen quiz için seçmek istediğiniz zorluk seviyesini belirtiniz? 1-Kolay 2-Orta 3-Zor Not:Lütfen sadece sayı giriniz!")
        self.level_choice(level_)
        aranan_1=[]
        aranan_2=[]
        aranan_3=[]
        aranan_list =[aranan_1,aranan_2,aranan_3]
        
        self.append(q_list,aranan_list,aranan_1,aranan_2,aranan_3)
        for i in aranan_list:
            self.sort_question(i)
        self.check_answer(aranan_list,ths)
            

class MixQuiz1(Quiz1):
    def __init__(self,list_1,list_2):
        self.list_1 = list_1
        self.list_2 = list_2
 
    def sort_question_is_classic(self,aranan):
        self.aranan =aranan
        for a in self.aranan:
            q_text = a.text
            q_answer = a.answer
            q_score=a.score
            q_level = a.level
            print(f"Seviye : {q_level}")
        print(f'\n{"-" * 16}\n')
        
    def sort_question_is_multi(self,aranan):
        self.aranan =aranan
        for a in self.aranan:
            q_text = a.text
            q_choice = a.choice
            q_answer = a.answer
            q_score=a.score
            q_level = a.level
            print(f"Seviye : {q_level}")
        print(f'\n{"-" * 16}\n')
        
    def append(self,q_list,aranan_list,aranan_1,aranan_2,aranan_3):
        self.q_list=q_list
        for ogr in self.q_list:
            q_level = ogr.level
            if q_level == "1": 
                aranan_1.append(ogr)
            elif q_level == "2":
                aranan_2.append(ogr)
            elif q_level == "3":
                aranan_3.append(ogr)  
        print(f'\n{"-"*50}\n')  
        aranan_list= [aranan_1,aranan_2,aranan_3]
        return aranan_list      

    def check_answer_is_classic(self,aranan_list,ths):
        sum=0
        index = 0
        self.ths=ths
        for i in aranan_list:
            for j in i:
                q_answer = j.answer
                q_score = j.score
                q_text =j.text
                index= index+1
                user_answer = input("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text))
                # if user_answer.lower() == q_answer.lower():
                #     # sum = sum + int(q_score)
                #     # print("Cevabınız Doğru")
                # else:
                #     sum = sum + 0
                #     print("Cevaınız Yanlış! Doğru Cevap : {q_answer}".format(q_answer=q_answer))
                ths.write(f'Soru  {index} : {q_text} "/n" Doğru Cevap: {q_score} "/n" Kullanıcı Cevap: {user_answer}')  
                # self.ths.write("Soru {index}: ".format(index=index) + "{q_text}".format(q_text=q_text) +"\n" " Doğru cevap: {q_answer}".format(q_answer=q_answer)+" Kullanıcı Cevabı : {user_answer} ".format(user_answer=user_answer)")
                ths.write("\n")
                    
                print("---------------------------------------------------------------------------------")
        # print(f'Sınav sonucunuz en kısa zamanda bildirilecektir.')
        # ths.write(f'\n{"*" * 16}\nSınav sonucunuz en kısa zamanda bildirilecektir!.\n{"*" * 16}\n')
        # self.close_txt()

    def check_answer_is_multi(self,aranan_list,ths):
        sum=0
        index = 0
        for i in aranan_list:
            for j in i:
                q_answer = j.answer
                q_score = j.score
                q_choice = j.choice
                q_text =j.text
                index= index+1
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
                    
                    print("---------------------------------------------------------------------------------")
        # print(f"Sınav Sonucunuz : {sum}/100.\n".format(sum=sum))
        # ths.write("\n****************" +f" Sınav Sonucunuz : {sum}/100.".format(sum=sum)+"*************************\n")
        # self.close_txt() 
    def mix_quiz(self):
        list_1 =self.list_1
        list_2 = self.list_2
        user_name =  input("Lütfen Ad ve Soyadınızı aralarında boşluk bırakarak yazınız!")
        q= Quiz1()
        ths = open("sinav.txt", "w")
        self.open_txt(user_name,ths)
        sum = 0
        index =0
        aranan_1=[]
        aranan_2=[]
        aranan_3=[]
        aranan_list_is_multi =[aranan_1,aranan_2,aranan_3]
        aranan_4=[]
        aranan_5=[]
        aranan_6=[]
        aranan_list_is_classic =[aranan_4,aranan_5,aranan_6]
        self.append(list_1,aranan_list_is_multi,aranan_1,aranan_2,aranan_3)
        self.append(list_2,aranan_list_is_classic,aranan_4,aranan_5,aranan_6)

        for i in aranan_list_is_multi:
            self.sort_question_is_multi(i)
        self.check_answer_is_multi(aranan_list_is_multi,ths)
        for i in aranan_list_is_multi:
            self.sort_question_is_multi(i)
        self.check_answer_is_classic(aranan_list_is_classic,ths)
   
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
       
            
        