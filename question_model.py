
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



class Transaction:
    
     # -------------------   START FOR ADD  -------------------------------------------------------------------------#
    def Add_Question(self, list_1=None, list_2=None):
        self.list_1 = list_1
        self.list_2 = list_2
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
  

        
    def Del_Question(self, list_1=None, list_2=None):
        self.list_1 = list_1
        self.list_2 = list_2
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

        
    def List_Question(self, list_1=None, list_2=None):
        self.list_1 = list_1
        self.list_2 = list_2
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
        
        


