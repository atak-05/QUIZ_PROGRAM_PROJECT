# ==============Klasik Soru Tipi - Dogru\Yanlış - Boşluk Doldurma ==================#
# from quiz_brain import Quiz


# class Question2():
#     question_data_type_1 = [
#         {"question": "En iyi programlama dili pythondur",   "answer": "True"},]

#     def __init__(self, question, answer):
#         self.question = question
#         self.answer = answer

#     def question_ekle(self):
#         self.question_data_type_1.append(self.question)
#         self.question_data_type_1.append(self.answer)
#         print('{} adlı kişi personele eklendi'.format(self.question))

#     def question_listele(self):
#         print('Personel listesi:')
#         for kişi in self.question_data_type_1:
#             print(kişi)


# # ==============================Çoktan Seçmeli Soru Tipi ============================#
# class Question1():
#     question_data_type_2 = []

#     def __init__(self, question, answer, choice):
#         self.question = question
#         self.answer = answer
#         self.choice = choice

#     def question_ekle(self):
#         self.question_data_type_2.append(self.question)
#         self.question_data_type_2.append(self.answer)
#         self.question_data_type_2.append(self.choice)
#         print('{} adlı kişi personele eklendi'.format(self.question))

#     def question_listele(self):
#         print('Personel listesi:')
#         for kişi in self.question_data_type_2:
#             print(kişi)

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
   
                
         
        
q1 = Question("Soru1",   "Cevap1", "10", "3")
q2 = Question("Soru2",   "Cevap2", "10", "3")
q3 = Question("Soru3",   "Cevap3", "10", "3")
q4 = Question("Soru3",   "Cevap3", "10", "3")
q5 = Question("Soru3",   "Cevap3", "10", "3")
q6 = Question("Soru3",   "Cevap3", "10", "3")
q7 = Question("Soru3",   "Cevap3", "10", "3")
q8 = Question("Soru3",   "Cevap3", "10", "3")
q9 = Question("Soru3",   "Cevap3", "10", "3")
q10 = Question("Soru3",   "Cevap3", "10", "3")

list_2 = [q1, q2, q3, q4, q5, q6, q7, q7, q8, q9, q10]



        

class MultiChoice(Question):
    def __init__(self, text, answer, score, level,choice):
        super().__init__(text, answer, score, level)
        self.choice = choice

# =============== Çoktan Seçmeli Soru Tipleri için===========================================================================#

q1 = MultiChoice("Soru1",   "a", "10", "3", "a- b- c- d-")
q2 = MultiChoice("Soru2",   "a", "10", "3", "a- b- c- d-")
q3 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q4 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q5 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q6 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q7 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q8 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q9 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")
q10 = MultiChoice("Soru3",   "a", "10", "3", "a- b- c- d-")


list_1 = [q1, q2, q3, q4, q5, q6,q7,q8, q9, q10]
class TrueFalse(Question):
    pass
        

class Classic(Question):
    pass


class GapFilling(Question):
    pass



from data import list_1, list_2
class Islemler:
    
     # -------------------   START FOR ADD  -------------------------------------------------------------------------#
    def SoruEkle():
        question_type = input("Eklemek istediğiniz soru tipini belirtiniz?Sadece numarasını yazınız! 1-Çoktan Seçmeli 2-Klasik 3-Dogru Yanlış 4-Boşluk Doldurma")
        if question_type == "1" or question_type == "2" or question_type == "3" or question_type == "4":
            num = int(input('Kaç adet soru eklemek istiyorsunuz: '))
            i = 0
            while(i<num):
                if question_type == "1":
                    text = input("Soru Textinizi Yazınız!")
                    answer = input("Cevap Textinizi Yazınız!")
                    score = input("Lütfen bu soru için puan belirleyiniz!")
                    level = input("Lütfen bu soru için 1'den 3'e kadar seviye belirleyiniz.Örneğin; 1")
                    choice = input("Lütfen seçeneklerinizi belirleyin. Örnek olarak; a-Soru Şıkkı b-Soru Şıkkı c-Soru Şıkkı d-Soru Şıkkı")
                    new = MultiChoice(text,answer,score,level,choice )
                    list_2.append(new)
                    i += 1
                elif question_type == "1" or "2" or "3":
                    text = input("Soru Textinizi Yazınız!")
                    answer = input("Cevap Textinizi Yazınız!")
                    score = input("Lütfen bu soru için puan belirleyiniz!")
                    level = input("Lütfen bu soru için 1'den 3'e kadar seviye belirleyiniz.Örneğin; 1")
                    new = Question(text,answer, score,level )
                    list_1.append(new)
                    i += 1
                    
                print("EklendiYeni!")
                print("--------------")
        else:
            print("Lütfen belirtilen şıklardan birinin numarasını yazınız!")
        
    

    # -------------------   END FOR ADD ------------------------------------------------------------------------#    
    #----------------------------------------------------------------------------------------------------------------#
  

        
    def SoruSil(self):
        # # ----------------------------------------   START FOR DELETE    -------------------------------------#
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
            
        # # ----------------------------------------   END FOR DELETE    -------------------------------------#
        #-----------------------------------------------------------------------------------------------------#   
        
         
        # # ----------------------------------------   START FOR LIST    -------------------------------------#

        
    def SoruListele(self):
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
         
         

    def SoruGüncelle(self):
        pass
        
        


