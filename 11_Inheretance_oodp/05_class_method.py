class employee:
    a=1
    @classmethod
    def show(cls):
        print(f"the calss value of a is {cls.a}")
e= employee()
e.a = 453
# @classmethod --> is used to print what is in 
# the calss and  if we do't put it & put like e.a = 453
# 453 willl be printed  
e.show()
