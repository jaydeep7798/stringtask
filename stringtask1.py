import logging
logging.basicConfig(filename="string1.log",level=logging.DEBUG,format=('%(asctime)s ,%(name)s ,%(levelname)s ,%(message)s'))
class string:
    def __init__(self,strings):
        logging.info("lets complete string task")
        self.strings=strings

    def try_to_jump_of_3(self):
        try:
            logging.debug("we are operating string opearion")
            logging.info(self.strings[0:10:3])
            return self.strings[0:10:3]
        finally:
            logging.error("No error found")
    def reverse_the_string(self):
        try:
            logging.debug("we are about reversed the string")
            logging.error(self.strings[::-1])
            return self.strings[::-1]
        except Exception as e:
            logging.exception(e)
    def try_to_to_in_uppercase(self):
        try:
            logging.debug("make string inro upper case")
            logging.info(self.strings.upper())
            return self.strings.upper()
        finally:
            logging.error("No error found")
    def try_to_inlowercase(self):
        try:
            logging.info("try to arrange into the lower case ")
            logging.info(self.strings.lower())
            logging.warning("no error found")
        except Exception as e:
            logging.exception(e)






s="this is My First Python programming class and i am learNING python string and its function"
s_string=string(s)
print(s_string.try_to_jump_of_3())
print(s_string.reverse_the_string())
print(s_string.try_to_to_in_uppercase())
print(s_string.try_to_inlowercase())


